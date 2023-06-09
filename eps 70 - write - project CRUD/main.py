import os
import CRUD as CRUD 


# ini adalah portal utama progam kita
# pake if name ini supaya nnti kalau kita running program itu lebih rapi
# ini sebenarnya konvensi dimana kita bikin program pake python kita pake if name ini
if __name__ == "__main__":
    # untuk mendeteksi sistem operasi device kita itu apa
    sistem_operasi = os.name

    # untuk memebersihkan tampilan terminal sesuai dengan os yg terdeteksi secara otomatis
    match sistem_operasi:
        case "posix": os.system("clear") #macos #linux
        case "nt":os.system("cls") #windows

    
    print("SELAMAT DATANG DI PROGRAM")
    print("DATABASE PERPUSTAKAAN")
    print("=========================")

    # check databse itu ada atau tidak
    CRUD.init_console()

    # membuat menu
    while (True):
        # untuk memebersihkan tampilan terminal sesuai dengan os yg terdeteksi secara otomatis
        match sistem_operasi:
            case "posix": os.system("clear") #macos #linux
            case "nt":os.system("cls") #windows

        print("SELAMAT DATANG DI PROGRAM")
        print("DATABASE PERPUSTAKAAN")
        print("=========================")

        print(f"1. Read Data")
        print(f"2. Create Data")
        print(f"3. Update Data")
        print(f"4. Delete Data \n")

        # menerima input masukan opsi dari user
        user_option = input("Masukan opsi :")

        # print("\n=========================\n")

        # mengamil input dari user dan mencocokkannya pake case 1-4
        match user_option:
            case "1": CRUD.read_console()
            case "2": CRUD.create_console()
            case "3": print("Update Data")
            case "4": print("Delete Data")
        
        # print("\n=========================\n")

        # membuat pilihan lanjut / break
        is_done = input("Apakah selesai (y/n)?")
        if is_done == "y" or is_done == "Y":
            break

    print("program berakhir") 