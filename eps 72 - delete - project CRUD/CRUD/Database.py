# catatan saat membuat database = .txt
# 1. harus bikin dlu data frame nya (mau urutannya apa aja gtu guys)
# 2. tentukan panjang kolomnya, dimana isinya itu mau brpa banyak
# 3. harus dipastikan panjang kolomnya sama untuk semua entry
# agar ketika kita mau merubah/hapus kita hanya tinggal ganti 1 baris aja

from . import Operasi

# kalau ingin merubah nama databasenya, tinggal dirubah aja nilai dari varibale DB_NAME ini guys
DB_NAME = "data.txt"
# bikin template database menggunakan data dictionary
TEMPLATE = {
    "pk":"xxxxxx",
    "date_add":"yyyy-mm-dd",
    "judul":255*" ",
    "penulis":255*" ",
    "tahun":"yyyy"
}


def init_console():
    '''fungsi mengecek database'''
    try:
        # saat database tidak di temukan, program akan loncat ke except untuk membuat database baru data.txt
        with open(DB_NAME,mode="r") as file:
            print("Database tersedia, init done!")
    except:
        print("Database tidak ditemukan, silahkan membuat database baru")
        Operasi.create_first_data()
        # with open(DB_NAME,mode="w",encoding="utf-8") as file:
        #     penulis = input("Penulis :") 
        #     judul = input("Judul :") 
        #     tahun = input("Tahun :") 
            # data_str = f"{penulis},{judul},{tahun}"
            # file.write(data_str)