# prakter konversi type data

#mengambil input data dari user 

#data yg di masukan pasti berupa string
data = input("Masukan data : ")
print("data = ", data,"type",type(data))


#jika ingin mengambil int, maka
data_int = int(input("Masukan nilai integer : "))
print("data = ", data_int,"type",type(data_int))


#jika ingin mengambil data float, maka
data_float = float(input("Masukan nilai float : "))
print("data = ", data_float,"type",type(data_float))


#jika ingin mengambil data boolean, maka
data_bool = bool(int(input("masukan nilai boolean: ")))
print("data = ", data_bool, "type =", type(data_bool))

