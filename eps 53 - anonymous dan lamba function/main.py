# lambda function -> bisa membuat program kita lebih simple

def f_kuadrat(angka):
    '''fungsi biasa'''
    return angka

print(f"ini adalah hasil fungsi biasa {f_kuadrat(8)}")

# kita coba skrng dengan lamba
# cara penulisan : output = lambda argument : expression
kuadrat = lambda angka:angka**2 #dgn 1 input
print(f"hasil dari lambda kuadrat = {kuadrat(5)}")

pangkat = lambda number,power : number ** power #dgn 2 input
print(f"hasil lambda pangkat = {pangkat(4,3)} \n")

## kegunaan lambda function
# sorting untuk list
data_list = ["otong", "ucup", "ulil","zoli","atong"]
data_list.sort()
print(f"sorted list = {data_list} \n")

# sorting dgn fungsi biasa berdasarkan panjang karakter
def sortbylen(nama): 
    return len(nama)

data_list.sort(key=sortbylen) #key nya diambil dari fungsi sorbylen
print(f"sorted list by len dgn fungsi biasa = {data_list} \n")

# sorting dengan lambda 
data_list = ["otong", "ucup", "ulil","zoli","atong"]
data_list.sort(key=lambda nama:len(nama))
print(f"sorted list by len dgn lamba = {data_list} \n")

# filter dengan lambda
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]

def f_filter(angka):
    return angka < 5

data_angka_baru = list(filter(f_filter,data_angka)) #dgn fungsi biasa
print(f"dengan fungsi biasa = {data_angka_baru}")

data_angka_baru = list(filter(lambda x:x<5, data_angka)) #dgn lambda
print(f"dengan fungsi lambda = {data_angka_baru} \n")

# kasus genap
data_genap = list(filter(lambda x:x%2==0, data_angka))
print(f"dengan fungsi lambda = {data_genap} \n")
# kasus ganjil
data_ganjil = list(filter(lambda x:x%2==1, data_angka))
print(f"dengan fungsi lambda = {data_ganjil} \n")
# kelipatan 3
data_kelipatan_3 = list(filter(lambda x:x%3==0, data_angka))
print(f"dengan fungsi lambda = {data_kelipatan_3} \n")

# #anonymouse function
# 1. currying -> dari haskell curry 
def pangkat(angka, n):
    hasil =  angka ** n 
    return hasil

data_angka = pangkat(4,3)
print(f"ini dengan fungsi biasa = {data_angka}")

# dengan currying menjadi :
def pangkat(n):
    return lambda angka:angka**n

pangkat2 = pangkat(2) #nilai pangkat
print(f"pangkat 2 = {pangkat2(5)}") #nilai yg akan dipangkatkan
pangkat3 = pangkat(3) #nilai pangkat
print(f"pangkat 3 = {pangkat3(3)}") #nilai yg akan dipangkatkan
print(f"pangkat bebas = {pangkat(3)(4)}") #bisa jg kita gabungkan langsung untuk nilai pangkat & nilai yg akan dipangkatkan
