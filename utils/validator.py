# ====================================
# VALIDATOR PROJECT SDCS
# ====================================

def validate_string(value):  # validasi string

    try:

        # cek apakah string tidak kosong
        return len(value.strip()) > 0

    except:

        return False


def validate_number(value):  # validasi angka

    try:

        # ubah ke integer
        value = int(value)

        # angka harus lebih dari 0
        return value > 0

    except:

        return False


def validate_dict(data):  # validasi dictionary

    try:

        # cek apakah tipe dictionary
        return type(data) == dict

    except:

        return False


def validate_not_empty(data):  # validasi tidak kosong

    try:

        # cek data tidak kosong
        return data is not None and data != ""

    except:

        return False