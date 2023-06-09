import datetime 

mahasiswa1 = {
    'nama':'masruri',
    'nim': '42420022',
    'sks_lulus': 146,
    'beasiswa': False,
    'lahir': datetime.datetime(2001,12,28)
}

mahasiswa2 = {
    'nama':'azhar',
    'nim': '42420002',
    'sks_lulus': 148,
    'beasiswa': True,
    'lahir': datetime.datetime(2012,12,28)
}

mahasiswa3 = {
    'nama':'faiz',
    'nim': '42420012',
    'sks_lulus': 148,
    'beasiswa': True,
    'lahir': datetime.datetime(1998,12,28)
}

data_mahasiswa = {
    'mah001' : mahasiswa1,
    'mah002' : mahasiswa2,
    'mah003' : mahasiswa3
}
# :<7 artinya kita akan membuat tulisannya menjadi rata kiri dengan space berjumlah 7, klo rata kanan pake (:>)
print(f"{'KEY':<7}{'Nama':<17}{'NIM':<14}{'SKS':<4}{'Beasiswa':<10}{'Lahir':<10}")
print("-"*60)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%c") #.strftime("%X") artinya kita akan membuat format waktu dgn tahun/bulan/tanggal
                                                        #.strftime("%d") tgl | .strftime("%b") bulan  | .strftime("%c") lengkap       
    
    # :^10 artinya kita akan membuat tulisan rata tengah dengan space 10
    print(f"{KEY:<7}{NAMA:<17}{NIM:<14}{SKS:<4}{BEASISWA:^10}{LAHIR:<10}")
