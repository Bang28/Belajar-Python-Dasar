# operasi komparasi
# setiap hasil dari komparasi adalah boolean
# >,<,>=,<=,==,!=,is,is not

a = 4
b = 2
# lebir besar dari >
print("======== lebih besar dari (>)")
hasil = a > 3
print(a,'>',3,'=',hasil)
hasil = b > 3
print(b,'>',3,'=',hasil)
hasil = b > 2
print(b,'>',2,'=',hasil)

print("======== kurang dari (<)")
hasil = a < 3
print(a,'<',3,'=',hasil)
hasil = b < 3
print(b,'>',3,'=',hasil)
hasil = b < 2
print(b,'>',2,'=',hasil)

print("======== lebih besar dari samadengan (>=)")
hasil = a >= 3
print(a,'>=',3,'=',hasil)
hasil = b >= 3
print(b,'>=',3,'=',hasil)
hasil = b >= 2
print(b,'>=',2,'=',hasil)

print("======== kurang dari samadengan (<=)")
hasil = a <= 3
print(a,'<=',3,'=',hasil)
hasil = b <= 3
print(b,'<=',3,'=',hasil)
hasil = b <= 2
print(b,'<=',2,'=',hasil)

print("======== samadengan (==)")
hasil = a == 4
print(a, '==', 4, '=', hasil)
hasil = b == 4
print(b, '==', 4, '=', hasil)

print("======== tidaksamadengan (!=)")
hasil = a != 4
print(a, '!=', 4, '=', hasil)
hasil = b != 4
print(b, '!=', 4, '=', hasil)

# <,>,<=,>=,!=,== (dapat bekeja pada syntax literal(contohnya pada baris-baris code di atas ))
# contoh a = 4 (dimana a adalah variabel dan 4 ada nilainya atau disebut literal dan a memakan memory sedang 4 tidak)

# is berfungsi untuk membandingkan nilai suatu objek(nilai sebuah variabel) dan tidak bisa bekerja pada syntax literal
print("======== object identity (is)") #is sebagai komparasi object identity
x = 5 #ini adalah assignment membuat object
y = 5
print("nilai x = ", x, ",id =",hex(id(x)))
print("nilai y = ", y, ",id =",hex(id(y)))
hasil = x is y
print("x is y=", hasil )

x = 5 #ini adalah assignment membuat object
y = 6
print("nilai x = ", x, ",id =",hex(id(x)))
print("nilai y = ", y, ",id =",hex(id(y)))
hasil = x is y
print("x is y=", hasil )

print("======== object identity (is not)") #is not sebagai komparasi object identity
x = 5 #ini adalah assignment membuat object
y = 5
print("nilai x = ", x, ",id =",hex(id(x)))
print("nilai y = ", y, ",id =",hex(id(y)))
hasil = x is not y
print("x is y=", hasil )

x = 5 #ini adalah assignment membuat object
y = 6
print("nilai x = ", x, ",id =",hex(id(x)))
print("nilai y = ", y, ",id =",hex(id(y)))
hasil = x is not y
print("x is y=", hasil )

