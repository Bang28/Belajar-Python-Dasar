# control flow (continue, pass, break)

# pass -> berfungsi sebagai dummy, tidak akan dieksekusi
# angka = 0
# while angka < 5:
#     angka += 1
#     if angka == 3:
#         pass #ini tidak akan di eksekusi
#     print(angka)

# continue
angka = 0
print(f"angka sekarang -> {angka}")

while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}") #aksi 1

    if angka == 3:
        print("hi") 
        continue #ini akan membuat loop meloncat ke step selanjutnya
    print("hallo") #aksi 2

print("akhir program")
