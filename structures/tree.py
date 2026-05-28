class TreeNode:
    """
    Node tunggal dalam struktur Tree Posko.
    Setiap node merepresentasikan satu posko (utama / cabang).
    """

    def __init__(self, id_posko: str, nama: str, lokasi: str,
                 kapasitas: int = 0, level: int = 0):
        self.id_posko  = id_posko
        self.nama      = nama
        self.lokasi    = lokasi
        self.kapasitas = kapasitas
        self.level     = level          # 0 = root, 1 = cabang, dst.
        self.children: list['TreeNode'] = []
        self.parent: 'TreeNode | None'  = None

    def tambah_anak(self, node: 'TreeNode'):
        node.parent = self
        node.level  = self.level + 1
        self.children.append(node)

    def hapus_anak(self, id_posko: str) -> bool:
        for i, child in enumerate(self.children):
            if child.id_posko == id_posko:
                self.children.pop(i)
                return True
        return False

    def __repr__(self):
        return f"TreeNode({self.id_posko}, {self.nama})"


class Tree:
    """
    N-ary Tree untuk merepresentasikan hierarki Posko Bencana.
    Satu root (posko utama) bisa memiliki banyak cabang bertingkat.
    """

    def __init__(self):
        self.root: TreeNode | None = None
        self._index: dict[str, TreeNode] = {}   # id_posko → node (akses O(1))

    # ──────────────────────────────────────────────
    # CRUD
    # ──────────────────────────────────────────────

    def tambah_posko_utama(self, id_posko: str, nama: str,
                           lokasi: str, kapasitas: int = 0) -> bool:
        """Menambahkan posko utama (root). Hanya boleh ada satu root."""
        if self.root is not None:
            print("  [!] Posko utama sudah ada. Tidak bisa menambah root baru.")
            return False
        node = TreeNode(id_posko, nama, lokasi, kapasitas, level=0)
        self.root = node
        self._index[id_posko] = node
        return True

    def tambah_cabang(self, id_posko: str, nama: str, lokasi: str,
                      kapasitas: int, id_induk: str) -> bool:
        """
        Menambahkan posko cabang di bawah posko dengan id_induk.
        """
        if id_posko in self._index:
            print(f"  [!] ID '{id_posko}' sudah digunakan.")
            return False
        induk = self._index.get(id_induk)
        if induk is None:
            print(f"  [!] Posko induk '{id_induk}' tidak ditemukan.")
            return False
        node = TreeNode(id_posko, nama, lokasi, kapasitas)
        induk.tambah_anak(node)
        self._index[id_posko] = node
        return True

    def hapus_posko(self, id_posko: str) -> bool:
        """
        Menghapus posko beserta seluruh cabangnya secara rekursif.
        Tidak bisa menghapus root.
        """
        if id_posko == (self.root.id_posko if self.root else None):
            print("  [!] Tidak bisa menghapus posko utama.")
            return False
        node = self._index.get(id_posko)
        if node is None:
            return False
        # hapus semua keturunan dari index
        self._hapus_dari_index(node)
        # lepas dari induk
        if node.parent:
            node.parent.hapus_anak(id_posko)
        return True

    def _hapus_dari_index(self, node: TreeNode):
        """Rekursif: hapus node dan seluruh keturunannya dari _index."""
        self._index.pop(node.id_posko, None)
        for child in node.children:
            self._hapus_dari_index(child)

    def cari_posko(self, id_posko: str) -> TreeNode | None:
        return self._index.get(id_posko)

    # ──────────────────────────────────────────────
    # Traversal (menggunakan rekursion.py lewat callback)
    # ──────────────────────────────────────────────

    def tampilkan_struktur(self):
        """Menampilkan hierarki posko dalam bentuk pohon visual."""
        if self.root is None:
            print("  [!] Struktur posko masih kosong.")
            return
        print(f"\n{'─'*55}")
        print(f"  {'STRUKTUR HIERARKI POSKO BENCANA':^51}")
        print(f"{'─'*55}")
        self._cetak_node(self.root, prefix="", is_last=True)
        print(f"{'─'*55}")

    def _cetak_node(self, node: TreeNode, prefix: str, is_last: bool):
        """Rekursif: mencetak satu node dan cabang-cabangnya."""
        connector = "└── " if is_last else "├── "
        ikon = "🏠" if node.level == 0 else ("🏢" if node.level == 1 else "🏕️")
        print(f"  {prefix}{connector}{ikon} [{node.id_posko}] {node.nama}")
        print(f"  {prefix}{'    ' if is_last else '│   '}    📌 {node.lokasi} | Kapasitas: {node.kapasitas}")

        child_prefix = prefix + ("    " if is_last else "│   ")
        for i, child in enumerate(node.children):
            self._cetak_node(child, child_prefix, i == len(node.children) - 1)

    def preorder(self) -> list[TreeNode]:
        """Preorder traversal: root → anak kiri → anak kanan (rekursif)."""
        hasil = []
        self._preorder_rekursif(self.root, hasil)
        return hasil

    def _preorder_rekursif(self, node: TreeNode | None, hasil: list):
        if node is None:
            return
        hasil.append(node)
        for child in node.children:
            self._preorder_rekursif(child, hasil)

    def postorder(self) -> list[TreeNode]:
        """Postorder traversal: anak → root (rekursif)."""
        hasil = []
        self._postorder_rekursif(self.root, hasil)
        return hasil

    def _postorder_rekursif(self, node: TreeNode | None, hasil: list):
        if node is None:
            return
        for child in node.children:
            self._postorder_rekursif(child, hasil)
        hasil.append(node)

    def hitung_total_posko(self) -> int:
        return len(self._index)

    def hitung_total_kapasitas(self) -> int:
        return sum(n.kapasitas for n in self._index.values())

    # ──────────────────────────────────────────────
    # Serialisasi
    # ──────────────────────────────────────────────

    def to_dict(self):
        """Mengubah seluruh tree ke dictionary untuk disimpan ke JSON."""
        if self.root is None:
            return {"nodes": []}
        nodes = []
        for node in self.preorder():
            nodes.append({
                "id_posko":  node.id_posko,
                "nama":      node.nama,
                "lokasi":    node.lokasi,
                "kapasitas": node.kapasitas,
                "id_induk":  node.parent.id_posko if node.parent else None
            })
        return {"nodes": nodes}

    def from_dict(self, data: dict):
        """Memuat tree dari dictionary (hasil baca JSON)."""
        self.root = None
        self._index = {}
        for item in data.get("nodes", []):
            if item["id_induk"] is None:
                self.tambah_posko_utama(
                    item["id_posko"], item["nama"],
                    item["lokasi"], item["kapasitas"]
                )
            else:
                self.tambah_cabang(
                    item["id_posko"], item["nama"],
                    item["lokasi"], item["kapasitas"],
                    item["id_induk"]
                )
