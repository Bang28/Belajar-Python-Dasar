# __main__ top level code environment

# __name__ == "__main__"

# # __name__ pada file program utama
# __name__ akan berubah menjadi __main__ saat kita panggil pada program utaman
print(f"nilai __name__ pada main.py = {__name__}") 


# #__name__ pada file program eksternal
# kalau seperti ini, nilainya sudah beda lagi
import fungsi 

# #contoh penggunaan __main__

# deklarasi
def f_tambah(a:int,b:int)->int:
    return a + b

# fungsi utama
if __name__ == "__main__":
    angka1 = 5
    angka2 = 10
    hasil = f_tambah(angka1,angka2)
    print(f"hasil tambah = {hasil}")

# #import package
import package
