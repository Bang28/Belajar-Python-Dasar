# operasi logika atau boolean
# not, or, and, xor

print("==== NOT ====")
a = True
b = not a #object b akan melakukan operasi not pada object a, dimana nilai object b akan selalu kebalikanya dari nilai a
print("data a = ", a)
print("------- NOT")
print("data b = ", b)

print("==== OR ====") #OR akan bernilai FALSE ketika kedua nilainya False sisanya TRUE
a = True
b = True
c = a or b
print(a, 'OR', b, '=', c)
a = True
b = False
c = a or b
print(a, 'OR', b, '=', c)
a = False
b = True
c = a or b
print(a, 'OR', b, '=', c)
a = False
b = False
c = a or b
print(a, 'OR', b, '=', c)

print("==== AND ====") #AND akan bernilai True ketika kedua nilainya True sisanya false
a = True
b = True
c = a and b
print(a, 'AND', b, '=', c)
a = True
b = False
c = a and b
print(a, 'AND', b, '=', c)
a = False
b = True
c = a and b
print(a, 'AND', b, '=', c)
a = False
b = False
c = a and b
print(a, 'AND', b, '=', c)

print("==== XOR ====") #XOR akan bernilai True ketika salah satu nilainya True 
# XOR merupakan operasi bitwise bukan logika, tpi bisa digunakan pada operasi logika dengan simbol (^)
a = True
b = True
c = a ^ b
print(a, 'XOR', b, '=', c)
a = True
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)
a = False
b = True
c = a ^ b
print(a, 'XOR', b, '=', c)
a = False
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)
