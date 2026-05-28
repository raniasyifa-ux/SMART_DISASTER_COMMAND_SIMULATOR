class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class SingularLinkedList:
            def __init__(self):
                self.head = None
            
            #menambahkan data
            def tambah(self, data):
                nodebaru = Node(data)

                if self.head == None:
                    self.head = nodebaru
                    return
                
                now = self.head

                while now.next:
                    now = now.next
                
                now.next = nodebaru

            #menampilkan datanya
            def tampil(self):
                now = self.head

                if self.head is None:
                    print("KOSONGGGGG")
                    return
                
                while now:
                    print(f"NAMA : {now.data.nama}")
                    print(f"LOKASI : {now.data.lokasi}")
                    print(f"KONDISI: {now.data.kondisi}")
                    print("-----" * 10)
                
                    now = now.next

            def hapus(self, nama):
                now = self.head

                prev = None

                if now is None:
                    return False
                  
                if now.data.nama.lower() == nama.lower():
                    self.head = now.next
                    return True
                while now:
                    if now.data.nama.lower() == nama.lower():
                     break
                    prev = now
                    now = now.next
                
                if now is None:
                    return False
                
                prev.next = now.next
                return True
            
            def update(self, namaLama, namaBaru, lokasiBaru, kondisiBaru):
                sekarang = self.head

                while sekarang:
                    if sekarang.data.nama.lower() == namaLama.lower():
                        sekarang.data.nama = namaBaru
                        sekarang.data.lokasi = lokasiBaru
                        sekarang.data.kondisi = kondisiBaru

                        return True
                    sekarang = sekarang.next
                
                return False

                  
                  
