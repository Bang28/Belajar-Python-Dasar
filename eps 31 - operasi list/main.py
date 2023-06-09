# operasi list

data_angka = [2,1,3,4,1,12,4,3,5,2,1,41,2]
print(f"data angka = \n{data_angka}")

# count data (untuk menghitung jumlah angka yg sama muncul berapa kali)
jumlah_data_4 = data_angka.count(4) #untuk melihat angka 4 muncul berapa kali
jumlah_data_2 = data_angka.count(2) #untuk melihat angka 2 muncul berapa kali
print(f"jumlah data 4 = {jumlah_data_4}")
print(f"jumlah data 2 = {jumlah_data_2}")

# ambil posisi data (mencari tau index pada data)
data = ["ucup", "otong", "dudung", "asep"]
print(f"data = {data}")

index_dudung = data.index("dudung")
print(f"index si dudung = {index_dudung}")

# mengurutkan list 
print(f"data angka sebelum sort = {data_angka}")
data_angka.sort()
print(f"data angka sort = {data_angka}")

print(f"data = {data}")
data.sort()
print(f"data sort = {data}")

# mengurutkan balik data list sort
data_angka.reverse()
print(f"data reverse = {data_angka}")
data.reverse()
print(f"data reverse = {data}")

