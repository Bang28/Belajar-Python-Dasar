from time import time
from . import Database
from .Util import random_string
import time
import os


def create_first_data():
    '''fungsi create database kalo semisal database tidak ditemukan'''
    penulis = input("Penulis: ")
    judul = input("Judul: ")
    # membuat inputan tahun berupa string, dan panjangnya harus 4 karakter
    while (True):
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun))==4:
                break
            else:
                print("tahun salah, silahkan input ulang tahun(yyyy)")

        except:
            print("tahun harus angka, silahkan input ulang tahun(yyyy)")

    # mengcopy frame template database ke variabel data
    data = Database.TEMPLATE.copy()

    # #ini adalah data frame
    # membuat primary key secara acak dgn panjang karakter 6 digit
    data["pk"] = random_string(6)
    # menambahkan waktu pada data yang kita inputkan dgn format(tahun,bulan,tanggl,jam,menit,detik) waktu indonesia
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S-%z",time.gmtime())
    # mengambil inputan nama penulis ditambah dgn spasi sisanya dari template database
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    # data frame nya akan kita taro ke data_str
    data_str = f"{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n"
    print(data_str)
    try:
        with open(Database.DB_NAME,mode="w",encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("udah jadi")


def read(**kwargs):
    '''fungsi membaca database'''
    try:
        with open(Database.DB_NAME,mode="r") as file:
            content = file.readlines()

            # program tambahan untuk update data
            jumlah_buku = len(content)
            if "index" in kwargs:
                index_buku = kwargs["index"]-1
                if index_buku < 0 or index_buku > jumlah_buku:
                    return False
                else:
                    return content[index_buku]
                
            else:
                return content
    except:
        print("Membaca database error")
        return False
    

def create(tahun,judul,penulis):
    # mengcopy frame template database ke variabel data
    data = Database.TEMPLATE.copy()

    # #ini adalah data frame
    # membuat primary key secara acak dgn panjang karakter 6 digit
    data["pk"] = random_string(6)
    # menambahkan waktu pada data yang kita inputkan dgn format(tahun,bulan,tanggl,jam,menit,detik) waktu indonesia
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S-%z",time.gmtime())
    # mengambil inputan nama penulis ditambah dgn spasi sisanya dari template database
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    # data frame nya akan kita taro ke data_str
    data_str = f"{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n"
    # print(data_str)
    
    try:
        with open(Database.DB_NAME,mode="a",encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("udah jadi")



def update(no_buku,pk,data_add,tahun,judul,penulis):
    # mengcopy frame template database ke variabel data
    data = Database.TEMPLATE.copy()

    # #ini adalah data frame
    # membuat primary key secara acak dgn panjang karakter 6 digit
    data["pk"] = pk
    # menambahkan waktu pada data yang kita inputkan dgn format(tahun,bulan,tanggl,jam,menit,detik) waktu indonesia
    data["date_add"] = data_add
    # mengambil inputan nama penulis ditambah dgn spasi sisanya dari template database
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    # data frame nya akan kita taro ke data_str
    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'

    panjang_data = len(data_str)
    try:
        with open(Database.DB_NAME,mode="r+",encoding="utf-8") as file:
            file.seek(panjang_data*(no_buku-1))
            file.write(data_str)

    except:
        print("error update")


def delete(no_buku):
    '''fungsi delete'''
    try:
        with open(Database.DB_NAME,mode="r") as file:
            counter = 0
            
            while(True):
                content = file.readline()
                if len(content) == 0:
                    break
                elif content == no_buku - 1:
                    pass
                else:
                    with open("data_temp.txt",mode="a",encoding="utf-8") as temp_file:
                        temp_file.write(content)
                counter += 1
    except:
        print("database error")

    os.rename("data_temp.txt",Database.DB_NAME)