'''Keyword Argument (kwargs)'''

def fungsi(nama,tinggi, berat):
    '''ini fungsi biasa '''
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("asep", 189, 68)

def fungsi(**kwargs):
    '''ini fungsi kwargs '''
    nama = kwargs['nama']
    tinggi = kwargs['tinggi']
    berat = kwargs['berat']
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(nama="asep", tinggi=189, berat=68)


# studi kasus
def math(*args,**kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output += angka

        # print("operasi penumlahan")
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka
        # print("operasi perkalian")
    else:
        print("tidak ada operasi")

    return output 

hasil = math(1,2,3,4,5,6,option="tambah")
print(f"hasil jumlah {hasil}")
hasil = math(1,2,3,4,5,6,option="kali")
print(f"hasil kali {hasil}")

