

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
m = sorted([ int(input()) for i in range(n) ])

r = None
for i in range(1, len(m)):
    v = abs(m[i] - m[i-1])
    if r == None:
        r = v
        pass
    if r > v:
        r = v
print(r)
