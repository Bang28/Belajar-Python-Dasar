'''type hints untuk fungsi'''

# bentuk standard fungsi yang sudah kita pelajari

# ini adalah studi kasus :
'''
def fungsi (parameter):
    hasil = parameter ** 2
    print(hasil)
    
fungsi(1)
fungsi("ucup")
fungsi(True)
'''
import string

# ini adalah penggunaan type hints untuk nanti sharing program ke temen
def fungsi_dgn_hints(argument:int) -> int: #artinya nilai masuk kan keluarnya harus INT
    '''fungsi dengan hints'''
    output = 10 ** argument
    return output

HASIL = fungsi_dgn_hints(2)
print(HASIL)

def display(argument:string):
    print(argument)

display("ucup")

