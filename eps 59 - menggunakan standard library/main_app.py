import datetime 

data_waktu = datetime.datetime.now()
print(f"datetime now : {data_waktu}")
print(f"tahun : {data_waktu.year}") #untuk ngambil tahunnya saja
print(f"datetime now : {data_waktu.strftime('%A')}") #untuk ngamil harinya aja

# library untuk menjumlahkan sebuah data
from collections import Counter

data = ["a","s","a","x","s","x","c","a"]

# ini program mencari jumlah banyaknya karakter a yg muncul pada variable data dengan for
count = 0
for i in data:
    if i == "a":
        count += 1

print(count)

# ini program untuk mencari jumlah masing-maisng karakter pada variable data dengan Counter
# lebih simple guys...
data_count = Counter(data)
print(f"ini adalah data count = {data_count}")
# contoh jika ingin mencari jumlah untuk satu karakter doang nih
print(f"a pada data muncul sebanyak = {data_count['a']}")


# library untuk membaca text/file
import io #input/output file

file = io.open("baca.txt","r")
print(file.read())