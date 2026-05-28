from services.korban_service import (
    tambahkorban,
    tampil,
    cari
)
from menu.evakuasi_menu import menuEvakuasi
from menu.posko_menu import menuPosko

def menuPetugas():

    while True:

        print("\n==== MENU PETUGAS ====")
        print("1. TAMBAH KORBAN")
        print("2. TAMPIL KORBAN")
        print("3. CARI KORBAN")
        print("4. MENU EVAKUASI")
        print("5. MENU POSKO")

        pilihmenu = input("PILIH MENU: ")

        if pilihmenu == "1":
            tambahkorban()

        elif pilihmenu == "2":
            tampil()

        elif pilihmenu == "3":
            cari()

        elif pilihmenu == "4":
           menuEvakuasi()

        elif pilihmenu == "5":
            menuPosko()
        elif pilihmenu == "6":
            break