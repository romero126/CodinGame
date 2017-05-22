import sys
import math


l = int(input())
h = int(input())
t = input().upper()
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?"

for x in range(h):
    r = input()
    o = ""
    for i in range(len(t)):

        f = abc.find(t[i])
        if f == -1:
            f = 26
        p = l * f
        o += r[p:(p+l)]
    print(o)
