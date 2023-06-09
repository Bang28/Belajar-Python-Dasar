# 1. mode write (pake mode="w")
# dia akan membuat file baru jika tidak ada, lalu akan overwrite/menghapus isinya lalu memasukan isi yang baru

with open("data_1.txt",mode="w",encoding="utf-8") as file:
    file.write("akhirnya bisa lanjut belajar lagi guys")

# 2. mode append (pake mode="a")
# dgn append, data yg diinputkan akan terus bertambah tidak tertimpa sperti write
with open("data_2.txt",mode="w",encoding="utf-8") as file:
    file.write("setelah kena 1 masalah yang sepele \n")

with open("data_2.txt",mode="a",encoding="utf-8") as file:
    file.write("tapi bikin lier, sampe uninstall python berulang-ulang")

# 3. mode r+
# dia akan menimpa isi teks sesuai panjang data 
with open("data_3.txt",mode="w",encoding="utf-8") as file:
    file.write("baris 1")
with open("data_3.txt",mode="r+",encoding="utf-8") as file:
    file.write("baris 2")
    data = file.read()
    print(data)


