'''default argument'''

# contoh fungsi dengan nilai default argument
'''
def fungsi(argument = nilai defaultna):

'''
# contoh 1
def say_hello(nama = "hamba allah"): #hamba allah adalah nilai defaultnya dari argument pada fungsi ini
    '''fungsi dengan default argument'''
    print(f"hallo {nama} \n")

say_hello()

# contoh 2
def sapa_dia(nama, pesan = "gimana belajarnya hari ini?"):
    '''fungsi dengan satu input biasa, dan satu dengan default argument'''
    print(f"hai {nama}, {pesan} \n")

sapa_dia("ruri", "selamat belajar")
sapa_dia("maung")

# contoh 3
def hitung_pangkat(angka, pangkat):
    hasil = angka**pangkat
    return hasil

print(hitung_pangkat(9,2))
hasil = hitung_pangkat(pangkat=8, angka=2)
print(hasil)
print("\n")

# contoh 4
def fungsi(input1=1, input2=2, input3=3, input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil

print(fungsi())
# kita bisa merubah nilai default dari sebuah argument pada fungsi, contohnya :
print(fungsi(input1=10)) #seperti ini contoh merubah sebuah nilai argument pada fungsi
