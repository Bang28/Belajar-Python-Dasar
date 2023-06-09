import datetime
import os
import string
import random

# template dictionary mahasiswa
mahasiswa_template = {
    'nama':'nama',
    'nim':'000000000',
    'sks_lulus':0,
    'lahir': datetime.datetime(1111,11,11)
}

data_mahasiswa = {}

while True:
    os.system("cls")
    print(f"{'Selamat Datang':^20}")
    print(f"{'Data Mahasiswa':^20}")
    print("-"*20)

    # kita akan membuat data dictionary mahasiswa dimana kita akan menggunakan key dari mahasiswa_template
    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    # dimana data yang didapan diambil dari inputan user
    mahasiswa['nama'] = input("nama mahasiswa :")
    mahasiswa['nim'] = input("nim mahasiswa :")
    mahasiswa['sks_lulus'] = int(input("SKS lulus :"))
    TAHUN_LAHIR = int(input("tahun lahir (yyyy) :"))
    BULAN_LAHIR = int(input("bulan lahir (1-12) :"))
    TANGGAL_LAHIR = int(input("tanggal lahir (1-31) :"))
    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

    # disini kita akan membuat keynya secara acak dengan range number ada 6, agar setiap data memiliki key yg bebeda
    # key dibuat dengan random dan memilih string dengan kodenya ascii uppercase dengan panjang 6 karakter
    KEY = "".join((random.choice(string.ascii_uppercase) for i in range(6)))
    # kita akan menambahkan data pada data_mahasiswa yang diambil dari data yg diinputkan ke mahasiswa
    data_mahasiswa.update({KEY:mahasiswa})

    print("\n")
    print(f"{'KEY':<7}{'Nama':<17}{'NIM':<9}{'SKS Lulus':<10}{'Lahir':<10}")
    print("-"*60)
    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa

        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks_lulus']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

        print(f"{KEY:<6} {NAMA:<16} {NIM:<9} {SKS:^8} {LAHIR:<10}")
    
    print("\n")
    is_done = input("masih ada lagi? (y/n)")

    if is_done == "n":
        break

print("program selesai")

# fromkeys
