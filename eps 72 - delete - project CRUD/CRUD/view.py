from . import Operasi


def read_console():
    '''fungsi membaca data'''
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


def create_console():
    '''fungsi menambahkan data'''
    print("\n\n"+"="*100)
    print("Silahkan tambah data buku\n")
    
    penulis = input("Penulis\t: ")
    judul = input("Judul\t: ")
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

    Operasi.create(tahun,judul,penulis)
    print("\nBerikut adalah data baru anda")
    read_console()


def update_console():
    '''fungsi merubah data'''
    read_console() #memanggil fungsi read

    while (True):
        print("Pilih nomer buku yang akan diupdate: ")

        # mengambil nomer buku
        no_buku = int(input("Nomer Buku: "))
        data_buku = Operasi.read(index=no_buku)

        if data_buku:
            break
        else:
            print("nomer tidak valid, silahkan input ulang")

    data_break = data_buku.split(',')
    pk = data_break[0]
    data_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1] #:-1 untuk mengambil enter dari database

    while (True):
        # data yang ingin di update
        print("\n"+"="*100)
        print("Pilih data buku yang akan dirubah")
        print(f"1. Judul\t:{judul:.40}")
        print(f"2. Penulis\t:{penulis:.40}")
        print(f"3. Tahun\t:{tahun:4}")

        # memilih mode untuk update
        user_option = input("Pilih data [1,2,3]: ")
        print("\n"+"="*100)
        match user_option:
            case "1": judul = input("Judul\t: ")
            case "2": penulis = input("Penulis\t: ")
            case "3": 
                # membuat inputan tahun berupa string, dan panjangnya harus 4 karakter
                while (True):
                    try:
                        tahun = int(input("Tahun\t: "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print("tahun salah, silahkan input ulang tahun(yyyy)")

                    except:
                        print("tahun harus angka, silahkan input ulang tahun(yyyy)")

            case _: print("index tidak cocok")

        print("Data baru anda")
        print(f"1. Judul\t:{judul:.40}")
        print(f"2. Penulis\t:{penulis:.40}")
        print(f"3. Tahun\t:{tahun:4}")
        
        # membuat pilihan lanjut / break
        is_done = input("Apakah sudah sesuai (y/n)?")
        if is_done == "y" or is_done == "Y":
            break
    
    Operasi.update(no_buku,pk,data_add,tahun,judul,penulis)


def delete_console():
    '''fungsi menghapus data'''
    read_console()
    while (True):
        print("Pilih nomer buku yang akan di delete: ")

        # mengambil nomer buku
        no_buku = int(input("Nomer Buku: "))
        data_buku = Operasi.read(index=no_buku)

        if data_buku:
            data_break = data_buku.split(',')
            pk = data_break[0]
            data_add = data_break[1]
            penulis = data_break[2]
            judul = data_break[3]
            tahun = data_break[4][:-1] #:-1 untuk mengambil enter dari database


            # data yang ingin di delete
            print("\n"+"="*100)
            print("Data buku yang akan dihapus")
            print(f"1. Judul\t:{judul:.40}")
            print(f"2. Penulis\t:{penulis:.40}")
            print(f"3. Tahun\t:{tahun:4}")


            # membuat pilihan lanjut / break
            is_done = input("Apakah anda yakin (y/n)?")
            if is_done == "y" or is_done == "Y":
                Operasi.delete(no_buku)
                break
        else:
            print("nomer tidak valid, silahkan input ulang")

    print("Data berhasil dihapus")



