from services.korban_service import (
    tampil,
    cari
)
from menu.posko_menu import menuPosko

def menuRelawan():

    while True:

        print("\n==== MENU RELAWAN ====")
        print("1. TAMPIL KORBAN")
        print("2. CARI KORBAN")
        print("3. MENU POSKO")
        print("4. LOGOUT")

        pilihmenu = input("PILIH MENU: ")

        if pilihmenu == "1":
            tampil()

        elif pilihmenu == "2":
            cari()

        elif pilihmenu == "3":

            menuPosko()

        elif pilihmenu == "4":

            print("LOGOUT BERHASIL")

            break