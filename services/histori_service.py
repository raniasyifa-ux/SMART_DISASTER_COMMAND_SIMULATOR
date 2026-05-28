from datetime import datetime  # mengambil module datetime untuk waktu otomatis

FILE_PATH = "data/histori.txt"  # lokasi file penyimpanan histori


# =========================================
# MENAMBAHKAN HISTORI
# =========================================

def tambah_histori(aktivitas):

    # mengambil waktu saat ini
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # membuka file histori dalam mode append
    with open(FILE_PATH, "a") as f:

        # menambahkan aktivitas ke file
        f.write(f"[{waktu}] {aktivitas}\n")


# =========================================
# MENAMPILKAN HISTORI
# =========================================

def tampil_histori():

    try:

        # membuka file histori dalam mode read
        with open(FILE_PATH, "r") as f:

            # mengembalikan seluruh isi file
            return f.read()

    except FileNotFoundError:

        # jika file belum ada maka return string kosong
        return ""


# =========================================
# LOAD HISTORI
# =========================================

def load_histori():

    try:

        # membuka file histori
        with open(FILE_PATH, "r") as f:

            # membaca semua baris histori
            return f.readlines()

    except FileNotFoundError:

        # jika file tidak ditemukan
        return []