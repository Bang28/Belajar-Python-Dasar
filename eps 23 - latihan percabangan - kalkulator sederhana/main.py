# latihan 
# kalkulator sederhana

print(9*"="+"Kalkulator Sederhana"+9*"=")

angka_1 = float(input("masukan angka pertama : "))
operator = input("masukan operator(+,-,*,/) : ")
angka_2 = float(input("masukan angka kedua : "))

# percabangannya
if operator == "+":
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah = {hasil}")
elif operator =="-":
    hasil = angka_1 - angka_2
    print(f"hasilnya adalah = {hasil}")
elif operator == "*" or operator == "x":
    hasil = angka_1 * angka_2
    print(f"hasilnya adalah = {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"hasilnya adalah = {hasil}")
else:
    print("masukan ada salah!")
print("akhir program")

