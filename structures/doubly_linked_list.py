class Node:  # node untuk Doubly Linked List

    def __init__(self, data):  # menyimpan data node
        self.data = data  # isi data
        self.prev = None  # pointer ke node sebelumnya
        self.next = None  # pointer ke node berikutnya


class DoublyLinkedList:  # struktur histori aktivitas

    def __init__(self):  # membuat list kosong
        self.head = None  # awal list belum ada data

    def add(self, data):  # tambah histori baru
        new_node = Node(data)  # membuat node baru

        if self.head is None:  # jika list masih kosong
            self.head = new_node  # node jadi head pertama
            return  # selesai

        temp = self.head  # mulai dari head

        while temp.next:  # selama belum sampai akhir
            temp = temp.next  # pindah ke node berikutnya

        temp.next = new_node  # sambungkan node terakhir ke baru
        new_node.prev = temp  # set pointer balik ke node sebelumnya

    def display(self):  # tampilkan histori
        result = []  # list untuk hasil

        temp = self.head  # mulai dari head

        while temp:  # selama node masih ada
            result.append(temp.data)  # ambil data
            temp = temp.next  # pindah ke node berikutnya

        return result  # return semua histori