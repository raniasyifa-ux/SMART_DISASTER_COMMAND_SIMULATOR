from models.user import User
from utils.file_handler import load_data, save_file

FILENYA = "data/users.json"

def register():
    users = load_data(FILENYA)

    username = input("MASUKKAN NAMA: ")
    password = input("MASUKKAN PASSWORD: ")
    role = input("MASUKKAN ROLE ANDA (ADMIN/ PETUGAS / RELAWAN): ")

    #jika username sudah ada
    for user in users:
        if user ["username"] == username:
            print("USERNAME SUDAH DIGUNAKAN")
            return
    
    userBaru = User(username, password, role)

    users.append(userBaru.to_dict())
    save_file(FILENYA, users)

    print("REGISTER BERHASIL, SILAHKAN LOGIN")


def login():
    users = load_data(FILENYA)

    username = input ("MASUKKAN USERNAME ANDA: ")
    password = input("MASUKKAN PASSWORDNYA: ")

    for user in users:
        if user["username"] == username and user["password"] == password:
            print(f"LOGIN BERHASIL, SELAMAT DATANG  {username}")
            return user
        
    print("LOGIN GAGAL, SILAHKAN MENCOBA LAGI")
    return None 