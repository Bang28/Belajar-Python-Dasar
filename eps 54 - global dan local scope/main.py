## global dan local scope

# memasukan variable langsung ke dalam fungsi

var_global = "otong" #<- ini namanya variable global 

# akses variable global dalam fungsi
def fungsi1():
    print(f"fungsi1 menampilkan {var_global}")

fungsi1()

# akses variable global dalam looping
for i in range(0,5):
    print(f"loop {i} - {var_global}")

# akses dengan percabangan
if True:
    print(f"if menampilkan {var_global}")

##variable local scope

def fungsi2():
    nama_local = "ucup" #<- ini namanya variable local, hanya bisa diakses didalam fungsi ini

fungsi2()
# print(nama_local) #tidak bisa dilakukan 

## contoh 1: penggunaan akses variable global
'''bisa jg variable namanya ditaro disini biar jadi variabel global'''
def say_otong():
    print(f"hello {nama}")

nama = "ucup" #bisa ditaro disini, atau di atas fungsi agar variabel global ini bisa diakses oleh fungsi tersebut, yang penting jgn setelah pemanggilan fungsi naronya
say_otong()
'''jangan taro di sini, ntr fungsi diatasnya error, karna tidak ada variabel nama yg bisa di panggil'''
def say_hello():
    print(f"hai {nama}")

say_hello()

## contoh 2: merubah nilai variable global dengan fungsi
angka = 0

def ubah_angka(nilai_baru):
    global angka #fungsi ini untuk mendapatkan akses merubah nilai variabel global
    angka = nilai_baru

print(f"sebelum dirubah = {angka}")
ubah_angka(10)
print(f"sesudah dirubah = {angka}")


## contoh 3: variabel local & global tidak pengaruh pada penggunaan for & if
angka = 0
for i in range(0,5):
    angka += i
    angka_dummy = 0

print(angka)
print(angka_dummy)

if True:
    angka_dummy = 10

print(angka)
print(angka_dummy)