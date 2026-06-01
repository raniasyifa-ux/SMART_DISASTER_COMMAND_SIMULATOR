class Korban: #class menyimpan data korban
    def __init__(self, nama, lokasi, kondisi, id_posko=None, nama_posko=None):
        self.nama = nama
        self.lokasi = lokasi
        self.kondisi = kondisi
        self.id_posko = id_posko        # ID posko tempat korban ditempatkan
        self.nama_posko = nama_posko    # Nama posko (untuk kemudahan tampil)
    
    def to_dict(self): #menyimpan data ke dictionary
        return {
            "nama"       : self.nama,
            "lokasi"     : self.lokasi,
            "kondisi"    : self.kondisi,
            "id_posko"   : self.id_posko,
            "nama_posko" : self.nama_posko
        }
