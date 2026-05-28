import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from menu.admin import menuAdmin
from menu.petugas import menuPetugas
from menu.relawan import menuRelawan

from services.auth_service import login, register
from services.korban_service import loadKorban
from services.histori_service import load_histori


def main():
    while True:

        print("\n======================================")
        print(" SISTEM SIMULASI PENANGANAN BENCANA ")
        print("======================================")

        print("1. LOGIN")
        print("2. REGISTER")
        print("3. KELUAR")

        pilih = input("Pilih menu: ")

        # LOGIN
        if pilih == "1":

            user = login()

            if user:

                loadKorban()
                load_histori()

                role = user["role"].upper()

                if role == "ADMIN":
                    menuAdmin()

                elif role == "PETUGAS":
                    menuPetugas()

                elif role == "RELAWAN":
                    menuRelawan()

                else:
                    print("Role tidak dikenali!")

        # REGISTER
        elif pilih == "2":
            register()

        # KELUAR
        elif pilih == "3":
            print("Program selesai.")
            break

        else:
            print("Menu tidak tersedia!")


if __name__ == "__main__":
    main()