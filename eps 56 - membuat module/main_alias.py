# memuat module matematika dengan import

# dari modul matematika kita akan mengimport fungsi tambah 
#penggunan alias hari 1 1, tidak bisa langsung di gabung dengan 1 nama alias yg sama
from matematika import tambah as t 
from matematika import kali as k
from matematika import pangkat as p
# from matematika import * #artinya mengamil semua yg ada di module matematike 

# penggunaannya akan seperti ini :
# berbeda dgn yang hanya menggunakan import saja
hasil_tambah = t(1,2,3,4,5)
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = k(1,2,3,4,5)
print(f"hasil kali   = {hasil_kali}")

pangkat3 = p(3)
print(f"hasil pangkat   = {pangkat3(5)}")