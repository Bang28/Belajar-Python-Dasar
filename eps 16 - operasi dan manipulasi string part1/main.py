# operasi dan manipulasi string

# 1. menyambung string (namanya concatenate)

nama_pertama = "Muhammad"
nama_tengah = "Masruri"
nama_akhir = "Maung"

nama_lengkap = nama_pertama +" "+ nama_tengah +" "+ nama_akhir
print(nama_lengkap)

# 2. menghitung panjang dari string
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang)) #fungsi str adalah untuk merubah typedata dari object panjang ke string

# 3. operator untuk string
# mengecek apakah ada komponen chat atau string pada string
d = "A" 
status = d in nama_lengkap #nilai pada object d (A) ada di object nama lengkap -> salah
print(d + " ada di " + nama_lengkap + " = " +  str(status)) 
d = "a" 
status = d in nama_lengkap #nilai pada object d (a) ada di object nama lengkap -> benar
print(d + " ada di " + nama_lengkap + " = " +  str(status)) 
d = "A" 
status = d not in nama_lengkap #nilai pada object d (A) tidak ada di object nama lengkap -> benar
print(d + " ada di " + nama_lengkap + " = " +  str(status)) 

# mengulang string
print("wk"*10)
print(10*"wk")

# indexing (kita mengambil data dari string)
print("index ke-0 : "+ nama_lengkap[0])
print("index ke-1 : "+ nama_lengkap[1])
print("index ke-(-1) : "+ nama_lengkap[-1]) #jika index yg dimasukkan minus, maka data yg diambil dimulai dari belakang
print("index ke-(-2) : "+ nama_lengkap[-2]) #jika index yg dimasukkan minus, maka data yg diambil dimulai dari belakang
print("index ke-[0-3] : "+ nama_lengkap[0:3]) #indexing range/rentang pada python, data index terakhir tidak akan diambil oleh python (sudah bawaan python)
print("index ke-[0,2,4,6,8,10] : "+ nama_lengkap[0:10:2]) #2 diakhir merupakan increment, cara bacanya kita akan mengambil data dari index ke 0 sampai 10 dengan kenaikan/kelipatan 2

# item paling kecil
print("paling kecil :" + min(nama_lengkap))
# item paling besar
print("paling besar :" + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah "+str(ascii_code))
data = 117
print("char untuk 117 adalah "+chr(data))

# 4. operator dalam bentuk method
data = "otong surotong pararotong"
jumlah = data.count("o") #data adalah objectnya dan count() adalah method nya
print("jumlah o pada data "+ data + " = " + str(jumlah))
