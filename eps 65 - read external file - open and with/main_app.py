# # tutorial membaca file eksternal


print(3*"=","membaca file txt",3*"=")
# file = open("F:/Belajar Program/Belajar Python/belajar/eps 65 - read external file - open and with/data.txt",mode="r")
file = open("data.txt",mode="r")
print(f"status read = {file.readable()}")
print(f"status read = {file.writable()}")
print(file.read()) #baca selurus isi file
print(file.readline(),end="") #untuk membaca urut perbaris 1 1 guys,end="" untuk menghilangkan newline/ \n
print(file.readlines()) #membaca semua baris sebagai list

# ketika file sudah diopen, jangan lupa untuk di tutup kemabali
# agar ketika nnti direopen, tidak terjadi error
# tapi cara dibawah ini terbilang ribet
print(f"apakah file sudah di close : {file.closed}")
file.close()
print(f"apakah file sudah di close : {file.closed}")


# #salah satu teknik membuka file dipython agar tidak ribet
# ketika file sudah dibuka, maka dia auto close guys
print(3*"=","membaca file txt dgn with",3*"=")
with open("data.txt",mode="r") as file:
    content = file.readline()
    print(content,end="")

print(f"apakah file sudah di close : {file.closed}")
