import datetime
import os
# template dictionary mahasiswa
mahasiswa_template = {
    'nama':'nama',
    'nim':'000000000',
    'sks_lulus':0,
    'lahir': datetime.datetime(1111,11,11)
}

data_mahasiswa = {}

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

print(mahasiswa)


# fromkeys
