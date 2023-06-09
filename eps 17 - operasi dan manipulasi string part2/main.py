# oprator dalam bentuk method

## merubah case dari string
# meruah semua ke upper case (huruf besar)
salam = "bro!"
print("normal = ", salam)
salam = salam.upper()
print("upper = ", salam)

# meruah semua ke lower case (huruf kecil)
alay = "Aku KEce ABiezZZZ"
print("normal = ", alay)
alay = "Aku KEce ABiezZZZ".lower()
print("lower = ", alay)

## pengecekan dengan isX method
# contoh pengecekan lower case dan upper case
salam = "sist"
apakah_lower = salam.islower() #hasilnya boolean
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper() #hasilnya boolean
print(salam + " is upper = " + str(apakah_upper))

# isalpha()->untuk mengecek kalau semuanya adalah huruf
# isalnum()->untuk huruf dan angka
# isdecimal()->untuk angka saja
# isspace()->spasi,tab,newline
# istitle()->apabila semua kata komponen string dimulai hurup besar

judul = "It Is Okey Not To Be Orkay "
cek_judul = judul.istitle()
print(judul + " is title = " + str(cek_judul))
cek_judul = judul.isalpha()
print(judul + " is alpha = " + str(cek_judul))
cek_judul = judul.isalnum()
print(judul + " is alnum = " + str(cek_judul))
cek_judul = judul.isdecimal()
print(judul + " is decimal = " + str(cek_judul))
cek_judul = judul.isspace()
print(judul + " is space = " + str(cek_judul))

## ngecek komponen startswith() endswitch() 
cek_start = "Kimetsu No Yaiba".startswith("Kimetsu")
print("Kata pertama dimulai dari Kimetsu? = " + str(cek_start))
cek_end = "Kimetsu No Yaiba".endswith("Yaiba")
print("Kata terakhir adalah Yaiba? = " + str(cek_end))

## penggabungan komponen join() split()
pisah = ['aku','belajar','python']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = "akuiyabelajariyapython".split('iya')
print(gabungan)
gabungan = "akuiyabelajariyapython"
print(gabungan.split('iya')) #sama aja hasilnya kaya yg diatas, cuma beda cara penulisan saja

## alokasi karakter rjust() ljust() center()
kanan = "kanan".rjust(10)
print("'"+kanan+"'")
kiri = "kiri".ljust(10)
print("'"+kiri+"'")
tengah = "tengah".center(10, "=") #ditambah menggunakan argument, biar ga polos banget pake space kalo aslinya
print("'"+tengah+"'")

# kebalikannya dari rjust(), ljust(), & center() ==> strip()
tengah = tengah.strip("=")
print("'"+tengah+"'")

