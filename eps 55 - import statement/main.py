# import 

# fungsinya adalah untuk mengambil program dari file eksternal .py

# 1. untuk menyambung program dari eksternal dan menjalankannya
import program_print
import program_ucup

# 2. import dengan datanya
import variable
import kucuy

# data ada di namaspce variable
print(variable.data) #cara mencetaknya
print(kucuy.data) #cara mencetaknya

# 3. import dengan fungsi
import matematika

hasil = matematika.tambah(4,5)
print(hasil)