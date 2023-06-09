'''fungsi dengan kembalian'''

# template fungsi dengan kembalian
'''
def nama_fungsi(argument):
    badan fungsi
    return output
'''

# fungsi kuadrat 
def kuadrat(input_angka):
    '''fungsi kuadrat'''
    output_kuadrat = input_angka**2
    return output_kuadrat
    
y = kuadrat(3)
print(y)
z = 10 + kuadrat(8)
print(z, "\n")

# fungsi tambah 
def fungsi_tambah(angka1,angka2):
    '''fungsi return dengan multi input'''
    return angka1 + angka2

a = fungsi_tambah(18,29)
print(a, '\n')

# fungsi dengan return/output banyak
def operasi_aritmatika(angka1,angka2):
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2

    return tambah, kurang, kali, bagi

i,j,k,l = operasi_aritmatika(10,12)

print(f"hasil tambah = {i}")
print(f"hasil kurang = {j}")
print(f"hasil kali = {k}")
print(f"hasil bagi = {l}")
