from collections import defaultdict, deque
import heapq


class Graph:
    """
    Graf berbobot (weighted graph) menggunakan adjacency list.
    Digunakan untuk merepresentasikan jaringan jalur evakuasi
    antar lokasi/titik kumpul.
    """

    def __init__(self):
        # adjacency list: {lokasi: [(tetangga, bobot), ...]}
        self.adjacency_list = defaultdict(list)
        self.vertices = set()

    # ──────────────────────────────────────────────
    # CRUD Jalur
    # ──────────────────────────────────────────────

    def tambah_lokasi(self, lokasi: str):
        """Menambahkan lokasi/vertex ke dalam graf."""
        self.vertices.add(lokasi)

    def tambah_jalur(self, asal: str, tujuan: str, jarak: float, dua_arah: bool = True):
        """
        Menambahkan jalur (edge) antara dua lokasi.
        Secara default jalur bersifat dua arah (undirected).
        """
        self.vertices.add(asal)
        self.vertices.add(tujuan)
        self.adjacency_list[asal].append((tujuan, jarak))
        if dua_arah:
            self.adjacency_list[tujuan].append((asal, jarak))

    def hapus_jalur(self, asal: str, tujuan: str, dua_arah: bool = True):
        """Menghapus jalur antara dua lokasi."""
        self.adjacency_list[asal] = [
            (t, j) for t, j in self.adjacency_list[asal] if t != tujuan
        ]
        if dua_arah:
            self.adjacency_list[tujuan] = [
                (t, j) for t, j in self.adjacency_list[tujuan] if t != asal
            ]

    def hapus_lokasi(self, lokasi: str):
        """Menghapus lokasi beserta semua jalur yang terhubung."""
        self.vertices.discard(lokasi)
        self.adjacency_list.pop(lokasi, None)
        for tetangga in self.adjacency_list:
            self.adjacency_list[tetangga] = [
                (t, j) for t, j in self.adjacency_list[tetangga] if t != lokasi
            ]

    def tampilkan_peta(self):
        """Menampilkan seluruh hubungan antar lokasi beserta jaraknya."""
        if not self.vertices:
            print("  [!] Peta masih kosong.")
            return

        print(f"\n{'─'*55}")
        print(f"  {'PETA JARINGAN JALUR EVAKUASI':^51}")
        print(f"{'─'*55}")
        lokasi_terurut = sorted(self.vertices)
        for lokasi in lokasi_terurut:
            tetangga = self.adjacency_list.get(lokasi, [])
            if tetangga:
                koneksi = ", ".join(
                    f"{t} ({j:.1f} km)" for t, j in sorted(tetangga)
                )
                print(f"  📍 {lokasi}")
                print(f"      └─→ {koneksi}")
            else:
                print(f"  📍 {lokasi}  (tidak terhubung)")
        print(f"{'─'*55}")

    # ──────────────────────────────────────────────
    # Algoritma Pencarian Jalur
    # ──────────────────────────────────────────────

    def dijkstra(self, asal: str, tujuan: str):
        """
        Mencari jalur terpendek dari asal ke tujuan menggunakan
        algoritma Dijkstra.

        Returns:
            (jarak_total, [daftar_lokasi_rute]) atau (inf, []) jika tidak ada jalur.
        """
        if asal not in self.vertices or tujuan not in self.vertices:
            return float('inf'), []

        # priority queue: (jarak_kumulatif, lokasi, path)
        pq = [(0, asal, [asal])]
        visited = set()

        while pq:
            jarak, lokasi_saat_ini, path = heapq.heappop(pq)

            if lokasi_saat_ini in visited:
                continue
            visited.add(lokasi_saat_ini)

            if lokasi_saat_ini == tujuan:
                return jarak, path

            for tetangga, bobot in self.adjacency_list.get(lokasi_saat_ini, []):
                if tetangga not in visited:
                    heapq.heappush(pq, (jarak + bobot, tetangga, path + [tetangga]))

        return float('inf'), []

    def bfs(self, asal: str, tujuan: str):
        """
        Breadth-First Search — mencari jalur dengan jumlah
        lintasan (hop) paling sedikit.

        Returns:
            [daftar_lokasi_rute] atau [] jika tidak ada jalur.
        """
        if asal not in self.vertices or tujuan not in self.vertices:
            return []

        queue = deque([[asal]])
        visited = {asal}

        while queue:
            path = queue.popleft()
            lokasi_saat_ini = path[-1]

            if lokasi_saat_ini == tujuan:
                return path

            for tetangga, _ in self.adjacency_list.get(lokasi_saat_ini, []):
                if tetangga not in visited:
                    visited.add(tetangga)
                    queue.append(path + [tetangga])

        return []

    def dfs(self, asal: str, tujuan: str):
        """
        Depth-First Search — menelusuri jalur secara mendalam.

        Returns:
            [daftar_lokasi_rute] atau [] jika tidak ada jalur.
        """
        if asal not in self.vertices or tujuan not in self.vertices:
            return []

        stack = [[asal]]
        visited = set()

        while stack:
            path = stack.pop()
            lokasi_saat_ini = path[-1]

            if lokasi_saat_ini == tujuan:
                return path

            if lokasi_saat_ini not in visited:
                visited.add(lokasi_saat_ini)
                for tetangga, _ in self.adjacency_list.get(lokasi_saat_ini, []):
                    if tetangga not in visited:
                        stack.append(path + [tetangga])

        return []

    # ──────────────────────────────────────────────
    # Serialisasi
    # ──────────────────────────────────────────────

    def to_dict(self):
        """Mengubah graf ke bentuk dictionary untuk disimpan ke JSON."""
        edges = []
        dicatat = set()
        for asal, tetangga_list in self.adjacency_list.items():
            for tujuan, jarak in tetangga_list:
                kunci = tuple(sorted([asal, tujuan]))
                if kunci not in dicatat:
                    edges.append({"asal": asal, "tujuan": tujuan, "jarak": jarak})
                    dicatat.add(kunci)
        return {"vertices": list(self.vertices), "edges": edges}

    def from_dict(self, data: dict):
        """Memuat data graf dari dictionary (hasil baca JSON)."""
        self.adjacency_list = defaultdict(list)
        self.vertices = set(data.get("vertices", []))
        for edge in data.get("edges", []):
            self.tambah_jalur(edge["asal"], edge["tujuan"], edge["jarak"])
