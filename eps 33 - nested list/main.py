# nested list 

data_list_biasa = [1,2,3,4]
data_0 = [2,3,4]
data_1 = [2,4,1,2]

list_2D = [data_0,data_1,data_list_biasa] #list di dalam list
print(f"list 2D = {list_2D}")

# contoh penggunaan 
peserta_0 = ["ucup", 25, "laki-laki"]
peserta_1 = ["otong", 12, "laki-laki"]
peserta_2 = ["memei", 23, "perempuan"]

list_peserta = [peserta_0,peserta_1,peserta_2]
print(f"perserta = {list_peserta}")

# manfaat penggunaan nested list :
for peserta in list_peserta:
    print(f"nama \t :{peserta[0]}")
    print(f"umur \t :{peserta[1]}")
    print(f"gender \t :{peserta[2]}\n")

# nested list terdapat masalah dengan reference 

list_copy = list_peserta.copy()
print(f"perserta = {list_copy}")
peserta_0[0] = "maung"
print(f"perserta = {list_copy}")
print(f"perserta = {list_peserta}")



