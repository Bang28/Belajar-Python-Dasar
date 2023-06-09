# init untuk mengatur urutan package pada python, menggabungkan/menyambukan package dengan module


import sains

hasil_tambah = sains.matematika.tambah(1,2,3,4,5) #ini kita tidak perlu lgi memanggil modulenya, bisa langsung packaeg terus fungsi, karna sudah di gabungkan di file init
print(f"ini hasil tambah = {hasil_tambah}")
hasil_pangkat = sains.matematika.pangkat(5) #ini kita tidak perlu lgi memanggil modulenya, bisa langsung packaeg terus fungsi, karna sudah di gabungkan di file init
print(f"ini hasil pangkat = {hasil_pangkat(5)}")
hasil_fisika = sains.fisika.gaya(1,2)
print(f"ini hasil gaya = {hasil_fisika}")

# from  sains  import *   

# hasil_tambah = matematika.basic.tambah(1,2,3,4,5) #ini kita tidak perlu lgi memanggil modulenya, bisa langsung packaeg terus fungsi, karna sudah di gabungkan di file init
# print(f"ini hasil tambah = {hasil_tambah}")
# hasil_fisika = fisika.gaya(1,2)
# print(f"ini hasil gaya = {hasil_fisika}")

