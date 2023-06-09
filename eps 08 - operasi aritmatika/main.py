# operasi aritmatika

a = 10
b = 3

# operasi penjumlahan +
hasil = a + b
print (a , '+', b, '=',hasil)

# operasi pengurangan -
hasil = a - b
print (a , '-', b, '=',hasil)

# operasi perkalian *
hasil = a * b
print (a , '*', b, '=',hasil)

# operasi pembagian /  
hasil = a / b
print (a , '/', b, '=',hasil)

# operasi eksponen (berpangkat) **  
hasil = a ** b
print (a , '**', b, '=',hasil)

# operasi modulus (sisa bagi) %
hasil = a % b
print (a , '%', b, '=',hasil)

# operasi floor division // (kebalikannya dari modulus)(hasil bagi jika nilainya float, maka akan dikonversi ke type data int)
hasil = a // b
print (a , '//', b, '=',hasil)

# prioritas operasi, operational precedence(urutannya : eksponen-perkalian-penjumlahan)
x = 3
y = 2
z = 4

hasil = x ** y * z + y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//', x,'=', hasil) 

hasil = x + y * z
print(x,'+',y,'*',z,'=',hasil)

hasil = (x + y) * z #operasi yang didalam kurung akan dikerjakan terlebih dahulu
print(x,'+',y,'*',z,'=',hasil)

'''
    urutan operasi aritmatika :
    1. ()
    2. eksponen
    3. perkalian bersamam teman-temannya (* / ** % //)
    4. penjumlahan dan pengurangan
'''