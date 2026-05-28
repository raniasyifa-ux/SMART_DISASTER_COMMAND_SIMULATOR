
import os
import platform


# ──────────────────────────────────────────────────────────────
# Helper Tampilan
# ──────────────────────────────────────────────────────────────

def bersihkan_layar():
    """Membersihkan layar terminal."""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def garis(panjang: int = 55, karakter: str = "─"):
    print(karakter * panjang)


def header(judul: str, lebar: int = 55):
    """Mencetak header menu dengan judul di tengah."""
    print("\n" + "═" * lebar)
    print(f"  {'SMART DISASTER COMMAND SIMULATOR':^{lebar-4}}")
    print(f"  {judul:^{lebar-4}}")
    print("═" * lebar)


def sub_header(judul: str, lebar: int = 55):
    print(f"\n{'─'*lebar}")
    print(f"  {judul:^{lebar-4}}")
    print(f"{'─'*lebar}")


def pesan_berhasil(pesan: str):
    print(f"\n  ✅  {pesan}")


def pesan_error(pesan: str):
    print(f"\n  ❌  {pesan}")


def pesan_info(pesan: str):
    print(f"\n  ℹ️   {pesan}")


def tunggu_enter():
    input("\n  Tekan Enter untuk melanjutkan...")


def input_pilihan(prompt: str = "Pilih menu") -> str:
    return input(f"\n  {prompt} : ").strip()


def konfirmasi(pertanyaan: str) -> bool:
    """Meminta konfirmasi ya/tidak dari pengguna."""
    jawaban = input(f"\n  {pertanyaan} (y/n) : ").strip().lower()
    return jawaban == "y"


# ──────────────────────────────────────────────────────────────
# Menu Jalur Evakuasi (Fitur 4)
# ──────────────────────────────────────────────────────────────

def menu_evakuasi():
    """Menampilkan menu utama Simulasi Jalur Evakuasi."""
    header("🗺️  SIMULASI JALUR EVAKUASI")
    print("  1. Tambah Lokasi")
    print("  2. Tambah Jalur Evakuasi")
    print("  3. Tampilkan Peta Wilayah")
    print("  4. Cari Jalur Tercepat (Dijkstra)")
    print("  5. Cari Jalur BFS (Paling Sedikit Titik)")
    print("  6. Cari Jalur DFS")
    print("  7. Simulasi Perpindahan Tim Penyelamat")
    print("  8. Hapus Jalur")
    print("  9. Hapus Lokasi")
    print("  0. Kembali ke Menu Utama")
    garis()


def menu_tambah_lokasi() -> str:
    sub_header("➕ TAMBAH LOKASI BARU")
    return input("  Nama Lokasi : ").strip()


def menu_tambah_jalur() -> tuple:
    """Mengembalikan (asal, tujuan, jarak, dua_arah)."""
    sub_header("➕ TAMBAH JALUR EVAKUASI")
    asal    = input("  Lokasi Asal   : ").strip()
    tujuan  = input("  Lokasi Tujuan : ").strip()
    try:
        jarak = float(input("  Jarak (km)    : ").strip())
    except ValueError:
        pesan_error("Jarak tidak valid.")
        return None, None, None, None
    dua_arah_input = input("  Dua arah? (y/n) [default: y] : ").strip().lower()
    dua_arah = dua_arah_input != "n"
    return asal, tujuan, jarak, dua_arah


def menu_cari_jalur(label: str = "CARI JALUR") -> tuple:
    """Mengembalikan (asal, tujuan)."""
    sub_header(f"🔍 {label}")
    asal   = input("  Lokasi Asal   : ").strip()
    tujuan = input("  Lokasi Tujuan : ").strip()
    return asal, tujuan


def menu_simulasi_tim() -> tuple:
    """Mengembalikan (nama_tim, asal, tujuan)."""
    sub_header("🚑 SIMULASI PERPINDAHAN TIM")
    nama_tim = input("  Nama Tim      : ").strip()
    asal     = input("  Lokasi Asal   : ").strip()
    tujuan   = input("  Lokasi Tujuan : ").strip()
    return nama_tim, asal, tujuan


# ──────────────────────────────────────────────────────────────
# Menu Struktur Posko (Fitur 6)
# ──────────────────────────────────────────────────────────────

def menu_posko():
    """Menampilkan menu utama Simulasi Struktur Posko."""
    header("🏠 SIMULASI STRUKTUR POSKO")
    print("  1. Tambah Posko Utama")
    print("  2. Tambah Posko Cabang")
    print("  3. Tampilkan Struktur Posko (Tree)")
    print("  4. Tampilkan Semua Detail Posko")
    print("  5. Traversal Preorder (Rekursif)")
    print("  6. Traversal Postorder (Rekursif)")
    print("  7. Traversal Per Level")
    print("  8. Jalur Komando ke Posko Utama")
    print("  9. Update Jumlah Pengungsi")
    print(" 10. Hapus Posko")
    print(" 11. Statistik Posko")
    print("  0. Kembali ke Menu Utama")
    garis()


def menu_tambah_posko_utama() -> tuple:
    """Mengembalikan (id_posko, nama, lokasi, kapasitas)."""
    sub_header("🏠 TAMBAH POSKO UTAMA")
    id_posko = input("  ID Posko    : ").strip()
    nama     = input("  Nama Posko  : ").strip()
    lokasi   = input("  Lokasi      : ").strip()
    try:
        kapasitas = int(input("  Kapasitas   : ").strip())
    except ValueError:
        pesan_error("Kapasitas tidak valid. Gunakan angka.")
        return None, None, None, None
    return id_posko, nama, lokasi, kapasitas


def menu_tambah_posko_cabang() -> tuple:
    """Mengembalikan (id_posko, nama, lokasi, kapasitas, id_induk)."""
    sub_header("🏢 TAMBAH POSKO CABANG")
    id_posko = input("  ID Posko Baru   : ").strip()
    nama     = input("  Nama Posko      : ").strip()
    lokasi   = input("  Lokasi          : ").strip()
    try:
        kapasitas = int(input("  Kapasitas       : ").strip())
    except ValueError:
        pesan_error("Kapasitas tidak valid.")
        return None, None, None, None, None
    id_induk = input("  ID Posko Induk  : ").strip()
    return id_posko, nama, lokasi, kapasitas, id_induk


def menu_update_pengungsi() -> tuple:
    """Mengembalikan (id_posko, jumlah, mode)."""
    sub_header("👥 UPDATE JUMLAH PENGUNGSI")
    id_posko = input("  ID Posko    : ").strip()
    try:
        jumlah = int(input("  Jumlah      : ").strip())
    except ValueError:
        pesan_error("Jumlah tidak valid.")
        return None, None, None
    mode_input = input("  Mode (1=Tambah / 2=Kurangi) : ").strip()
    mode = "tambah" if mode_input == "1" else "kurangi"
    return id_posko, jumlah, mode


# ──────────────────────────────────────────────────────────────
# Menu Utama (dipakai main.py, mengarahkan ke submenu)
# ──────────────────────────────────────────────────────────────

def menu_utama(peran: str = "admin"):
    """Menampilkan menu utama berdasarkan peran pengguna."""
    header(f"  MENU UTAMA  |  Peran: {peran.upper()}")
    print("  1. Simulasi Data Korban")
    print("  2. Simulasi Distribusi Bantuan")
    print("  3. Simulasi Jalur Evakuasi")
    print("  4. Simulasi Prioritas Wilayah")
    print("  5. Simulasi Struktur Posko")
    print("  6. Simulasi Histori Aktivitas")
    print("  7. Simulasi Notifikasi Darurat")
    print("  8. Penyimpanan & Laporan")
    print("  0. Logout")
    garis()
