'''*args'''

# memasukkan banyak data/argument 

# fungsi dengan gaya penulisan biasa (kurang rekomendet jg)
def fungsi(nama,tinggi,berat):
    print(f"{nama} punya tinggi {tinggi} dan berat{berat}")

fungsi("ani", 159, 47)


# fungsi dengan datalist (tidak direkomendasikan penggunaan seperti ini)
def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(["ucup", 180, 60])


# kenalan dengan *args atau argument
# ini adalah cara mengambil banyak input pada fungsi di python
def fungsi (*args): #dengan menggunakan *args kita bebas memasukkan banyak data sekalipun
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("lala", 150, 50)


# studi kasus
def tambah(*data): #tanda * didepan argument (data) menandakan itu adalah *args, dimana kita bebas menginputkan berapapun
    # data tipenya adalah tuples, dia bisa diiterasi
    output = 0
    for angka in data:
        output += angka

    return output

hasil = tambah(1,23,4,5,6,7,9)
print(f"hasil = {hasil}")



