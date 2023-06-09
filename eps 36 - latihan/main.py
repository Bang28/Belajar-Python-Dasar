# latihan menggunakan list

list_buku = []
while True:
    print("\nMasukan Data Buku")
    judul = input("Masukan judul buku \t: ")
    penulis = input("Masukan nama penulis \t: ")

    #data yg diinputkan akan ditampung ke dalam variable data_buku
    data_buku = [judul, penulis]
    #data yang sudah dimasukan ke data_buku akan ditambahkan ke list_buku
    list_buku.append(data_buku)
    
    print("\n\n","="*10,"Data Buku","="*10)
    for index,buku in enumerate(list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]}")
    print("\n\n","="*20)
    isLanjut = input("Apakah dilanjutkan? (y/n)")

    if isLanjut == "n":
        break

print("Program Selesai")


