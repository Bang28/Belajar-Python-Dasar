# operator dictionary

data_dict = {
    "nn":"nana",
    "rr":"ruri",
    "if":"informatika"
}

# mengambil panjang dari dictionary
LENDICT = len(data_dict)
print(f"panjang dictionary : {LENDICT}")

# mengecek key exist atau tidak 
KEY = "rr"
CHECKKEY = KEY in data_dict
print(f"apakah key {KEY} ada di data dict : {CHECKKEY}")

# mengakses value(read) dengan get
print(data_dict['rr']) #tidak sepintar menggunakan .get untuk mengecek data
print(data_dict.get('rr')) #ini merupakan data dictionary, ditandai ada .get dstu
print(data_dict.get('ss','key tidak ditemukan')) #bisa menambahkan pesan 

# update data dict
data_dict['rr'] = "ruri inf"
print(data_dict)

# menambahkan data dict
data_dict['as'] = "aulia sapi"
print(data_dict)

# upadate data dict dengan cara elegan
data_dict.update({"rr":"ruri"})
print(data_dict)
data_dict.update({"zz":"zafran zzzzzz"}) #kalau key tidak ada, data akan tetap ditambahkan
print(data_dict)

# menghapus data pada dictionary
del data_dict['zz']
print(data_dict)

