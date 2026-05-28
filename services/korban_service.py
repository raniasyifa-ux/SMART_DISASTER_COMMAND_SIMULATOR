from models.korban import Korban
from structures.singly_linked_list import SingularLinkedList
from utils.file_handler import load_data, save_file
from algorithms.searching import linear_search
from algorithms.sorting import bubbleSort
from services.notifikasi_services import tambah_notifikasi
FILEKORBAN = "data/korban.json"

#membbuat linked list untuk korban
data_korban = SingularLinkedList()

#mengambil data korban.json ke linkedlist
def loadKorban():
    data_korban.head
    data = load_data(FILEKORBAN)
    
    for i in data:
        korban = Korban(
            i["nama"],
            i["lokasi"],
            i["kondisi"]
        )
    
        data_korban.tambah(korban)

def simpan():
    data = []

    now = data_korban.head

    while now:
        data.append(now.data.to_dict())
        now = now.next
    
    save_file(FILEKORBAN, data)


def tambahkorban():
    nama = input("MASUKKAN NAMA KORBAN: ")
    lokasi = input("MASUKKAN LOKASI NYA: ")
    kondisi = input("MASUKKAN KONDISI TERKINI: ")

    korbanBaru = Korban(nama, lokasi, kondisi)
    data_korban.tambah(korbanBaru)

    simpan()
    print("BERHASIL DAN SUDAH DI TAMBAHKAN")

    tambah_notifikasi(f"Korban baru: {nama}","DARURAT")

def tampil():
    data_korban.tampil()

def cari():
    nama = input("MASUKKAN NAMA KORBAN YANG AKAN DICARI: ")
    hasil = linear_search(data_korban, nama)
    
    if hasil:
        print("\n DATA TELAH DI TEMUKAN")
        print(f"NAMA KORBAN : {hasil.nama}")
        print(f"LOKASI KORBAN : {hasil.lokasi}")
        print(f"KONDISI KORBAN : {hasil.kondisi}")
    else:
        print("DATA TIDAK DITEMUKAN, SILAHKAN ULANGI")

def urut():
    data = []
    now = data_korban.head

    while now:
        data.append(now.data)
        now = now.next

    hasil = bubbleSort(data)

    print("DATA KORBAN YANG TERLAH DIURUTKAN")

    for korban in hasil:
         print(f"NAMA KORBAN : {korban.nama}")
         print(f"LOKASI KORBAN : {korban.lokasi}")
         print(f"KONDISI KORBAN : {korban.kondisi}")
         print("-" * 10)

def hapus():
    nama = input("MASUKKAN NAMA KORBAN YANG INGIN DIHAPUS: ")
    hasil = data_korban.hapus(nama)

    if hasil:
        save_file(FILEKORBAN, nama)
        print("DATA BERHASIL DIHAPUS")
    else:
        print("DATA TIDAK DITEMUKAN")
    tambah_notifikasi(f"Korban dihapus: {nama}","INFO")

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
        print("DATA BERHASIL DI PERBAHARUI")
    else:
        print("DATA TIDAK DITEMUKAN")