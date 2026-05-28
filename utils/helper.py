# garis pemisah
def garis():
    print("=" * 40)


# judul menu
def judul(teks):

    garis()
    print(teks.center(40))
    garis()


# pause sederhana
def pause():
    input("TEKAN ENTER UNTUK LANJUT...")


# membersihkan terminal sederhana
def clear():
    print("\n" * 50)