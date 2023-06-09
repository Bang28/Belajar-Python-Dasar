# copy dictionary 

teman_teman = {
    "cp":"cecep panjul",
    "it":"ikhsan tambayong",
    "ui":"upin ipin",
    "tudal":"tuk dalang",
    "ros":"kak ros"
}

friends = teman_teman.copy()

print(f"teman-teman : {teman_teman}")
print(f"friends : {friends}\n")

teman_teman["cp"]="contak person"
print(f"teman-teman : {teman_teman}")
print(f"friends : {friends}\n")

# pop dictionary (diambil berdasarkan key)
dataIt = friends.pop("it") #data pada friends dgn key "it" akan ditranfer ke dataIt dengan posisi yang dinaikan
print(f"data It : {dataIt}")
print(f"friends : {friends}\n")

# popitem dictionary (diambil berpasanan key + value (yg terakhir aj))
dataTerakhir = friends.popitem()#kita akan mengambil data terakhir pd variable friends
print(f"data terakhir : {dataTerakhir}")
print(f"friends : {friends}\n")
