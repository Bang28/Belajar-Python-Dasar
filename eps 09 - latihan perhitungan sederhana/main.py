# latihan operasi aritmatika

print("\n Pogram Konversi Temperature\n")
# program konversi celcius ke satuan lain
print("=======program konversi celcius ke satuan lain========")

celcius = float(input('masukkan suhu dalam celcius :'))
print('suhu adalah :', celcius, 'celcius')

# reamur ((4/5) * c)
reamur = (4 / 5) * celcius
print ("suhu dalam reamur adalah :", reamur, "reamur")

# fahrenheit ((9/5) * celcius + 32)
fahrenheit = ((9/5) * celcius + 32)
print ("suhu dalam fahrenheit adalah :", fahrenheit, "fahreinheit")

# kelvin (celcius + 273)
kelvin = celcius + 273
print ("suhu dalam kelvin adalah :", kelvin, "kelvin")

# program konversi reamur ke satuan lain
print("=======program konversi reamur ke satuan lain========")
reamur = float(input("masukan suhu dalam reamur :"))
print("suhu adalah :", reamur, "reamur")

# celcius ((5/4)*reamur)
celcius = (5/4) * reamur
print("suhu dalam celcius adalah :", celcius, "celcius")

# fahrenheit ((9/4)*reamur+32)
fahrenheit = (9/4) * reamur + 32
print("suhu dalam fahrenheit adalah :", fahrenheit, "fahrenheit")

# kelvin ((5/4)*reamur+273)
kelvin = (5/4) * reamur + 273
print("suhu dalam kelvin adalah :", kelvin, "kelvin")

# program konversi fahrenheit ke satuan lain
print("=======program konversi fahrenheit ke satuan lain========")
fahrenheit = float(input("masukan suhu dalam fahrenheit :"))
print("suhu dalam fahrenheit adalah :", fahrenheit)

# celcius (5/9*(fahrenheit-32))
celcius = 5/9 * (fahrenheit - 32)
print("suhu dalam celcius adalah :", celcius, "celcius")

# reamur (4/9*(fahrenheit-32))
reamur = 4/9 * (fahrenheit - 32)
print("suhu dalam reamur adalah :", reamur, "reamur")

# kelvin (5/9*(fahrenheit+459))
kelvin = 5/9 * (fahrenheit + 459)
print("suhu dalam kelvin adalah :", kelvin, "kelvin")

# program konversi kelvin ke satuan lain
print("=======program konversi kelvin ke satuan lain========")
kelvin = float(input("masukan suhu dalam kelvin :"))
print("suhu dalam kelvin adalah :", kelvin, "kelvin")

# celcius (kelvin - 273)
celcius = kelvin - 273
print("suhu dalam celcius adalah :", celcius, "celcius")

# reamur (4/5 (kelvin - 273))
reamur = 4/5 * (kelvin - 273)
print("suhu dalam reamur adalah :", reamur, "reamur")

# fahrenheit ((9/5 * kelvin) - 459)
fahrenheit = (9/5 * kelvin) - 459
print ("suhu dalam fahrenheit adalah :", fahrenheit, "fahrenheit")