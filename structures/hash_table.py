class HashTable:

    def __init__(self):
        self.table = {}

    # tambah data
    def tambah(self, key, value):
        self.table[key] = value

    # ambil data
    def ambil(self, key):
        return self.table.get(key)

    # hapus data
    def hapus(self, key):

        if key in self.table:
            del self.table[key]
            return True

        return False

    # tampilkan semua data
    def tampil(self):

        for key, value in self.table.items():
            print(f"{key} : {value}")