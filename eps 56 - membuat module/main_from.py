# memuat module matematika dengan import

# dari modul matematika kita akan mengimport fungsi tambah 
from matematika import tambah, kali, pangkat #manual mengambil 1 1 (tapi lebih rekomen yg ini, karna leih jelas)
from matematika import * #artinya mengamil semua yg ada di module matematike 

# penggunaannya akan seperti ini :
# berbeda dgn yang hanya menggunakan import saja
hasil_tambah = tambah(1,2,3,4,5)
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = kali(1,2,3,4,5)
print(f"hasil kali   = {hasil_kali}")

pangkat3 = pangkat(3)
print(f"hasil pangkat   = {pangkat3(5)}")