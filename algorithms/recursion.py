
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from structures.tree import TreeNode


# ──────────────────────────────────────────────────────────────
# Traversal Rekursif untuk Tree Posko
# ──────────────────────────────────────────────────────────────

def preorder_rekursif(node: 'TreeNode | None', hasil: list) -> None:
    """
    Preorder DFS: kunjungi node saat ini dulu,
    kemudian setiap anak secara rekursif.
    """
    if node is None:
        return
    hasil.append(node)
    for child in node.children:
        preorder_rekursif(child, hasil)


def postorder_rekursif(node: 'TreeNode | None', hasil: list) -> None:
    """
    Postorder DFS: kunjungi semua anak terlebih dahulu,
    baru node saat ini.
    """
    if node is None:
        return
    for child in node.children:
        postorder_rekursif(child, hasil)
    hasil.append(node)


def level_order_rekursif(root: 'TreeNode | None') -> list[list['TreeNode']]:
    """
    Level-order (BFS) menggunakan rekursif dengan helper.
    Mengembalikan list of list, setiap sublist = satu level.
    """
    levels: list[list] = []
    _kumpulkan_level(root, 0, levels)
    return levels


def _kumpulkan_level(node: 'TreeNode | None', level: int,
                     levels: list[list]) -> None:
    """Helper rekursif untuk level_order_rekursif."""
    if node is None:
        return
    if level == len(levels):
        levels.append([])
    levels[level].append(node)
    for child in node.children:
        _kumpulkan_level(child, level + 1, levels)


def cari_node_rekursif(node: 'TreeNode | None',
                       id_posko: str) -> 'TreeNode | None':
    """Mencari node dengan id_posko tertentu secara rekursif (DFS)."""
    if node is None:
        return None
    if node.id_posko == id_posko:
        return node
    for child in node.children:
        hasil = cari_node_rekursif(child, id_posko)
        if hasil:
            return hasil
    return None


def hitung_kedalaman(node: 'TreeNode | None') -> int:
    """
    Menghitung kedalaman (height) tree dari node tertentu secara rekursif.
    Node tanpa anak → kedalaman 0.
    """
    if node is None or not node.children:
        return 0
    return 1 + max(hitung_kedalaman(child) for child in node.children)


def hitung_total_node(node: 'TreeNode | None') -> int:
    """Menghitung total node dalam subtree secara rekursif."""
    if node is None:
        return 0
    return 1 + sum(hitung_total_node(child) for child in node.children)


def cetak_jalur_ke_root(node: 'TreeNode | None') -> list[str]:
    """
    Mengembalikan jalur dari node ke root dalam bentuk list id_posko.
    Menggunakan rekursif pada pointer parent.
    """
    if node is None:
        return []
    if node.parent is None:
        return [node.id_posko]
    return cetak_jalur_ke_root(node.parent) + [node.id_posko]


# ──────────────────────────────────────────────────────────────
# Fungsi Rekursif Umum (dipakai modul lain)
# ──────────────────────────────────────────────────────────────

def fibonacci(n: int) -> int:
    """Fibonacci rekursif — digunakan untuk keperluan pengujian / demo."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def faktorial(n: int) -> int:
    """Faktorial rekursif."""
    if n == 0:
        return 1
    return n * faktorial(n - 1)


def flatten_rekursif(nested: list) -> list:
    """
    Meratakan nested list secara rekursif.
    Berguna untuk mengumpulkan data dari struktur bertingkat.
    """
    hasil = []
    for item in nested:
        if isinstance(item, list):
            hasil.extend(flatten_rekursif(item))
        else:
            hasil.append(item)
    return hasil
