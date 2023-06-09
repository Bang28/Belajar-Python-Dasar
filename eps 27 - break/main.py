# break 

angka = 0

while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}")

    if angka == 3:
        print("hi")
        break #ini akan membuat loop selesai disini

    print("hallo")

print("akhir program")


data_int = int(input("hitung sampai : "))
angka = 0

while True:
    angka += 1
    print(f"angka sekarang -> {angka}")

    if angka == data_int:
        print("hi")
        break #ini akan membuat loop selesai disini

    print("hallo")

print("akhir program")