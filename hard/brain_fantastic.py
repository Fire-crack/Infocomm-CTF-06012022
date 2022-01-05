# welcome to brainfuck!
# 
# you will be creating a interpreter for this language, with a few modifications
# 
# brainfuck is a simple language to learn, with simple syntax
# it operates on an infinite grid of squares, with integers in them
# 
# 
# the code just manipulates an "arrow" (known as a pointer) on the infinite grid of integers
# 
# 
# 
# ------------------------------------
# |  0 |  0 |  0 |  0 |  0 |  0 |  0 |
# ------------------------------------
#        /\
#        |
#        |
#        |
#        |
# 
# 
# the instruction ">", moves the arrow one grid to the right
# 
# ------------------------------------
# |  0 |  0 |  0 |  0 |  0 |  0 |  0 |
# ------------------------------------
#             /\
#             |
#             |
#             |
#             |
# 
# likewise, the instruction "<", moves the arrow one grid to the left
# 
# ------------------------------------
# |  0 |  0 |  0 |  0 |  0 |  0 |  0 |
# ------------------------------------
#        /\
#        |
#        |
#        |
#        |
# 
# 
# now it's back to where it was!
# 
# the instruction "+", adds 1 to the current grid its pointing at
# 
# 
# ------------------------------------
# |  0 |  1 |  0 |  0 |  0 |  0 |  0 |
# ------------------------------------
#        /\
#        |
#        |
#        |
#        |
# 
# 
# similarly, the instruction "-", deducts 1 to the current grid it's pointing at, allowing it to go to negative numbers
# 
# 
# so that's four instructions you've learnt already, +-><
# 
# now we're going to add another concept, called loops.
# 
# the "[" and "]" instruction tells it to continue executing instructions in between the pair of brackets,
# until the grid it's pointing at is -1
# 
# example:
# 
# current grids:
# 
# ------------------------------------
# |  0 |  0 |  0 | -1 |  0 |  0 |  0 |
# ------------------------------------
#        /\
#        |
#        |
#        |
#        |
# 
# 
# code: [>]
# 
# ending result:
# 
# 
# ------------------------------------
# |  0 |  0 |  0 | -1 |  0 |  0 |  0 |
# ------------------------------------
#                 /\
#                 |
#                 |
#                 |
#                 |
# 
# "[": the loop is started.  ←---------------------
# ">": the arrow moves to the right                |
#  "]" the current grid's value is checked,        |
# if it is -1, the loop is broken out off.         |
# else, restart the loop  -------------------------→
# 
# 
# next up, we have the "." instruction, 
# this just prints out the character associated with the ascii value
# for example,
# 
# ------------------------------------
# |  0 |  0 |  0 | 69 |  0 |  0 |  0 |
# ------------------------------------
#                 /\
#                 |
#                 |
#                 |
#                 |
# 
# "." will print out "E"
# 
# 
# 
# here's a sample code of modified brainfuck that prints out "hi"
# code = +[>+++++<-]>[+++[>+++++<-]]+++++++[>+++++<-]>-.+.
# 
# 
# THAT'S why it's called brainfuck :D
# 
# 
# 
# for the last instruction i'm gonna be adding,
# it's a memory instruction
# 
# 
# the instruction "^" will either remember what the current grid is,
# or paste what it remembers onto the grid
# 
# ------------------------------------
# |  0 |  0 |  0 | -1 |  0 |  0 |  0 |
# ------------------------------------
#                 /\
#                 |
#                 |
#                 |
#                 |
# 
# running "^" on a non-zero grid will cause it to remember the number, which in this case is -1
# if it's pointing to another number that has a value 0, it would paste out
# the number it remembered
# 
# do take note that the memory can change as well,
# as you can run "^" on another grid, let's say of value 2, that will cause it to change its memory
# 
# 
# 
# here's the same sample code that prints "hi", but with the memory instruction
# 
# code = +[>+++++<-]>-^>^<[>>++[<+++++>-]<<-]>----------.+.
# 
# 
# 
# here's the code that prints out the flag:
# 
# code = ++++^[>+++++<-]>[<+++>-]+^[<-->-]<.>+^>^[<[<+>-]+^>-]<[<-->-]<++.<^[>--<-]>----.+++.>+^>+^[<[<+++>-]++^>-]<<--.^<++++[>--<-]>.<+^+.>---.<.--..<<++^>^<[>[>++<-]+^<-]>>----.>-.<<+++[>--<-]>+++.>-.<<+++[>--<-]>---.+++++.<+++[>--<-]>--.>--.<+++.<+++[>++<-]>++++.>.<<+++[>--<-]+++[>--<-]>-.<+++++[>+++<-]>.<+++[>--<-]>-.>.++.<-.----.<+++[>++<-]>+++.<+++[>---<-]>.<+^++^[>++<-]>+.<+^[>--<-]+^[>-<-]>.<+^+[>++++<-]>.
