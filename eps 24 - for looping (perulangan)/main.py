# perulangan (loop)

# for kondisi:
#     aksi

# ini dengan list
angka2_list = [0,1,2,3,4] #ini adalah list
print(angka2_list)

for i in angka2_list: #untuk semua i yang ada didalam angka2_list 
    print(f"i sekarang -> {i}") #maka for akan mengulang-ulang aksi dengan mengambil nilai i yang ada di list
print("akhir program 1\n")

# ini dengan range
angka2_range = range(5) #5 ini jumlah index
for i in angka2_range:
    print(f"i sekarang -> {i}") #maka for akan mengulang-ulang aksi dengan mengambil nilai i yang ada di list
print("akhir program 2\n")

angka2_range = range(1,10) #kita akan mulai indexnya dari index ke 1, dengan jumlah index yaitu 10
for i in angka2_range:
    print(f"i sekarang -> {i}") #maka for akan mengulang-ulang aksi dengan mengambil nilai i yang ada di list
print("akhir program 3\n")

# menggunakan string
data_str = "saya rajin banget"

for huruf in data_str:
    print(huruf)
print("akhir program 4")

