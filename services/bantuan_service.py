import json  # library JSON

from structures.queue import Queue  # import queue FIFO
from structures.stack import Stack  # import stack LIFO
from structures.doubly_linked_list import DoublyLinkedList  # histori
from structures.circular_linked_list import CircularLinkedList  # notifikasi
from models.bantuan import Bantuan  # model bantuan
from models.notifikasi import Notifikasi  # model notifikasi
from utils.validator import validate_string  # validasi input
from services.histori_service import tambah_histori  # histori file

DATA_FILE = "data/bantuan.json"  # file penyimpanan


class BantuanService:  # service utama bantuan

    def __init__(self):  # inisialisasi
        self.queue = Queue()  # antrean bantuan
        self.stack = Stack()  # undo bantuan
        self.histori = DoublyLinkedList()  # histori sistem
        self.notif = CircularLinkedList()  # notifikasi

        self.load_data()  # load data awal

    def load_data(self):  # ambil data dari file

        try:  # coba buka file
            with open(DATA_FILE, "r") as f:  # buka file
                data = json.load(f)  # ubah JSON ke Python

                for item in data:  # loop data
                    self.queue.enqueue(item)  # masukkan ke queue

        except:  # jika file tidak ada
            self.queue = Queue()  # buat queue baru

    def save_data(self):  # simpan data

        with open(DATA_FILE, "w") as f:  # buka file write
            json.dump(self.queue.display(), f, indent=4)  # simpan JSON

    def tambah_bantuan(self, id_bantuan, nama, jenis, jumlah, lokasi):  # tambah bantuan

        if not validate_string(nama):  # cek validasi nama
            return "Data tidak valid"  # jika salah

        bantuan = Bantuan(id_bantuan, nama, jenis, jumlah, lokasi)  # buat object

        self.queue.enqueue(bantuan.to_dict())  # masuk queue
        self.stack.push(bantuan.to_dict())  # masuk stack

        self.histori.add(f"Tambah: {nama}")  # simpan histori
        self.notif.add(f"Bantuan {nama} masuk")  # notifikasi

        self.save_data()  # simpan file
        tambah_histori(f"Bantuan {nama} ditambahkan")  # histori txt

        return "Bantuan berhasil ditambahkan"  # output

    def proses_bantuan(self):  # proses FIFO

        data = self.queue.dequeue()  # ambil data pertama

        if data:  # jika ada data
            self.histori.add(f"Proses: {data['nama']}")  # histori
            tambah_histori(f"Proses {data['nama']}")  # file txt
            self.save_data()  # simpan
            return data  # return data

        return "Tidak ada bantuan"  # jika kosong

    def undo(self):  # undo stack

        data = self.stack.pop()  # ambil data terakhir

        if data:  # jika ada data
            self.histori.add(f"Undo: {data['nama']}")  # histori
            return f"Undo {data['nama']}"  # output

        return "Tidak ada undo"  # jika kosong

    def tampilkan_antrian(self):  # tampil queue
        return self.queue.display()  # return data

    def tampilkan_histori(self):  # tampil histori
        return self.histori.display()  # return data

    def tampilkan_notifikasi(self):  # tampil notif
        return self.notif.display()  # return data