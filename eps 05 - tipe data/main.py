#tipe data : angka bilangan bulat(integer)
import ctypes


data_integer = 1
print(type (data_integer))
print("data : ", data_integer, ", bertipe :", type(data_integer))

#tipe data : pecahan (float) 
#tidak ada tipe data double di python, semua menggunakan float
data_float = 3.14
print(type (data_float))
print("data : ", data_float, ", bertipe :", type(data_float))

#tipe data : karakter (string) 
data_string = "ini string"
print(type (data_string))
print("data : ", data_string, ", bertipe :", type(data_string))

#tipe data : biner true/false (boolean) 
data_bool = True
print(type (data_bool))
print("data : ", data_bool, ", bertipe :", type(data_bool))

##tipe data khusus
#bilangan kompleks
data_complex = complex(5,6)
print(type (data_complex))
print("data : ", data_complex, ", bertipe :", type(data_complex))

#tipe data dari bahasa C(berikut contoh cara menggunakannya)
from ctypes import c_double
data_c_double = c_double(10,5)
print("data : ", data_c_double)
print("- bertipe : ", type(data_c_double))
