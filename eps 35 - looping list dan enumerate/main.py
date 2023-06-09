# looping dari list

# 1. for loop
print("\nfor loop")
kumpulan_angka = [4,3,2,5,6,7,1]

for angka in kumpulan_angka:
    print(f"ini adalah angka = {angka}")

peserta = ["ucop", "mail","ali", "baba"]
for nama in peserta:
    print(f"nama = {nama}")

# 2. for loop and range
print("\nfor loop dan range")
kumpulan_angka = [10,5,4,2,6,5]
Panjang = len(kumpulan_angka)

for i in range(Panjang):
    print(f"angka = {kumpulan_angka[i]}")

# 3. while loop
print("\nwhile loop")
kumpulan_angka = [10,5,4,2,6,5]
Panjang = len(kumpulan_angka)

i = 0
while i < Panjang:
    print(f"angka = {kumpulan_angka[i]}")
    i += 1
     
# 4. list comprehension (perulangan paling simpel)
print("\nlist comprehension")
data = ["ucok", 1,2,3,"baba"]
[print(f"data = {i}") for i in data] 
angka = [10,5,4,2,6,5]
angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)
    

# 5. enumerate (index data akan ikut ditampilkan)
print("\n\nenumerate")
data_list = ["ucok", 1,2,3,"baba"]

for index,data in enumerate(data_list):
    print(f"index = {index}, data = {data}")






