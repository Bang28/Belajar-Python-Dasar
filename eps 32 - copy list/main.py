# teknik menduplikat list

a = ["ucup", "otong", "dudung"]
print(f"a = {a}")

b = a #ini bukan mengcopy list
print(f"b = {b}")

# kita akan merubah list dari a

# ini akan merubah kedua list
a[1] = "sausan" 
b.sort()
print(f"a = {a}")
print(f"b = {b}")
# kenapa kedua ikut berubah
# because address pada a dan b itu sama, mari kita cek
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")

# menduplikat list dengan copy
# data yang dirubah tidak akan mempengarusi data awal
print("membuat list c dengan a.copy()")
c = a.copy() #full duplikat/data baru
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("kita ubah data 1")
c[1] = "meimei"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
