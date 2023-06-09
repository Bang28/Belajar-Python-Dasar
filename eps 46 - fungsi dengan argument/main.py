# fungsi dengan argument
# diamana kita bisa mengisi fungsi ini dengan inputan

# cara penulisan fungsi di python :
'''
def nama_fungsi (argument):
    badan fungsi
'''

def hello_world(nama): 
    # fungsi hello_world untuk menerima input dengan variable nama
    print(f"selamat datang di dunia wahai orang baik {nama}")

hello_world("ruri") #ini adalah inputan pada sebuah fungsi
hello_world("nana")

# program penjumlahan
def tambah(angka1,angka2):
    '''fungsi tambah''' #ini namanya doc string
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")

tambah(1,5) #ini adalah inputan pada sebuah fungsi
tambah(12,13)

def say_hi(list_peserta):
    '''fungsi say_hi'''
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"yang terhormat {peserta}")

anggota_boyband = ["ucup", "nana", "asep"]

say_hi(anggota_boyband)