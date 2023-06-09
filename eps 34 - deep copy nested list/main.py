data_0 = [1,2,3]
data_1 = [4,5,6]

data_2D = [data_0,data_1]
data_2D_copy = data_2D.copy()
print(f"data 2D = {data_2D}")
print(f"data 2D copy = {data_2D_copy}")

# mengambil data nested list
data = data_2D[1][1] #1 pertama (x), 1 kedua (y), cara pengambilannya sama kaya data pada matrik
print(f"data = {data}")

# liat address semua nested list
print(f"address asli = {hex(id(data_2D))}")
print(f"address copy = {hex(id(data_2D_copy))}")

# menggunkan deep copy untuk megatasi masalah pada nested reference
from copy import deepcopy 
data_2D = [data_0,data_1,10]
data_2D_deepcopy = deepcopy(data_2D)

print(f"address asli = {hex(id(data_2D[0]))}")
print(f"address deep = {hex(id(data_2D_deepcopy[0]))}")

data_2D[1][0] = 30
print(f"data 2D = {data_2D}")
print(f"data 2D copy = {data_2D_copy}")
print(f"data 2D copy = {data_2D_deepcopy}")

