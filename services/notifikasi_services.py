from models.notifikasi import Notifikasi
from structures.circular_linked_list import CircularLinkedList

notifikasi = CircularLinkedList()


def tambah_notifikasi(pesan, level="INFO"):

    notif = Notifikasi(pesan, level)

    notifikasi.add(notif)


def tampil_notifikasi():

    data = notifikasi.display()

    if not data:

        print("Tidak ada notifikasi")

    else:

        print("\n===== NOTIFIKASI DARURAT =====")

        for item in data:

            print(f"🔔 {item}")


def notif_berulang():

    print("\n===== NOTIFIKASI BERULANG =====")

    data = notifikasi.display()

    if not data:

        print("Tidak ada notifikasi")

    else:

        for item in data:

            print(f"🔔 {item}")