import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.



# w: width of the building.
# h: height of the building.

w, h = [int(i) for i in input().split()]

n = int(input())  # maximum numberof turns before game over.
pos = [int(i) for i in input().split()]
grid = [0,0,w,h]
# game loop

cases = [
    #Case, gridindex, posindex, increment
    ["R", 0, 0, 1],
    ["D", 1, 1, 1],
    ["L", 2, 0, -1],
    ["U", 3, 1, -1]
]
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    #Runtestcases
    for i in cases:
        if i[0] in bomb_dir:
            grid[i[1]] = pos[i[2]] + i[3]
            #I can shrink this more

    x, y, w, h = grid
    x = x + (w - x) / 2
    y = y + (h - y) / 2
    x, y = int(x), int(y)
    pos = [x,y]
    print(x, y)
