import json #mengambil library JSON bawaan PYTHON

def load_data(namafile): #membuat fungsi membaca data dari file JSON
    try:
        with open(namafile, "r") as f:
            return json.load(f) #mengubahisi JSON menjadi data python
    except:
        return [] #mengambalikan list kosonh

def save_file(namafile, data): #membuat fungsi menyimpan data
    with open(namafile, "w") as f:
        json.dump(data, f, indent= 4) #menyimpan data python menjadi JSON
