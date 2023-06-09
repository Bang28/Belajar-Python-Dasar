# #operasi 

# index  0(-3)   1(-2)     2(-1)
data = ["ucup", "otong", "dudung"]

# mengambil data dari list ini
print(f"data dari index ke 0 -> {data[0]}")
print(f"data dari index ke 1 -> {data[1]}")
print(f"data dari index ke 2 -> {data[2]}")

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjangnya data = {panjang_data}")


## manipulasi data list
# menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah = \n{data}")
data.insert(1,"nana")
print(f"data sesudah ditambah = \n{data}")

# menambahkan item di akhir list
data.append("maung")
print(f"data ditambah lagi = \n{data}")

# menambahkan list dengan list atau menggabungkan list
data_baru = ["adi","bayu","andi"]
data.extend(data_baru)
print(f"data gabungan = \n{data}")

# merubah data pada list
# kita ubah data ke 2 
data[2] = "sausan"
print(f"data dirubah = \n{data}")

# menghapus data pada list
data.remove("maung")
print(f"data remove = \n{data}")

# menghapus data paling belakang pada list
data.pop()
print(f"remove data akhir = \n{data}")  