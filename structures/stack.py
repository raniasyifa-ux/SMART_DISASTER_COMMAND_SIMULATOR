class Stack:  # struktur data Stack (LIFO)

    def __init__(self):  # membuat stack kosong
        self.items = []  # list untuk menyimpan data

    def is_empty(self):  # cek apakah stack kosong
        return len(self.items) == 0  # True jika kosong

    def push(self, item):  # tambah data ke stack
        self.items.append(item)  # masukkan ke atas stack

    def pop(self):  # ambil data terakhir
        if self.is_empty():  # jika stack kosong
            return None  # tidak ada data
        return self.items.pop()  # ambil data terakhir (LIFO)

    def display(self):  # tampilkan isi stack
        return self.items  # return semua data