import random
import string

def random_string(panjang:int)->str:
    '''fungsi membuat primary key secara acak dgn panjang karakter 6 digit'''
    hasil_string = ''.join(random.choice(string.ascii_letters) for i in range(panjang))
    return hasil_string