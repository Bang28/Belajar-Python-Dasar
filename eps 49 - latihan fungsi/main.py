'''latihan fungsi'''

import os

# # program untuk menghitung luas dan keliling persegi panjang

# # pertama membuat header programnya
# os.system("cls") #untuk membersihkan halaman pada terminal
# print(f"{'Program Menghitung Luas':^40}")
# print(f"{'Dan keliling Persegi Panjang':^40}")
# print(f"{'-'*40:^40}")

# # mengambil input user
# PANJANG = int(input("Masukan nilai panjang : "))
# LEBAR = int(input("masukan nilai lebar : "))

# # program menghitung luas & kelilling
# LUAS = PANJANG * LEBAR
# KELILING = 2 * (PANJANG+LEBAR)

# # menampilkan hasil
# print(f"hasil perhitungan luas = {LUAS}")
# print(f"hasil perhitungan keliling = {KELILING}")

def header():
    '''fungsi header'''
    os.system("cls")
    print(f"{'Program Menghitung Luas':^40}")
    print(f"{'Dan keliling Persegi Panjang':^40}")
    print(f"{'-'*40:^40}")

def input_user():
    '''mengambil input user'''
    panjang = int(input("Masukan nilai panjang : "))
    lebar = int(input("masukan nilai lebar : "))

    return panjang, lebar

def hitung_luas(panjang, lebar):
    '''fungsi luas'''
    return panjang * lebar

def hitung_keliling(panjang, lebar):
    '''fungsi keliling'''
    return 2 * (panjang + lebar)

def display(message, value):
    '''fungsi menampilkan'''
    print(f"hasil perhitungan {message} = {value}")

# # program utamanya (sesuai video latihan)
# while True:
#     header()
#     PANJANG,LEBAR = input_user()
    
#     LUAS = hitung_luas(PANJANG, LEBAR)
#     KELILING = hitung_keliling(PANJANG,LEBAR)
#     display("Luas", LUAS)
#     display("Keliling", KELILING)

#     isContunie = input("apakah lanjut? (y/n)")

#     if isContunie == "n":
#         break 

# print("program selesai")

# program utamanya (PR dari latihan)
while True:
    header()
    PANJANG,LEBAR = input_user()

    opsi = input("pilih 1 untuk hitung luas & 2 untuk keliling! (1/2)")

    if opsi == "1":
        LUAS = hitung_luas(PANJANG, LEBAR)
        display("Luas", LUAS)
    else :
        KELILING = hitung_keliling(PANJANG,LEBAR)
        display("Keliling", KELILING)

    isContunie = input("apakah lanjut? (y/n)")

    if isContunie == "n":
        break 

print("program selesai")