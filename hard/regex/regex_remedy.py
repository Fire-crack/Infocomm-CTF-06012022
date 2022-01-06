# Here, we will be delving into the world of RegEx (Regular Expressions)
# Regex is primarily used for detecting matches in a string
# Here, we will be detecting links within the source code of an html page.
# 
# Specifically, we will be looking at a wikipedia page.
# 
# Links are typically in the form of <href="link">
# 
# Links would either start with "http://", "https://", or "/wiki"
# 
# An example of a link would be "/wiki/Never_Gonna_Give_You_Up", or "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
# 
# Of course the regular expression written would be in an html page, which would look something like
# <href="/wiki/Never_Gonna_Give_You_Up">
# <href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">
# 
# The regex written below seems to have a flaw in it, fix it, and run the code to get the flag.
# 
# Here's a tutorial if you want to learn about regex from scratch: https://regexone.com
# Here's a nice debugger to play around with: https://regex101.com/r/D9Q1ef/1

import re

pattern = re.compile(r'''
    (?<=
        href="      # here, we find all strings that start with href="
    )

    (?:
        https?:\/\/ # here, we check if the strings start with http:// or https://
        |           # or, 
        \/wiki      # starts with /wiki
    )
    .+              # we match all other characters after, until
    (?=")           # we find a "
    '''
, re.X)


# open the file with the source code for the rickroll file
# do let izo know if you have trouble reading the file
s = open("rickroll.html", "r", encoding="utf-8").read()

# you don't need to change anything below this
from base64 import b64decode as bd
exec(bd("cmVzID0gcGF0dGVybi5maW5kYWxsKHMpCnBhcnQxID0gWyg2NzMsIDYpLCAoNjQ2LCA2KSwgKDUwMCwgNiksICgyODYsIDYxKSwgKDQwNSwgMzYpLCAoMzUwLCA3KSwgKDY5NiwgNyksICg2LCAxMyksICg1MDUsIDI1KSwgKDI3NCwgMjQpLCAoMTEyLCAxNyldCnBhcnQyID0gWyg2MjAsIDEwKSwgKDIzOCwgOCksICgxMTIsIDE5KSwgKDMzNywgMjMpLCAoNzM4LCAyMSksICg4LCAxMCksICg0NjgsIDIpLCAoNzQ4LCAyNiksICg3MjYsIDE0KSwgKDgwOCwgNyksICgyNzksIDIzKSwgKDY3LCAxMSksICgzNiwgMTApLCAoNzc5LCAxMyksICgxNjksIDEwMCksICg0MDMsIDEzKSwgKDQ5OSwgMTkpLCAoNjIwLCAxMSksICg2NTgsIDE2KSwgKDIyMCwgMjApLCAoMzc0LCAxNCksICg1ODEsIDE0KSwgKDcwLCA5KSwgKDI2MSwgMzApLCAoNzU3LCA2MSksICgzODIsIDEwKSwgKDE2OSwgMTAyKV0KZmxhZyA9ICIiLmpvaW4obWFwKGxhbWJkYSB0OiByZXNbdFswXSVsZW4ocmVzKV1bdFsxXSVsZW4ocmVzW3RbMF0lbGVuKHJlcyldKV0sIHBhcnQxKSkrInsiKyIiLmpvaW4obWFwKGxhbWJkYSB0OiByZXNbdFswXSVsZW4ocmVzKV1bdFsxXSVsZW4ocmVzW3RbMF0lbGVuKHJlcyldKV0sIHBhcnQyKSkrIn0iCnByaW50KGYiVGhlIGZsYWcgaXM6IHtmbGFnfSIp"))
