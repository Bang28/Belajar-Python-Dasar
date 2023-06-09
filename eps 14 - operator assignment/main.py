# operasi yang dapat dilakukan dengan penyingkatan
# operasi ditambah dengan assignment
# contoh :

# operasi aritmatika

a = 5 #ini adalah assignment
print("nilai a =", a)

# contoh penulisan yg dipersingkat
a += 1 #artinya adalah a = a + 1
print("nilai a +=1 adalah", a)

a -= 2 #artinya adalah a = a - 2
print("nilai a -=2 adalah", a)

a *= 5 #artinya adalah a = a * 5
print("nilai a *=5 adalah", a)

a /= 2 #artinya adalah a = a / 2
print("nilai a /=2 adalah", a)

b = 10
print("\n nilai b =", b)
# modulus dan floor division
b %=3 #artinya modulus/sisa bagi 3 dari 10
print("nilai b %=3 adalah", b)
# floor deivision
b //=3 #membulatkan hasil bagi dari bentuh float menjadi bentuk desimal
print("nilai b //=3 adalah", b)

# pangkat atau eksponen
a = 5
print("nilai a =", a)
a **= 3 #artinya nilai pada object a dipangkatkan 3 (5^3=125)
print("nilai a **= 3 adalah ", a)


# operasi bitwise

# contoh OR
c = True
print("\n nilai c =", c)
c |= False
print("nilai c |= false adalah ", c)
c = False
print("nilai c =", c)
c |= False
print("nilai c |= false adalah ", c)

# contoh AND
c = True
print("\n nilai c =", c)
c &= False
print("nilai c &= false adalah ", c)
c = True
print("nilai c =", c)
c &= True
print("nilai c &= false adalah ", c)

# contoh XOR
c = True
print("\n nilai c =", c)
c ^= False
print("nilai c ^= false adalah ", c)
c = True
print("nilai c =", c)
c ^= True
print("nilai c ^= false adalah ", c)

# contoh geser geser (right>> dan lift<<)
d = 0b0100
print("\n nilai d =", format(d,'04b'))
d >>= 2
print("nilai d >>= 2 adalah ", format(d,'04b'))
d <<= 1
print("nilai d <<= 1 adalah ", format(d,'04b'))
