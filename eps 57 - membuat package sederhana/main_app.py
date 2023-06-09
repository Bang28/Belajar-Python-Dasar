# package adalah sebuah program/tempat dimana kita menyimpan/menaruh module-module kita dstu guys
# _pycache_ fungsinya adalah membuat si program berjalan lebih cepat
# import time
# t_start = time.time()

# sains <- ini nama package nya
# matematika <- ini nama module nya
'''cara cara memanggil package dengan modulnya nih guys'''
import sains.matematika 
from sains import fisika
from sains.fisika import gaya as force

hasil_tambah = sains.matematika.tambah(1,2,3,4,5)
print(f"hasil tambah dari package adalah {hasil_tambah}")

gaya = force(90,10)
print(f"gaya adalah {gaya}")


# t_end = time.time()
# print(f"waktu eksekusi adalah {t_end - t_start}")
