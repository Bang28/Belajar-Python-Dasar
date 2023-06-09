# looping dictionary

teman_teman = {
    "cp":"cecep panjul",
    "it":"ikhsan tambayong",
    "ui":"upin ipin",
    "tudal":"tuk dalang",
    "ros":"kak ros"
}

# looping first try (yang keluar adalah key nya)
for teman in teman_teman:
    print(teman)

# operator untuk mengambil item/iterables
keys = teman_teman.keys()
print(keys)

for key in teman_teman.keys(): #iterables (mengambil key nya saja)
    print(teman_teman.get(key))

values = teman_teman.values() #iterables
print(values)

for value in teman_teman.values(): #iterables (mengambil value nya saja)
    print(value)

items = teman_teman.items() 
print(items)

for item in teman_teman.items(): #item (mengambil berpasangan (key + value))
    print(item)
for key,value in teman_teman.items(): #mengambil terpisah antar key & item
    print(f"key = {key}, value = {value}")



