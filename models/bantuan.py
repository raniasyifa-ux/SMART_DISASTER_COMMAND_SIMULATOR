class Bantuan:  # class OOP bantuan

    def __init__(self, id_bantuan, nama, jenis, jumlah, lokasi):  # konstruktor
        self.id_bantuan = id_bantuan  # id bantuan
        self.nama = nama  # nama bantuan
        self.jenis = jenis  # jenis bantuan
        self.jumlah = jumlah  # jumlah bantuan
        self.lokasi = lokasi  # lokasi bantuan

    def to_dict(self):  # ubah ke dictionary untuk JSON
        return {
            "id_bantuan": self.id_bantuan,
            "nama": self.nama,
            "jenis": self.jenis,
            "jumlah": self.jumlah,
            "lokasi": self.lokasi
        }

    def __str__(self):  # tampilan string
        return f"{self.nama} ({self.jenis}) - {self.jumlah} - {self.lokasi}"