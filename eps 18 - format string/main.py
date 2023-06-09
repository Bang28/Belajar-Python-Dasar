# format string
# contoh generic
# string
nama = "ruri"
format_str = f"hello {nama}"
print(format_str)

# boolean
boolean = True
format_str = f"boolean {boolean}"
print(format_str)

# angka
angka = 2005.5
format_str = f"angka {angka}"
print(format_str)

# bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# bilangan dengan ordo ribuan
angka = 200000
format_str = f"bilangan bulat = {angka:,}" #untuk mempermudah mengenali angka ribuan gtu aj dah/membuat format angka ribuan
print(format_str)

# bilangan desimal
angka = 2005.54321
format_str = f"angka {angka:.2f}" #untuk mengambil 2 digit angka dibelajang koma
print(format_str)

# menampilkan leading zero 
angka = 2005.54321
format_str = f"angka {angka:8.2f}" 
print(format_str)

# menampilkan tanda plus atau minus
angka_minus = -10
angka_plus = 10
formar_minus = f"minus = {angka_minus:+}" #pada nilai yg minus, ini sebenernya tidak akan begitu berpengaruh
formar_plus = f"plus = {angka_plus:+d}"
print(formar_minus)
print(formar_plus)

# memformat persen
persentase = 0.045
format_persen = f"persen {persentase:.2%}" #mengambil 2 digit dibelakang koma, lalu memformatnya dalam bentuk persen
print(format_persen)

# melakukan operasi aritmatika didalam placeholder
harga = 10000
jumlah = 5
format_string = f"jumlah total = Rp {harga*jumlah:,}"
print(format_string)

# format angka lain (binary, octal, hexadecimal)
angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hexa = f"hexadecimal = {hex(angka)}"
print(format_binary)
print(format_octal)
print(format_hexa)
