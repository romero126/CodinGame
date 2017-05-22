
import sys
import math
import os
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.

mime = {}
for i in range(n):
    f = input().split()
    mime['.' + f[0].lower()] = f[1]

for i in range(q):
    file = input().lower()
    ext = os.path.splitext(" " + file)[1]
    try:
        x = mime[ext]
    except:
        x = "UNKNOWN"
    print(x)
