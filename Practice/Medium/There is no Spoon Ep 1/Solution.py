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

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
Debug(width, height)



#for w in range(width):
#    for h in range(height):
#        Debug(w, h)


ar = []

#Populate Array Lists
for h in range(height):

    line = input()  # width characters, each either 0 or .
    a = []
    for i in range(len(line)):
        a.append(line[i])
        #Debug("G:", line[i])
    #Debug("o: ", a)
    ar += [a]
    #ar.append[(a)]

    Debug(line)
#Debug(ar[1])



for y in range(len(ar)):
    for x in range(len(ar[y])):
        if ar[y][x] != '.':
            pos = str(x) + ' ' + str(y)
            right = '-1 -1'
            down = '-1 -1'

            #Get Next Right value Value
            for i in range(x+1, len(ar[y])):
                if ar[y][i] != '.':
                    right = str(i) + ' ' + str(y)
                    break

            #Calculate Down
            for i in range(y+1, len(ar)):
                if ar[i][x] != '.':
                    down = str(x) + ' ' + str(i)
                    break
            print(pos + ' ' + right + ' ' + down)
