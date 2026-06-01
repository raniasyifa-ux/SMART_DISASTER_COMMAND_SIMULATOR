from models.korban import Korban
from structures.singly_linked_list import SingularLinkedList
from utils.file_handler import load_data, save_file
from algorithms.searching import linear_search
from algorithms.sorting import bubbleSort
from services.notifikasi_services import tambah_notifikasi
from services.posko_service import PoskoService

FILEKORBAN = "data/korban.json"

# membuat linked list untuk korban
data_korban = SingularLinkedList()

# instance posko service (shared, load sekali)
_posko_service = PoskoService()


# ============================================================
# LOAD & SIMPAN
# ============================================================

def loadKorban():
    data_korban.head
    data = load_data(FILEKORBAN)

    for i in data:
        korban = Korban(
            i["nama"],
            i["lokasi"],
            i["kondisi"],
            i.get("id_posko", None),
            i.get("nama_posko", None)
        )
        data_korban.tambah(korban)


def simpan():
    data = []
    now = data_korban.head
    while now:
        data.append(now.data.to_dict())
        now = now.next
    save_file(FILEKORBAN, data)


# ============================================================
# HELPER: Tampilkan daftar posko aktif dan minta pilihan admin
# ============================================================

def _pilih_posko() -> tuple:
    """
    Menampilkan semua posko yang tersedia, lalu meminta admin
    memilih ID posko untuk korban. Mengembalikan (id_posko, nama_posko)
    atau (None, None) jika dilewati.
    """
    print("\n  ---- DAFTAR POSKO TERSEDIA ----")

    posko_aktif = []
    for pid, posko in _posko_service.data_posko.items():
        sisa = posko.sisa_kapasitas
        ikon = "🟢" if posko.status == "aktif" else ("🔴" if posko.status == "penuh" else "⚪")
        print(f"  {ikon} [{pid}] {posko.nama} | Sisa: {sisa}/{posko.kapasitas} | Status: {posko.status.upper()}")
        if posko.status != "penuh":
            posko_aktif.append(pid)

    if not posko_aktif:
        print("  [!] Semua posko sudah penuh. Korban tidak dapat ditempatkan.")
        return None, None

    print("  [0] Lewati (tidak tempatkan ke posko sekarang)")
    id_input = input("\n  Masukkan ID Posko untuk korban ini: ").strip().upper()

    if id_input == "0" or id_input == "":
        return None, None

    posko_dipilih = _posko_service.data_posko.get(id_input)
    if not posko_dipilih:
        print(f"  [!] ID Posko '{id_input}' tidak ditemukan. Korban tidak ditempatkan.")
        return None, None

    if posko_dipilih.status == "penuh":
        print(f"  [!] Posko '{posko_dipilih.nama}' sudah PENUH. Pilih posko lain.")
        return None, None

    return posko_dipilih.id_posko, posko_dipilih.nama


# ============================================================
# CRUD KORBAN
# ============================================================

def tambahkorban():
    nama    = input("MASUKKAN NAMA KORBAN   : ")
    lokasi  = input("MASUKKAN LOKASI        : ")
    kondisi = input("MASUKKAN KONDISI TERKINI: ")

    # --- Fitur Penempatan ke Posko ---
    print("\n  Apakah ingin langsung menempatkan korban ke posko?")
    print("  [1] Ya   [2] Tidak")
    pilih_posko = input("  Pilihan: ").strip()

    id_posko   = None
    nama_posko = None

    if pilih_posko == "1":
        id_posko, nama_posko = _pilih_posko()

        if id_posko:
            # update jumlah pengungsi di posko yang dipilih
            berhasil = _posko_service.update_pengungsi(id_posko, 1, "tambah")
            if berhasil:
                print(f"\n  Korban berhasil ditempatkan di: {nama_posko} [{id_posko}]")
            else:
                print("  [!] Gagal menambah pengungsi ke posko. Korban tetap disimpan tanpa posko.")
                id_posko   = None
                nama_posko = None

    korbanBaru = Korban(nama, lokasi, kondisi, id_posko, nama_posko)
    data_korban.tambah(korbanBaru)
    simpan()

    print("\nBERHASIL! DATA KORBAN SUDAH DITAMBAHKAN.")
    if id_posko:
        print(f"Korban ditempatkan di Posko: {nama_posko} [{id_posko}]")
    else:
        print("Korban belum ditempatkan di posko manapun.")

    tambah_notifikasi(f"Korban baru: {nama}", "DARURAT")


def tampil():
    data_korban.tampil()


def cari():
    nama = input("MASUKKAN NAMA KORBAN YANG AKAN DICARI: ")
    hasil = linear_search(data_korban, nama)

    if hasil:
        print("\n DATA TELAH DITEMUKAN")
        print(f"NAMA KORBAN    : {hasil.nama}")
        print(f"LOKASI KORBAN  : {hasil.lokasi}")
        print(f"KONDISI KORBAN : {hasil.kondisi}")
        if hasil.id_posko:
            print(f"POSKO          : {hasil.nama_posko} [{hasil.id_posko}]")
        else:
            print("POSKO          : Belum ditempatkan")
    else:
        print("DATA TIDAK DITEMUKAN, SILAHKAN ULANGI")


def urut():
    data = []
    now = data_korban.head
    while now:
        data.append(now.data)
        now = now.next

    hasil = bubbleSort(data)

    print("DATA KORBAN YANG TELAH DIURUTKAN")
    for korban in hasil:
        print(f"NAMA KORBAN    : {korban.nama}")
        print(f"LOKASI KORBAN  : {korban.lokasi}")
        print(f"KONDISI KORBAN : {korban.kondisi}")
        if korban.id_posko:
            print(f"POSKO          : {korban.nama_posko} [{korban.id_posko}]")
        else:
            print("POSKO          : Belum ditempatkan")
        print("-" * 30)


def hapus():
    nama = input("MASUKKAN NAMA KORBAN YANG INGIN DIHAPUS: ")

    # cek dulu apakah korban punya posko, agar bisa kurangi pengungsi
    now = data_korban.head
    korban_ditemukan = None
    while now:
        if now.data.nama.lower() == nama.lower():
            korban_ditemukan = now.data
            break
        now = now.next

    hasil = data_korban.hapus(nama)

    if hasil:
        # jika korban ada di posko, kurangi jumlah pengungsi
        if korban_ditemukan and korban_ditemukan.id_posko:
            _posko_service.update_pengungsi(korban_ditemukan.id_posko, 1, "kurangi")
            print(f"Jumlah pengungsi di Posko {korban_ditemukan.id_posko} diperbarui.")

        save_file(FILEKORBAN, nama)
        print("DATA BERHASIL DIHAPUS")
    else:
        print("DATA TIDAK DITEMUKAN")

    tambah_notifikasi(f"Korban dihapus: {nama}", "INFO")


def update():
    namaLama = input("Masukkan Nama Korban yang ingin di Update: ")
    namaBaru = input("Masukkan Nama Baru: ")
    lokasiBaru = input("Masukkan Lokasi Terbaru: ")
    kondisiBaru = input("Masukkan Kondisi Terbaru: ")

    hasil = data_korban.update(
        namaLama, namaBaru, lokasiBaru, kondisiBaru
    )

    if hasil:
        simpan()
        print("DATA BERHASIL DIPERBARUI")
    else:
        print("DATA TIDAK DITEMUKAN")
