# list -> contoh array pada python, dimana kita mengakses datanya dengan index
# dictionary(dict)->associative array->dimana kita bisa mengakses datanya dengan identifiernya
# identifier-> kita sebut sebagai key, sehingga untuk mengakses datanya tidak perlu lgi index
# pada data dictionary kita bisa menyelipkan data list
# data dictionary merupakan salah satu collation yang sangat power full di python 

data_list = ['aku', 'kamu', 'kita']
data_dict_1 = {
    'rm':'rumah makan',
    'rs':'rumah sakit'
}

data_dict = {
    # 'key':'value'
    'rr':'ruri',
    'nn':'nana',
    'no': 1000,
    '1': 'menang',
    'list': data_list, #cara menyisipkan data list pada data dict
    'dc': data_dict_1 #menyisipkan data dict pada data dict
}

print(data_dict['rr']) #cara mengaksesnya dengan memanggil key nya
print(data_dict['list']) #cara mengaksesnya dengan memanggil key nya
print(data_dict['dc']) #cara mengaksesnya dengan memanggil key nya
