
from datetime import datetime


class Posko:
    """
    Merepresentasikan satu posko penanggulangan bencana.

    Atribut:
        id_posko  : Identifikasi unik posko (mis. 'P001')
        nama      : Nama posko (mis. 'Posko Utama Pekanbaru')
        lokasi    : Alamat / koordinat lokasi posko
        kapasitas : Jumlah maksimal korban yang dapat ditampung
        jumlah_pengungsi : Jumlah pengungsi saat ini
        status    : 'aktif' / 'penuh' / 'tidak aktif'
        dibuat_pada : Timestamp pembuatan data
    """

    STATUS_VALID = {"aktif", "penuh", "tidak aktif"}

    def __init__(self, id_posko: str, nama: str, lokasi: str,
                 kapasitas: int = 100, jumlah_pengungsi: int = 0,
                 status: str = "aktif"):
        self.id_posko          = id_posko.strip().upper()
        self.nama              = nama.strip()
        self.lokasi            = lokasi.strip()
        self.kapasitas         = max(0, kapasitas)
        self.jumlah_pengungsi  = max(0, jumlah_pengungsi)
        self.status            = status if status in self.STATUS_VALID else "aktif"
        self.dibuat_pada       = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # ──────────────────────────────────────────────
    # Property & Helper
    # ──────────────────────────────────────────────

    @property
    def sisa_kapasitas(self) -> int:
        return max(0, self.kapasitas - self.jumlah_pengungsi)

    @property
    def persentase_terisi(self) -> float:
        if self.kapasitas == 0:
            return 0.0
        return round((self.jumlah_pengungsi / self.kapasitas) * 100, 1)

    def update_status_otomatis(self):
        """Memperbarui status berdasarkan kapasitas secara otomatis."""
        if self.jumlah_pengungsi >= self.kapasitas:
            self.status = "penuh"
        elif self.status == "penuh" and self.jumlah_pengungsi < self.kapasitas:
            self.status = "aktif"

    def tambah_pengungsi(self, jumlah: int = 1) -> bool:
        """Menambahkan pengungsi ke posko. Gagal jika sudah penuh."""
        if self.jumlah_pengungsi + jumlah > self.kapasitas:
            return False
        self.jumlah_pengungsi += jumlah
        self.update_status_otomatis()
        return True

    def kurangi_pengungsi(self, jumlah: int = 1) -> bool:
        """Mengurangi jumlah pengungsi (setelah dipindahkan/pulang)."""
        if self.jumlah_pengungsi - jumlah < 0:
            return False
        self.jumlah_pengungsi -= jumlah
        self.update_status_otomatis()
        return True

    # ──────────────────────────────────────────────
    # Tampilan
    # ──────────────────────────────────────────────

    def tampilkan(self):
        status_ikon = {"aktif": "🟢", "penuh": "🔴", "tidak aktif": "⚪"}
        ikon = status_ikon.get(self.status, "❓")
        print(f"  ┌─ ID      : {self.id_posko}")
        print(f"  ├─ Nama    : {self.nama}")
        print(f"  ├─ Lokasi  : {self.lokasi}")
        print(f"  ├─ Status  : {ikon} {self.status.upper()}")
        print(f"  ├─ Kapasitas: {self.jumlah_pengungsi}/{self.kapasitas} ({self.persentase_terisi}%)")
        print(f"  └─ Dibuat  : {self.dibuat_pada}")

    def __repr__(self):
        return (f"Posko(id={self.id_posko}, nama={self.nama}, "
                f"status={self.status}, "
                f"{self.jumlah_pengungsi}/{self.kapasitas})")

    # ──────────────────────────────────────────────
    # Serialisasi
    # ──────────────────────────────────────────────

    def to_dict(self) -> dict:
        return {
            "id_posko":         self.id_posko,
            "nama":             self.nama,
            "lokasi":           self.lokasi,
            "kapasitas":        self.kapasitas,
            "jumlah_pengungsi": self.jumlah_pengungsi,
            "status":           self.status,
            "dibuat_pada":      self.dibuat_pada,
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Posko':
        obj = cls(
            id_posko=data["id_posko"],
            nama=data["nama"],
            lokasi=data["lokasi"],
            kapasitas=data.get("kapasitas", 100),
            jumlah_pengungsi=data.get("jumlah_pengungsi", 0),
            status=data.get("status", "aktif"),
        )
        obj.dibuat_pada = data.get("dibuat_pada", obj.dibuat_pada)
        return obj
