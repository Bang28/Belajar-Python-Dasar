# latihan logika dan komparasi
# akan membuat gabungan area rentang dari angka

# misal +++++3-----------10++++++++++
inputUser = float(input("masukan angka yang bernilai \n kurang dari 3 \n atau \n lebih besar dari 10 \n :"))

# +++++++3------------
# memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("kurang dari 3 = ",isKurangDari)

# ------------10+++++++
# memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("lebih dari 10 = ",isLebihDari)

# menggabungkan dua are
# ++++++3-----------10++++++++++
isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukan : ", isCorrect)
print("\n", 10*"=", "\n")

# -----3+++++++10------
# merupakan sebuah kasus irisan 
inputUser = float(input("masukan angka yang bernilai \n lebih dari 3 \n dan \n kurang dari 10 \n :"))

# -----3++++++
# lebih dari 3
isLebihDari = inputUser > 3
print("lebih dari 3 = ", isLebihDari)

# ++++++10------
# kurang dari 10
isKurangDari = inputUser < 10
print("kurang dari 10 = ", isKurangDari)

isCorrect = isKurangDari and isLebihDari
print("angka yang anda masukan : ", isCorrect)

# ------0++++++5------8++++++11--------
inputUser = float(input("masukan angka yg bernilai \n lebih dari 0 \n kurang dari 5 \n lebih dari 8 \n kurang dari 11"))
# ------0++++++
# lebih dari 0
isLebihDari = inputUser > 0
print("lebih dari 0 = ", isLebihDari)

# ++++++5------
# kurang dari 5
isKurangDari = inputUser > 5
print("kurang dari 5 = ",isKurangDari)

# ------8++++++
# lebih dari 8
isLebihDari = inputUser > 8
print("lebih besar dari = ", isLebihDari)

# ++++++11------
# kurang dari 11
isKurangDari = inputUser > 11
print("kurang dari 11 = ", isKurangDari)

# +++++0------5++++++8------11++++++
inputUser = Float(input("masukan angka yg bernilai \n kurang dari 0 \n lebih dari 5 \n kurang dari 8 \n lebih dari 11"))
# +++++0-----
# kurang dari 0
isKurangDari = inputUser < 0
print("kurang dari 0 = ", isKurangDari)

# ------5+++++++
# lebih dari 5
isLebihDari = inputUser > 5
print("lebih dari 5 = ",isLebihDari)

# +++++8-------
# kurang dari 8
isKurangDari = inputUser > 8
print("kurang dari 8 = ",isKurangDari)

# ------11++++++
# lebih dari 11
isLebihDari = inputUser > 11
print("lebih dari 11 = ", isLebihDari)