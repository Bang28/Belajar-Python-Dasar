## list
# list-> kumpulan data, beda dengan B.pemro lain yg menyebutnya dengan array

# kumpulan data numer
angka = [1,2,3,4,5] 

# kumpulan data string
data_string = ["kakak, adek, sodara"]

# kumpulan data boolean
data_boolean = [True, False, True, False]

# kumpulan data campuran
data_campuran = [1,"kakak",2,"adek"]

# cara alternatif membuat list
data_range = range(0,10,2) #range(start, stop, step)
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop, list dengan comprehenship
list_pake_for = [i**2 for i in range (0,10)] #**2 untuk memangkatkan nilai range yang ditampung i
print(list_pake_for)

# membuat list pake for pake if
list_pake_for_if = [i for i in range(0,10) if i != 5]
print(list_pake_for_if)
list_pake_for_if = [i for i in range(0,10) if i%2 == 0]
print(list_pake_for_if)
list_pake_for_if = [i for i in range(0,10) if i%2 != 0]
print(list_pake_for_if)


