# contoh membuat exception

from numbers import Number

def tambah(a,b):
    if not isinstance(a,Number) or not isinstance(b,Number):
        raise "input pertama harus angka"
    return a+b
print(tambah(5,6)) #kalau satau satu inputnya berupa string, maka akan muncul error exception


angka = 0
try:
    hasil = 10/angka
except Exception as error_message:
    print(error_message)

try:
    hasil = 10/angka
except ZeroDivisionError as error_message: #sama aja kek yg diatasnya
    print(error_message)
