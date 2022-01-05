# flag = something
from random import choice

b = [bin, hex, oct]
cipherlist = []

for c in flag:
    cipherlist.append( choice(b)(ord(c)) )

# cipherlist = ['0o103', '0b1010100', '0x46', '0b1001001', '0b1101110', '0o146', '0b1101111', '0o143', '0x6f', '0b1101101', '0b1101101', '0b1111011', '0x64', '0x31', '0b1100110', '0b1100110', '0x65', '0x72', '0x33', '0b1101110', '0b1110100', '0x5f', '0b1100010', '0b1100001', '0x73', '0o63', '0o163', '0o137', '0b1110111', '0b1101000', '0b1101111', '0x61', '0o41', '0o175']
