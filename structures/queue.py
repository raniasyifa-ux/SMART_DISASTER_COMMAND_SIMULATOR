class Queue:  # struktur data Queue (FIFO)

    def __init__(self):  # membuat queue kosong
        self.items = []  # list untuk menyimpan data

    def is_empty(self):  # cek apakah queue kosong
        return len(self.items) == 0  # jika panjang 0 maka kosong

    def enqueue(self, item):  # tambah data ke belakang
        self.items.append(item)  # memasukkan item ke list

    def dequeue(self):  # ambil data paling depan
        if self.is_empty():  # jika queue kosong
            return None  # tidak ada data untuk diambil
        return self.items.pop(0)  # hapus data index pertama (FIFO)

    def display(self):  # tampilkan isi queue
        return self.items  # mengembalikan semua data