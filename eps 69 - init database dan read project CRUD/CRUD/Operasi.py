from . import Database
from .Util import random_string
import time


def create_first_data():
    '''fungsi create database kalo semisal database tidak ditemukan'''
    penulis = input("Penulis: ")
    judul = input("Judul: ")
    tahun = input("Tahun: ")

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
    data["tahun"] = tahun

    # data frame nya akan kita taro ke data_str
    data_str = f"{data['pk']},{data['date_add']},{data['penulis']},{data['judul']},{data['tahun']}\n"
    print(data_str)
    try:
        with open(Database.DB_NAME,mode="w",encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("udah jadi")


def read():
    '''fungsi membaca database'''
    try:
        with open(Database.DB_NAME,mode="r") as file:
            content = file.readlines()
            return content
    except:
        print("Membaca database error")
        return False
    