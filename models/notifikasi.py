class Notifikasi:  # class notifikasi bencana

    def __init__(self, pesan, level="INFO"):  # konstruktor
        self.pesan = pesan  # isi pesan
        self.level = level  # level info

    def to_dict(self):  # ubah ke dictionary
        return {
            "pesan": self.pesan,
            "level": self.level
        }

    def __str__(self):  # tampilan notifikasi
        return f"[{self.level}] {self.pesan}"