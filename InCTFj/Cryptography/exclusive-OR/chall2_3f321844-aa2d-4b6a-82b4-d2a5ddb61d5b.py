from pwn import xor
from random import randint
from secret import pt

pt2 = []
for i in range(0, len(pt), 16):
    pt2.append(pt[i : i + 16].encode())
pt=pt2
ct = ''
for i in range(len(pt)):
    ct+=(xor(pt[i],chr(randint(0, 256)).encode())).hex()

with open('output.txt', 'w') as f:
    f.write(ct)