# date and time(latihan)

import datetime as dt

hari_ini = dt.date.today()
print(hari_ini)
print(f"hari ini adalah hari = {hari_ini:%A}")

tanggal = dt.date(2001,12,28)
print(tanggal)
print(f"hari ini adalah hari = {tanggal:%A}")

print("silahkan masukkan tanggal, \nbulan, tahun lahir anda :")
tanggal = int(input("masukan tanggal \t: "))
bulan = int(input("masukan bulan \t\t: "))
tahun = int(input("masukan tahun \t\t:"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"tanggal lahir anda adalah : {tanggal_lahir}")
print(f"lahir pada hari : {tanggal_lahir:%A}")

hari_ini = dt.date.today()
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365 #.days artinya kita hanya akan mengambil angkanya saja tanpa format datanya. //untuk membulatkan hasil bagi
umur_bulan_sisa = (umur_hari.days % 365) // 30 
umur_hari_sisa = umur_bulan_sisa % 30
print(f"umur anda saat ini adalah : {umur_hari}")
print(f"umur anda saat ini adalah : {umur_tahun} tahun {umur_bulan_sisa} bulan {umur_hari_sisa} hari")
