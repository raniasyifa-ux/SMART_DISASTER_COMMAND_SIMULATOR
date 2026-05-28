from services.posko_service import PoskoService
from utils.validator import validate_number

posko = PoskoService()


def menuPosko():

    while True:

        print("\n========== MENU POSKO ==========")
        print("1. Tambah Posko Utama")
        print("2. Tambah Posko Cabang")
        print("3. Tampilkan Struktur Posko")
        print("4. Tampilkan Semua Posko")
        print("5. Info Posko")
        print("6. Traversal Preorder")
        print("7. Traversal Postorder")
        print("8. Traversal Per Level")
        print("9. Jalur ke Root")
        print("10. Statistik Posko")
        print("11. Update Pengungsi")
        print("12. Hapus Posko")
        print("13. Kembali")

        pilih = input("Pilih menu: ")

        # ====================================
        # TAMBAH POSKO UTAMA
        # ====================================

        if pilih == "1":

            id_posko = input("ID Posko: ")
            nama = input("Nama Posko: ")
            lokasi = input("Lokasi: ")

            kapasitas = input("Kapasitas: ")

            if not validate_number(kapasitas):

                print("Kapasitas harus angka!")
                continue

            kapasitas = int(kapasitas)

            posko.tambah_posko_utama(
                id_posko,
                nama,
                lokasi,
                kapasitas
            )

        # ====================================
        # TAMBAH POSKO CABANG
        # ====================================

        elif pilih == "2":

            id_posko = input("ID Posko: ")
            nama = input("Nama Posko: ")
            lokasi = input("Lokasi: ")

            # Diubah → sebelumnya langsung int(input()
            kapasitas = input("Kapasitas: ")

            # Diubah menjadi validasi angka agar dicek validator terlebih dahulu
            if not validate_number(kapasitas):

                print("Kapasitas harus angka!")
                continue

            kapasitas = int(kapasitas)

            id_induk = input("ID Posko Induk: ")

            posko.tambah_posko_cabang(
                id_posko,
                nama,
                lokasi,
                kapasitas,
                id_induk
            )

        # ====================================
        # TAMPIL STRUKTUR TREE
        # ====================================

        elif pilih == "3":

            posko.tampilkan_struktur()

        # ====================================
        # TAMPIL SEMUA POSKO
        # ====================================

        elif pilih == "4":

            posko.tampilkan_semua_posko()

        # ====================================
        # INFO POSKO
        # ====================================

        elif pilih == "5":

            id_posko = input("Masukkan ID Posko: ")

            posko.info_posko(id_posko)

        # ====================================
        # PREORDER
        # ====================================

        elif pilih == "6":

            posko.traversal_preorder()

        # ====================================
        # POSTORDER
        # ====================================

        elif pilih == "7":

            posko.traversal_postorder()

        # ====================================
        # LEVEL ORDER
        # ====================================

        elif pilih == "8":

            posko.traversal_per_level()

        # ====================================
        # JALUR KE ROOT
        # ====================================

        elif pilih == "9":

            id_posko = input("Masukkan ID Posko: ")

            posko.jalur_ke_root(id_posko)

        # ====================================
        # STATISTIK
        # ====================================

        elif pilih == "10":

            posko.statistik()

        # ====================================
        # UPDATE PENGUNGSI
        # ====================================

        elif pilih == "11":

            id_posko = input("ID Posko: ")

            # Diubah  sebelumnya langsung int(input())
            jumlah = input("Jumlah Pengungsi: ")

           # Diubah menjadi validasi angka agar dicek validator terlebih dahulu
            if not validate_number(jumlah):

                print("Jumlah harus angka!")
                continue

            jumlah = int(jumlah)

            mode = input("Mode (tambah/kurangi): ")

            posko.update_pengungsi(
                id_posko,
                jumlah,
                mode
            )

        # ====================================
        # HAPUS POSKO
        # ====================================

        elif pilih == "12":

            id_posko = input("ID Posko: ")

            posko.hapus_posko(id_posko)

        # ====================================
        # KEMBALI
        # ====================================

        elif pilih == "13":

            break

        else:

            print("Menu tidak tersedia!")


