from services.korban_service import (
    tambahkorban,
    tampil,
    cari,
    urut,
    update,
    hapus
)

from services.bantuan_service import BantuanService
from menu.evakuasi_menu import menuEvakuasi
from menu.posko_menu import menuPosko

# import validator
from utils.validator import validate_number, validate_string

bantuan_service = BantuanService()


def menuAdmin():

    while True:

        print("\n==== MENU ADMIN ====")
        print("1. TAMBAH KORBAN")
        print("2. TAMPIL KORBAN")
        print("3. CARI KORBAN")
        print("4. URUTKAN KORBAN")
        print("5. UPDATE KORBAN")
        print("6. HAPUS KORBAN")
        print("7. TAMBAH BANTUAN")
        print("8. PROSES BANTUAN")
        print("9. UNDO BANTUAN")
        print("10. TAMPIL ANTREAN")
        print("11. TAMPIL HISTORI")
        print("12. TAMPIL NOTIFIKASI")
        print("13. MENU EVAKUASI")
        print("14. MENU POSKO")
        print("15. LOGOUT")

        pilihmenu = input("PILIH MENU: ")

        # ====================================
        # MENU KORBAN
        # ====================================

        if pilihmenu == "1":

            tambahkorban()

        elif pilihmenu == "2":

            tampil()

        elif pilihmenu == "3":

            cari()

        elif pilihmenu == "4":

            urut()

        elif pilihmenu == "5":

            update()

        elif pilihmenu == "6":

            hapus()

        # ====================================
        # MENU BANTUAN
        # ====================================

        elif pilihmenu == "7":

            id_bantuan = input("ID Bantuan: ")
            nama = input("Nama Bantuan: ")
            jenis = input("Jenis Bantuan: ")
            jumlah = input("Jumlah: ")
            lokasi = input("Lokasi: ")

            # validasi nama
            if not validate_string(nama):

                print("Nama bantuan tidak boleh kosong!")
                continue

            # validasi jumlah
            if not validate_number(jumlah):

                print("Jumlah harus berupa angka!")
                continue

            jumlah = int(jumlah)

            hasil = bantuan_service.tambah_bantuan(
                id_bantuan,
                nama,
                jenis,
                jumlah,
                lokasi
            )

            print(hasil)

        elif pilihmenu == "8":

            hasil = bantuan_service.proses_bantuan()

            print(hasil)

        elif pilihmenu == "9":

            hasil = bantuan_service.undo()

            print(hasil)

        elif pilihmenu == "10":

            data = bantuan_service.tampilkan_antrian()

            if not data:

                print("Antrean kosong")

            else:

                for item in data:

                    print(item)

        elif pilihmenu == "11":

            print(
                bantuan_service.tampilkan_histori()
            )

        elif pilihmenu == "12":

            print(
                bantuan_service.tampilkan_notifikasi()
            )

        # ====================================
        # MENU EVAKUASI
        # ====================================

        elif pilihmenu == "13":

            menuEvakuasi()

        # ====================================
        # MENU POSKO
        # ====================================

        elif pilihmenu == "14":

            menuPosko()

        # ====================================
        # LOGOUT
        # ====================================

        elif pilihmenu == "15":

            print("LOGOUT BERHASIL")

            break

        # ====================================
        # JIKA MENU TIDAK ADA
        # ====================================

        else:

            print("MENU TIDAK TERSEDIA")



