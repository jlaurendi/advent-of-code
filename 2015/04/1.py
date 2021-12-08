from hashlib import md5
from sys import exit

p_in = 'yzbqklnj'
# p_in = 'abcdef'
i = 1
while True:
    txt = p_in + str(i)
    hsh = md5(txt.encode('utf-8')).hexdigest()
    if hsh[0:6] == '000000':
        print(i)
        exit()
    i += 1