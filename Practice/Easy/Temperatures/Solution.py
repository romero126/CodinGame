import sys
import math



def Debug(obj):
    r = ""
    for i in obj:
        if r == "":
            r = str(i)
        else:
            r = r + ",  "+ str(i)
    print(r, file=sys.stderr)

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
n = int(input())

if n == 0:
    temps = [0]
else:

    temps = [int(i) for i in input().split(' ')]  # the n temperatures expressed as integers ranging from -273 to 5526




# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


Debug(["Value starts here", n])

Debug(["My Value", temps])

dist = abs(temps[0])
value = temps[0]
for i in temps:
    if i == abs(value):
        value = i

    if abs(i) < abs(value):
        dist = abs(i)
        value = i
Debug([value, dist])
print(value)
#print("result")
