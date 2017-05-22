def Debug(*args):
    r = ""
    for i in args:
        if r == "":
            r = str(i)
        else:
            r = r + "   " + str(i)
    print(r, file=sys.stderr)


import sys
import math
from struct import unpack

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)




#x = ''.join(format(ord(x), 'b') for x in message)
x = ""
for i in message:
    v = format(ord(i), 'b')
    if len(v) < 7:
        v = ((7 - len(v)) * '0') + v
    x += v

outText = ""

def Encode(last, r):
    v = ""
    if (last == "1"):
        v = "0"
    if (last == "0"):
        v = "00"
    result = v + " " + ((r)*"0")
    return result

Debug(message, x)
last = -1
r = 0



for i in range(len(x)):
    if x[i] != last:
        if (last != -1):
            #Debug("Encoding", r, last)
            outText += Encode(last,r)
            outText += " "
        last = x[i]
        r = 0
    r += 1

outText += Encode(last, r)

Debug(outText)
print(outText)
