class Korban: #class menyimpa ndata korban
    def __init__(self, nama, lokasi, kondisi):
        self.nama = nama
        self.lokasi = lokasi
        self.kondisi = kondisi
    
    def to_dict(self): #neyimpan data ke dictionary
        return{
            "nama" : self.nama,
            "lokasi" : self.lokasi,
            "kondisi" : self.kondisi
        }
    
