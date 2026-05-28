"""
services/posko_service.py
=========================
Mengelola seluruh operasi terkait Struktur Posko Bencana.
Menggunakan Tree (structures/tree.py) dan Model Posko (models/posko.py).
"""

from models.posko import Posko
from structures.tree import Tree, TreeNode
from algorithms.recursion import (
    preorder_rekursif, postorder_rekursif,
    level_order_rekursif, hitung_kedalaman,
    hitung_total_node, cetak_jalur_ke_root
)
import json
import os

DATA_FILE = "data/posko.json"


class PoskoService:
    def __init__(self):
        self.tree = Tree()
        # Simpan detail Posko terpisah dari tree (tree hanya simpan id/nama/lokasi/kapasitas)
        self.data_posko: dict[str, Posko] = {}
        self.muat_data()

    # ──────────────────────────────────────────────
    # File Handler
    # ──────────────────────────────────────────────

    def simpan_data(self):
        """Menyimpan data tree dan detail posko ke file JSON."""
        os.makedirs("data", exist_ok=True)
        payload = {
            "tree": self.tree.to_dict(),
            "detail": {pid: p.to_dict() for pid, p in self.data_posko.items()}
        }
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)

    def muat_data(self):
        """Memuat data posko dari file JSON jika tersedia."""
        if not os.path.exists(DATA_FILE):
            return
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                payload = json.load(f)
            self.tree.from_dict(payload.get("tree", {"nodes": []}))
            for pid, pdata in payload.get("detail", {}).items():
                self.data_posko[pid] = Posko.from_dict(pdata)
        except (json.JSONDecodeError, KeyError):
            print("  [!] Gagal memuat data posko. Memulai dengan data kosong.")

    # ──────────────────────────────────────────────
    # 6.1 Tambah Posko Utama & Cabang
    # ──────────────────────────────────────────────

    def tambah_posko_utama(self, id_posko: str, nama: str,
                           lokasi: str, kapasitas: int) -> bool:
        """Menambahkan posko utama (root dari tree)."""
        berhasil = self.tree.tambah_posko_utama(id_posko, nama, lokasi, kapasitas)
        if berhasil:
            self.data_posko[id_posko.upper()] = Posko(id_posko, nama, lokasi, kapasitas)
            self.simpan_data()
            print(f"  ✅ Posko utama '{nama}' berhasil ditambahkan.")
        return berhasil

    def tambah_posko_cabang(self, id_posko: str, nama: str,
                            lokasi: str, kapasitas: int, id_induk: str) -> bool:
        """Menambahkan posko cabang di bawah posko tertentu."""
        berhasil = self.tree.tambah_cabang(id_posko, nama, lokasi, kapasitas, id_induk)
        if berhasil:
            self.data_posko[id_posko.upper()] = Posko(id_posko, nama, lokasi, kapasitas)
            self.simpan_data()
            print(f"  ✅ Posko cabang '{nama}' berhasil ditambahkan di bawah '{id_induk}'.")
        return berhasil

    def hapus_posko(self, id_posko: str) -> bool:
        """Menghapus posko dan seluruh cabangnya."""
        # Kumpulkan semua id yang akan dihapus
        node = self.tree.cari_posko(id_posko)
        if node is None:
            print(f"  [!] Posko '{id_posko}' tidak ditemukan.")
            return False
        ids_akan_dihapus = [n.id_posko for n in self._ambil_semua_keturunan(node)]
        ids_akan_dihapus.append(id_posko.upper())

        berhasil = self.tree.hapus_posko(id_posko)
        if berhasil:
            for pid in ids_akan_dihapus:
                self.data_posko.pop(pid, None)
            self.simpan_data()
            print(f"  ✅ Posko '{id_posko}' dan cabangnya berhasil dihapus.")
        return berhasil

    def _ambil_semua_keturunan(self, node: TreeNode) -> list[TreeNode]:
        hasil = []
        for child in node.children:
            hasil.append(child)
            hasil.extend(self._ambil_semua_keturunan(child))
        return hasil

    # ──────────────────────────────────────────────
    # 6.2 Tampilkan Struktur Posko
    # ──────────────────────────────────────────────

    def tampilkan_struktur(self):
        """Menampilkan hierarki posko dalam bentuk tree visual."""
        self.tree.tampilkan_struktur()

    def tampilkan_semua_posko(self):
        """Menampilkan daftar lengkap semua posko beserta detailnya."""
        if not self.data_posko:
            print("  [!] Belum ada data posko.")
            return
        print(f"\n{'─'*55}")
        print(f"  {'DAFTAR SELURUH POSKO':^51}")
        print(f"{'─'*55}")
        for posko in self.data_posko.values():
            posko.tampilkan()
            print()

    def info_posko(self, id_posko: str):
        """Menampilkan detail satu posko."""
        posko = self.data_posko.get(id_posko.upper())
        if posko:
            posko.tampilkan()
        else:
            print(f"  [!] Posko '{id_posko}' tidak ditemukan.")

    # ──────────────────────────────────────────────
    # 6.3 Traversal Posko (Rekursif)
    # ──────────────────────────────────────────────

    def traversal_preorder(self):
        """Menelusuri posko dengan urutan preorder (rekursif)."""
        print(f"\n  📋 TRAVERSAL PREORDER (Posko Utama → Cabang)")
        print(f"  {'─'*45}")
        hasil = []
        preorder_rekursif(self.tree.root, hasil)
        if not hasil:
            print("  [!] Struktur posko kosong.")
            return
        for i, node in enumerate(hasil, 1):
            indent = "    " * node.level
            print(f"  {i:>2}. {indent}[{node.id_posko}] {node.nama} — {node.lokasi}")

    def traversal_postorder(self):
        """Menelusuri posko dengan urutan postorder (rekursif)."""
        print(f"\n  📋 TRAVERSAL POSTORDER (Cabang → Posko Utama)")
        print(f"  {'─'*45}")
        hasil = []
        postorder_rekursif(self.tree.root, hasil)
        if not hasil:
            print("  [!] Struktur posko kosong.")
            return
        for i, node in enumerate(hasil, 1):
            indent = "    " * node.level
            print(f"  {i:>2}. {indent}[{node.id_posko}] {node.nama} — {node.lokasi}")

    def traversal_per_level(self):
        """Menelusuri posko per level (level-order / BFS, rekursif)."""
        print(f"\n  📋 TRAVERSAL PER LEVEL")
        print(f"  {'─'*45}")
        levels = level_order_rekursif(self.tree.root)
        if not levels:
            print("  [!] Struktur posko kosong.")
            return
        for lvl, nodes in enumerate(levels):
            label = "Posko Utama" if lvl == 0 else f"Cabang Level {lvl}"
            print(f"\n  🔹 {label}:")
            for node in nodes:
                print(f"      [{node.id_posko}] {node.nama} — {node.lokasi}")

    def jalur_ke_root(self, id_posko: str):
        """Menampilkan jalur dari posko tertentu ke posko utama."""
        node = self.tree.cari_posko(id_posko)
        if node is None:
            print(f"  [!] Posko '{id_posko}' tidak ditemukan.")
            return
        jalur = cetak_jalur_ke_root(node)
        print(f"  🗺️  Jalur komando: {' → '.join(jalur)}")

    # ──────────────────────────────────────────────
    # Statistik
    # ──────────────────────────────────────────────

    def statistik(self):
        """Menampilkan statistik ringkas struktur posko."""
        total = hitung_total_node(self.tree.root)
        kedalaman = hitung_kedalaman(self.tree.root)
        total_kapasitas = sum(p.kapasitas for p in self.data_posko.values())
        total_pengungsi = sum(p.jumlah_pengungsi for p in self.data_posko.values())

        print(f"\n  📊 STATISTIK POSKO")
        print(f"  {'─'*35}")
        print(f"  Total Posko      : {total}")
        print(f"  Kedalaman Tree   : {kedalaman}")
        print(f"  Total Kapasitas  : {total_kapasitas} orang")
        print(f"  Total Pengungsi  : {total_pengungsi} orang")
        sisa = total_kapasitas - total_pengungsi
        print(f"  Sisa Kapasitas   : {sisa} orang")

    def update_pengungsi(self, id_posko: str, jumlah: int, mode: str = "tambah") -> bool:
        """
        Memperbarui jumlah pengungsi di posko.
        mode = 'tambah' atau 'kurangi'
        """
        posko = self.data_posko.get(id_posko.upper())
        if posko is None:
            print(f"  [!] Posko '{id_posko}' tidak ditemukan.")
            return False
        if mode == "tambah":
            ok = posko.tambah_pengungsi(jumlah)
        else:
            ok = posko.kurangi_pengungsi(jumlah)
        if ok:
            self.simpan_data()
        else:
            print(f"  [!] Operasi gagal — periksa kapasitas atau jumlah pengungsi.")
        return ok
