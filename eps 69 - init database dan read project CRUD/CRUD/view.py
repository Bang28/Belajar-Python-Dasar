from . import Operasi


def read_console():
    data_file = Operasi.read()
    
    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"

    # ini adalah header
    print("\n"+"="*100)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}") #40 brrti kita akan memberikan lebar 40
    print("-"*100)

    # data (akan ditampilkan dalam bentuk list)
    for index,data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f"{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}", end="") #.40 artinya kita akan memberikan spasi sebanyak 40

    # footer
    print("="*100+"\n")