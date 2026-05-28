from structures.graph import Graph
import json
import os
import time

DATA_FILE = "data/jalur.json"


class EvakuasiService:
    def __init__(self):
        self.graph = Graph()
        self.muat_data()

    # ──────────────────────────────────────────────
    # File Handler
    # ──────────────────────────────────────────────

    def simpan_data(self):
        """Menyimpan data graph jalur evakuasi ke file JSON."""
        os.makedirs("data", exist_ok=True)
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(self.graph.to_dict(), f, ensure_ascii=False, indent=2)

    def muat_data(self):
        """Memuat data graph dari file JSON jika tersedia."""
        if not os.path.exists(DATA_FILE):
            return
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.graph.from_dict(data)
        except (json.JSONDecodeError, KeyError):
            print("  [!] Gagal memuat data jalur. Memulai dengan data kosong.")

    # ──────────────────────────────────────────────
    # 4.1 Tambah Jalur Evakuasi
    # ──────────────────────────────────────────────

    def tambah_lokasi(self, nama_lokasi: str):
        """Menambahkan titik lokasi baru ke peta evakuasi."""
        nama_lokasi = nama_lokasi.strip()
        if nama_lokasi in self.graph.vertices:
            print(f"  [!] Lokasi '{nama_lokasi}' sudah ada di peta.")
            return
        self.graph.tambah_lokasi(nama_lokasi)
        self.simpan_data()
        print(f"  ✅ Lokasi '{nama_lokasi}' berhasil ditambahkan.")

    def tambah_jalur(self, asal: str, tujuan: str, jarak: float,
                     dua_arah: bool = True):
        """
        Menghubungkan dua lokasi dengan jalur evakuasi.
        Jalur secara default bersifat dua arah.
        """
        asal   = asal.strip()
        tujuan = tujuan.strip()
        if jarak <= 0:
            print("  [!] Jarak harus lebih dari 0.")
            return
        self.graph.tambah_jalur(asal, tujuan, jarak, dua_arah)
        self.simpan_data()

        self.simpan_histori_evakuasi(
            f"Tambah Jalur: {asal} -> {tujuan} ({jarak} km)"
        )

        arah = "↔" if dua_arah else "→"

        print(f"  ✅ Jalur {asal} {arah} {tujuan} ({jarak} km) berhasil ditambahkan.")

    def hapus_jalur(self, asal: str, tujuan: str, dua_arah: bool = True):
        """Menghapus jalur antara dua lokasi."""
        self.graph.hapus_jalur(asal.strip(), tujuan.strip(), dua_arah)
        self.simpan_data()
        print(f"  ✅ Jalur '{asal}' — '{tujuan}' berhasil dihapus.")

    def hapus_lokasi(self, nama_lokasi: str):
        """Menghapus lokasi dan semua jalur yang terhubung."""
        nama_lokasi = nama_lokasi.strip()
        if nama_lokasi not in self.graph.vertices:
            print(f"  [!] Lokasi '{nama_lokasi}' tidak ditemukan.")
            return
        self.graph.hapus_lokasi(nama_lokasi)
        self.simpan_data()
        print(f"  ✅ Lokasi '{nama_lokasi}' beserta jalurnya berhasil dihapus.")

    # ──────────────────────────────────────────────
    # 4.2 Tampilkan Peta Wilayah
    # ──────────────────────────────────────────────

    def tampilkan_peta(self):
        """Menampilkan seluruh jaringan jalur evakuasi."""
        self.graph.tampilkan_peta()
        total_lokasi = len(self.graph.vertices)
        total_jalur = sum(len(v) for v in self.graph.adjacency_list.values()) // 2
        print(f"  📊 Total Lokasi: {total_lokasi} | Total Jalur: {total_jalur}")

    # ──────────────────────────────────────────────
    # 4.3 Cari Jalur Tercepat
    # ──────────────────────────────────────────────

    def cari_jalur_tercepat(self, asal: str, tujuan: str):
        """
        Mencari jalur evakuasi tercepat (jarak terpendek) menggunakan
        algoritma Dijkstra.
        """
        asal   = asal.strip()
        tujuan = tujuan.strip()

        print(f"\n  🔍 Mencari jalur tercepat: {asal} → {tujuan}")
        print(f"  {'─'*45}")

        jarak, rute = self.graph.dijkstra(asal, tujuan)

        if not rute:
            print(f"  ❌ Tidak ada jalur yang menghubungkan '{asal}' dan '{tujuan}'.")
            return None, None

        print(f"  ✅ Jalur ditemukan!")
        print(f"  📍 Rute  : {' → '.join(rute)}")
        print(f"  📏 Jarak : {jarak:.1f} km")
        print(f"  🚏 Titik singgah: {len(rute) - 2} lokasi perantara")
        return jarak, rute

    def cari_jalur_bfs(self, asal: str, tujuan: str):
        """
        Mencari jalur dengan jumlah titik singgah paling sedikit
        menggunakan BFS.
        """
        asal   = asal.strip()
        tujuan = tujuan.strip()

        print(f"\n  🔍 BFS — Jalur paling sedikit titik singgah: {asal} → {tujuan}")
        rute = self.graph.bfs(asal, tujuan)

        if not rute:
            print(f"  ❌ Tidak ada jalur yang ditemukan.")
            return None

        # Hitung total jarak
        total_jarak = self._hitung_total_jarak(rute)
        print(f"  ✅ Rute  : {' → '.join(rute)}")
        print(f"  📏 Total Jarak : {total_jarak:.1f} km")
        return rute

    def cari_jalur_dfs(self, asal: str, tujuan: str):
        """Penelusuran jalur menggunakan DFS."""
        asal   = asal.strip()
        tujuan = tujuan.strip()

        print(f"\n  🔍 DFS — Penelusuran jalur: {asal} → {tujuan}")
        rute = self.graph.dfs(asal, tujuan)

        if not rute:
            print(f"  ❌ Tidak ada jalur yang ditemukan.")
            return None

        total_jarak = self._hitung_total_jarak(rute)
        print(f"  ✅ Rute  : {' → '.join(rute)}")
        print(f"  📏 Total Jarak : {total_jarak:.1f} km")
        return rute

    def _hitung_total_jarak(self, rute: list[str]) -> float:
        """Menghitung total jarak dari sebuah rute."""
        total = 0.0
        for i in range(len(rute) - 1):
            for tetangga, jarak in self.graph.adjacency_list.get(rute[i], []):
                if tetangga == rute[i + 1]:
                    total += jarak
                    break
        return total

    # ──────────────────────────────────────────────
    # 4.4 Simulasi Perpindahan Tim
    # ──────────────────────────────────────────────

    def simulasi_perpindahan_tim(self, nama_tim: str, asal: str,
                                 tujuan: str, delay: float = 0.5):
        """
        Mensimulasikan pergerakan tim penyelamat dari satu titik ke titik lain
        menggunakan jalur terpendek (Dijkstra).
        """
        print(f"\n  🚑 SIMULASI PERPINDAHAN TIM: {nama_tim.upper()}")
        print(f"  {'─'*50}")

        jarak, rute = self.graph.dijkstra(asal.strip(), tujuan.strip())

        if not rute:
            print(f"  ❌ Tidak ada jalur yang dapat dilalui tim '{nama_tim}'.")
            return

        print(f"  Tim      : {nama_tim}")
        print(f"  Asal     : {asal}")
        print(f"  Tujuan   : {tujuan}")
        print(f"  Jarak    : {jarak:.1f} km\n")

        print(f"  🏃 Tim mulai bergerak...")
        for i, titik in enumerate(rute):
            if i == 0:
                print(f"  ✔ [START] {titik}")
            elif i == len(rute) - 1:
                print(f"  ✔ [TIBA ] {titik} 🎯")
            else:
                # Hitung jarak segmen
                jarak_segmen = 0.0
                for tetangga, j in self.graph.adjacency_list.get(rute[i - 1], []):
                    if tetangga == titik:
                        jarak_segmen = j
                        break
                print(f"  ↓  [{i:>2}] {titik}  (+{jarak_segmen:.1f} km)")
            time.sleep(delay)
        self.simpan_histori_evakuasi(f"Tim {nama_tim} bergerak dari {asal} ke {tujuan}")
        print(f"\n  🏁 Tim '{nama_tim}' berhasil tiba di '{tujuan}'!")

    # ──────────────────────────────────────────────
    # Utilitas
    # ──────────────────────────────────────────────

    def daftar_lokasi(self) -> list[str]:
        """Mengembalikan daftar semua lokasi yang terdaftar."""
        return sorted(self.graph.vertices)

    def cek_konektivitas(self, lokasi_a: str, lokasi_b: str) -> bool:
        """Mengecek apakah dua lokasi terhubung (ada jalur)."""
        _, rute = self.graph.dijkstra(lokasi_a.strip(), lokasi_b.strip())
        return len(rute) > 0

    # ──────────────────────────────────────────────
    # HISTORI EVAKUASI
    # ──────────────────────────────────────────────

    def simpan_histori_evakuasi(self, aktivitas):
        """
        Menyimpan histori aktivitas evakuasi ke file txt.
        """
        os.makedirs("data", exist_ok=True)

        with open("data/histori_evakuasi.txt", "a", encoding="utf-8") as file:
            file.write(f"{aktivitas}\n")


    def tampilkan_histori_evakuasi(self):
        """
        Menampilkan histori evakuasi.
        """
        try:

            with open("data/histori_evakuasi.txt", "r", encoding="utf-8") as file:

                isi = file.read()

                if isi.strip() == "":
                    print("  [!] Histori evakuasi kosong.")

                else:
                    print("\n===== HISTORI EVAKUASI =====")
                    print(isi)

        except FileNotFoundError:

            print("  [!] File histori belum ada.")