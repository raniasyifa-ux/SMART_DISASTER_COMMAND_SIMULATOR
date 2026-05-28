class Node:  # node circular linked list

    def __init__(self, data):  # simpan data node
        self.data = data  # isi data
        self.next = None  # pointer next


class CircularLinkedList:  # struktur notifikasi berulang

    def __init__(self):  # list kosong
        self.head = None  # belum ada data

    def add(self, data):  # tambah notifikasi
        new_node = Node(data)  # buat node baru

        if self.head is None:  # jika list kosong
            self.head = new_node  # node jadi head
            new_node.next = self.head  # pointer ke dirinya sendiri
            return  # selesai

        temp = self.head  # mulai dari head

        while temp.next != self.head:  # cari node terakhir
            temp = temp.next  # pindah ke node berikutnya

        temp.next = new_node  # sambungkan node terakhir
        new_node.next = self.head  # kembali ke head (circular)

    def display(self, limit=10):  # tampilkan data (dibatasi)
        result = []  # hasil output

        if self.head is None:  # jika kosong
            return result  # return kosong

        temp = self.head  # mulai dari head
        count = 0  # counter

        while count < limit:  # batas looping agar tidak infinite
            result.append(temp.data)  # simpan data
            temp = temp.next  # pindah node
            count += 1  # tambah counter

        return result  # return hasil