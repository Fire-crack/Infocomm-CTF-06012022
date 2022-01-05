from textwrap import wrap

# flag = something

def hex_to_rgb(hexcode):
    # hexcode is a string
    return [int(hexcode[i:i+2], 16) for i in range(0, 6, 2)]

string = ""
for char in flag:
    string += str(ord(char))

cipherlist = []

for hexcode in wrap(string, 6):
    result = hex_to_rgb(hexcode)
    cipherlist.append(result)

# cipherlist = [[103, 132, 112], [115, 17, 1], [2, 17, 25], [145, 17, 16], [145, 9, 18], [49, 25, 151], [73, 17, 105], [89, 121, 81], [9, 73, 17], [1, 23, 17], [101, 20, 100], [100, 97, 22], [16, 65, 1], [83, 16, 25], [89, 113, 20], [81, 17, 5], [89, 89, 148], [129, 8, 72], [17, 113, 20], [17, 81, 37]]
