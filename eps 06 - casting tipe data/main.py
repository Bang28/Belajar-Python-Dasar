#belajar casting
#yaitu merubah dari satu tipe data ke tipe data lain
#tipe data = int, float, string, boolean

##integer
print("====INT====")
data_int = 9;
print("data : ", data_int, ",type =", type(data_int))

data_float = float(data_int) #mengkonversi ke type data float
data_str = str(data_int) #mengkonversi ke type data string
data_bool = bool(data_int) #nilai false ketika int = 0
print("data : ", data_float, ",type =",type(data_float))
print("data : ", data_str, ",type =",type(data_str))
print("data : ", data_bool, ",type =",type(data_bool))


##float
print("====FLOAT====")
data_float = 9.9;
print("data : ", data_float, ",type =", type(data_float))

data_int = int(data_float) #nilai akan dibulatkan ke bawah (9.9 = 9)
data_str = str(data_float) #mengkonversi ke type data string
data_bool = bool(data_float) #nilai false ketika float = 0
print("data : ", data_int, ",type =",type(data_int))
print("data : ", data_str, ",type =",type(data_str))
print("data : ", data_bool, ",type =",type(data_bool))


##boolean
print("====BOOLEAN====")
data_bool = True;
print("data : ", data_bool, ",type =", type(data_bool))

data_int = int(data_bool) #nilai akan 1 jika true & 0 jika false
data_str = str(data_bool) #hanya akan merubah type datanya ke string
data_float = float(data_bool) #konversi ke type data float 
print("data : ", data_int, ",type =",type(data_int))
print("data : ", data_str, ",type =",type(data_str))
print("data : ", data_float, ",type =",type(data_float))


##string
print("====STRING====")
data_str = "10"; #jika nilai nya berupa karakter, tidak bisa di casting ke INTEGER
print("data : ", data_str, ",type =", type(data_str))

data_int = int(data_str) #string harus angka
data_bool = bool(data_str) #sring harus angka
data_float = float(data_str) #false jika string kosong ("";)
print("data : ", data_int, ",type =",type(data_int))
print("data : ", data_bool, ",type =",type(data_bool))
print("data : ", data_float, ",type =",type(data_float))


