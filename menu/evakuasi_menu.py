from services.evakuasi_service import EvakuasiService
from utils.validator import validate_string

evakuasi = EvakuasiService()


def menuEvakuasi():

    while True:

        print("\n========== MENU EVAKUASI ==========")
        print("1. Tambah Lokasi")
        print("2. Tambah Jalur")
        print("3. Tampilkan Peta")
        print("4. Cari Jalur Tercepat (Dijkstra)")
        print("5. Cari Jalur BFS")
        print("6. Cari Jalur DFS")
        print("7. Simulasi Perpindahan Tim")
        print("8. Hapus Jalur")
        print("9. Hapus Lokasi")
        print("10. Histori Evakuasi")
        print("11. Kembali")

        pilih = input("Pilih menu: ")

        # ==============================
        # TAMBAH LOKASI
        # ==============================

        if pilih == "1":

            lokasi = input("Masukkan nama lokasi: ")

            # PERBAIKAN:
            # validasi string agar input tidak kosong
            if not validate_string(lokasi):

                print("Nama lokasi tidak valid!")
                continue

            evakuasi.tambah_lokasi(lokasi)

        # ==============================
        # TAMBAH JALUR
        # ==============================

        elif pilih == "2":

            asal = input("Lokasi asal: ")
            tujuan = input("Lokasi tujuan: ")

            # PERBAIKAN:
            # validasi input string
            if not validate_string(asal) or not validate_string(tujuan):

                print("Lokasi tidak valid!")
                continue

            try:

                jarak = float(input("Jarak (km): "))

                # PERBAIKAN:
                # validasi jarak harus lebih dari 0
                if jarak <= 0:

                    print("Jarak harus lebih dari 0!")
                    continue

                evakuasi.tambah_jalur(
                    asal,
                    tujuan,
                    jarak
                )

            except ValueError:

                # PERBAIKAN:
                # menangani input selain angka
                print("Jarak harus angka!")

        # ==============================
        # TAMPIL PETA
        # ==============================

        elif pilih == "3":

            evakuasi.tampilkan_peta()

        # ==============================
        # DIJKSTRA
        # ==============================

        elif pilih == "4":

            asal = input("Lokasi asal: ")
            tujuan = input("Lokasi tujuan: ")

            # PERBAIKAN:
            # validasi input lokasi
            if not validate_string(asal) or not validate_string(tujuan):

                print("Lokasi tidak valid!")
                continue

            evakuasi.cari_jalur_tercepat(
                asal,
                tujuan
            )

        # ==============================
        # BFS
        # ==============================

        elif pilih == "5":

            asal = input("Lokasi asal: ")
            tujuan = input("Lokasi tujuan: ")

            # PERBAIKAN:
            # validasi input lokasi
            if not validate_string(asal) or not validate_string(tujuan):

                print("Lokasi tidak valid!")
                continue

            evakuasi.cari_jalur_bfs(
                asal,
                tujuan
            )

        # ==============================
        # DFS
        # ==============================

        elif pilih == "6":

            asal = input("Lokasi asal: ")
            tujuan = input("Lokasi tujuan: ")

            # PERBAIKAN:
            # validasi input lokasi
            if not validate_string(asal) or not validate_string(tujuan):

                print("Lokasi tidak valid!")
                continue

            evakuasi.cari_jalur_dfs(
                asal,
                tujuan
            )

        # ==============================
        # SIMULASI TIM
        # ==============================

        elif pilih == "7":

            nama_tim = input("Nama Tim: ")
            asal = input("Lokasi asal: ")
            tujuan = input("Lokasi tujuan: ")

            # PERBAIKAN:
            # validasi semua input string
            if (
                not validate_string(nama_tim)
                or not validate_string(asal)
                or not validate_string(tujuan)
            ):

                print("Input tidak valid!")
                continue

            evakuasi.simulasi_perpindahan_tim(
                nama_tim,
                asal,
                tujuan
            )

        # ==============================
        # HAPUS JALUR
        # ==============================

        elif pilih == "8":

            asal = input("Lokasi asal: ")
            tujuan = input("Lokasi tujuan: ")

            # PERBAIKAN:
            # validasi input lokasi
            if not validate_string(asal) or not validate_string(tujuan):

                print("Lokasi tidak valid!")
                continue

            evakuasi.hapus_jalur(
                asal,
                tujuan
            )

        # ==============================
        # HAPUS LOKASI
        # ==============================

        elif pilih == "9":

            lokasi = input("Nama lokasi: ")

            # PERBAIKAN:
            # validasi nama lokasi
            if not validate_string(lokasi):

                print("Nama lokasi tidak valid!")
                continue

            evakuasi.hapus_lokasi(lokasi)

        # ==============================
        # HISTORI EVAKUASI
        # ==============================

        elif pilih == "10":

            evakuasi.tampilkan_histori_evakuasi()

        # ==============================
        # KEMBALI
        # ==============================

        elif pilih == "11":

            break

        # ==============================
        # MENU TIDAK TERSEDIA
        # ==============================

        else:

            # PERBAIKAN:
            # menangani input menu yang salah
            print("Menu tidak tersedia!")

