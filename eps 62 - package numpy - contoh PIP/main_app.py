import numpy as np

list_a = [1,2,3,4]
vector_a = np.array([1,2,3,4])
# perbedaanya list_a dgn vector_a (1. bentuk datanya)
print(f"ini list a = {list_a}") #tidak bisa melakukan sebuah operasi
print(f"ini vector a = {vector_a}") #bisa melakukan operasi aritmatika didalamnya
# contoh :
print(f"ini vector a dipangkatkan 2 = {vector_a**2}") #bisa melakukan operasi aritmatika didalamnya


matrix_a = np.array([(1,2),(3,4)])
print(f"ini matrib a = \n{matrix_a}")
print(f"ini matrib a kudrat= \n{matrix_a**2}")

zeros_a = np.zeros([2,2]) #nilai pada matrik nya akan 0 semua
print(f"zeros a = \n{zeros_a}")

ones_a = np.ones([2,2]) #nilai pada matrik nya akan 1 semua
print(f"zeros a = \n{ones_a}")

jumlah = matrix_a + zeros_a + ones_a
print(f"hasil penjumlahan matrix = \n{jumlah}")