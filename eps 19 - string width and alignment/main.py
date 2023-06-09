# witdh and multiline

# data
data_nama = "ucup surucup"
data_umur = 22
data_tinggi = 165.3
data_nomor_sepatu = 41

# string standard
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, nomor sepatu = {data_nomor_sepatu}"
print(5*"="+"Data String"+5*"=")
print(data_string)

# string multiline (dengan menggunakan enter/newline(\n))
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nnomor sepatu = {data_nomor_sepatu}"
print("\n"+5*"="+"Data String Multiline"+5*"=")
print(data_string)

# string multiline dengan kutip triplets
data_string = f"""nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
nomor sepatu = {data_umur}
"""
print("\n"+5*"="+"Data String Multiline 2"+5*"=")
print(data_string)

# mengatur lebar
data_nama = "ucup"
data_string = f"""
nama   = {data_nama:>5}
umur   = {data_umur:>5}
tinggi = {data_tinggi:>5}
sepatu = {data_umur:>5}
"""
print("\n"+5*"="+"Mengatur Lebar"+5*"=")
print(data_string)



