# 1. cara membuat string
# string adalah kumpulan karakter bisa angka dan huruf

data = "ini adalah string"
print(data)
print(type(data)) #untuk melihat type data pada object tersebut

# 1. cara membuat string
'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote
'''

data = 'menggunakan single quote'
print(data)

data = "menggunakan double quote"
print(data)

# 2. cara membuat string menggunakan tanda \ (backlash)
# membuat tanda single quote agar terbaca sebagai string
print('ini hari jum\'at') #dengan menambahkan tanda \, single quote ditengah akan dibaca sebagai string

# membuat backlash agar terbaca sebagai string
print("C:\\user\\ruri")

# cara membuat perintah tab pada sebuat string
print("ucup\t olong, jadi jauhan") #\t akan berfungsi sebagai tab

# memasukan perintah backspase pada string
print("ucup \botong, jadi gandengan") #\b berfungsi sebagai backspace

# newline
print("baris pertama. \nbaris kedua.") #LF -> Line Feed
print("baris petama. \rbaris kedua.") #CR -> Carriage return
print("baris petama. \r\nbaris kedua.") #CRLF -> Line feed Carriage return 
# perbedaan CRLF, CR, LF -> hanya pada penggunaan OS di laptop saja, bisa diliat langsung pada VSCODE di bagian pojok kanan bawah

# 3. bikin string literal atau raw
# hati-hati
print('C:\new folder') #hasilnya akan salah, cara mengatasinya menggunakan raw string 
print(r'C:\xampp\htdocs\dashboard') #dengan menambahkan r didepan, semua yg ada di dalam single quote akan diangap raw string

# multiline
print("""
Nama :
NIM :
Kelas :
""")

# menggabungkan literal string dan raw sekaligus
print(r"""
Nama : Masruri
NIM : 42420022
Semester : 6 univperadaban\membangun peradaban dunia
Website : www.ruri.com/newID
""")
