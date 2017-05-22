import sys
import math

w, h = [int(i) for i in input().split()]
grid = []
for i in range(h):
    v = [int(i) for i in input().split()]
    grid.append(v)

ex = int(input())  # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).

def path(p, x, y):
    if p == 'DOWN':
        print(x, y+1)
    elif p == 'LEFT':
        print(x-1, y)
    elif p == 'RIGHT':
        print(x+1, y)

rooms = {
    1: ['DOWN', 'DOWN', 'DOWN'],
    2: [None,'RIGHT','LEFT'],
    3: ['DOWN',None, None],
    4: ['LEFT',None,'DOWN'],
    5: ['RIGHT','DOWN',None],
    6: [-1, 'RIGHT', 'LEFT'],
    7: ['DOWN', None, 'DOWN'],
    8: [None, 'DOWN', 'DOWN'],
    9: ['DOWN', 'DOWN', None],
    10: ['LEFT', None, None],
    11: ['RIGHT', None, None],
    12: [None, None, 'DOWN'],
    13: [None, 'DOWN', None],
}

while True:
    xi, yi, pos = input().split()
    xi = int(xi)
    yi = int(yi)

    room = grid[yi][xi]
    r = rooms[room]
    if pos == 'TOP':
        path(r[0], xi, yi)
    elif pos == 'LEFT':
        path(r[1], xi, yi)
    elif pos == 'RIGHT':
        path(r[2], xi, yi)
