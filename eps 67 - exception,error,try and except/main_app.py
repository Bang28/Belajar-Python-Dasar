# error runtime -> error yang terjadi pada saat running program tapi bukan karna syntax/codinganya
# syntac error -> error yg terjadi karna syntac yg tidak selesai
# exception akan terjadi saat program mengalami error saat runtime  

# from math import nan
# ## contoh sederhana untuk menangkap exception
# input_user = int(input("masukan angka :"))
# hasil = nan #sama aja dgn 0

# try: 
#     hasil = 10/input_user
# except:
#     print("input tidak boleh 0")

# print(f"hasil = {hasil}")

# contoh try & except di aplikasi 
while True:
    angka = int(input("masukan angka pembagi :"))
    try:
        hasil = 10/angka
        print(f"hasil = {hasil}")
        is_done = input("lanjut? (y/n)")
        if is_done == "n":
            break

    except:
        print("pembagi tidak boleh 0")

print("akhir program 1")

# contoh aplikasi untuk membuat file data.txt
try:
    with open("data.txt",mode="r") as file:
        print(file.read())
except:
    print("file data.txt tidak ditemukan, membuat file baru")
    with open("data.txt",mode="w",encoding="utf-8") as file:
        file.write("ini file baru")
    

print("akhir program 2")




