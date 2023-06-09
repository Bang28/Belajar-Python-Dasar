# latihan perulangan

# membuat segitiga 
# 1. menggunakan for
sisi = 10
count = 1 # dummy variable
for i in range(sisi):
    print("*"*count)
    count +=1

print("akhir dari for\n")

# 2. menggunakan while
count = 1
while True:
    print("*"*count)
    count +=1
    if count > sisi :
        break

print("akhir dari while\n")

# 3. bikin hanya ganjil saja
count = 1
while True:
    if count %2:
        # akan print jika ganjil
        print("*"*count)
        count += 1
    else:
        # akan kembali ke atas jika genap
        count += 1
        continue 
        print("akan dilewati")
    

    # akan berhenti jika count melebihi sisi
    if count > sisi :
        break

print("akhir dari while\n")


# 4. bikin hanya ganjil saja
count = 1
spasi = int(sisi/2)
while True:
    if count %2:
        # akan print jika ganjil
        print(" "*spasi,"*"*count)
        spasi -= 1
        count += 1
    else:
        # akan kembali ke atas jika genap
        count += 1
        continue 
        print("akan dilewati")
    

    # akan berhenti jika count melebihi sisi
    if count > sisi :
        break

print("akhir dari while\n")

