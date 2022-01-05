# flag = something

import string

base = string.ascii_letters + string.punctuation
trans = base[13:] + base[:13]

ciphertext = flag.translate(str.maketrans(base, trans))
# ciphertext = P'SVAsBpBzzjp1CurEFhnE3hCErGGLhsHAl
