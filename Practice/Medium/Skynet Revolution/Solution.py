import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]


def bfs(m, s, g):
    q = [(s, [s])]
    while q:
        (v, p) = q.pop(0)
        for next in m[v] - set(p):
            if next == g:
                return p + [next]
            else:
                q.append((next,p + [next]))


m = {}
for i in range(l):
    n1, n2 = [int(j) for j in input().split()]
    try:
        m[n1].add(n2)
    except:
        m[n1] = set()
        m[n1].add(n2)
    try:
        m[n2].add(n1)
    except:
        m[n2] = set()
        m[n2].add(n1)




gw = []
for i in range(e):
    ei = int(input())  # the index of a gateway node
    gw.append(ei)


# game loop
while True:
    e = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    s = None
    for i in gw:
        x = bfs(m, e, i)
        if s == None:
            s = x
        if len(s) > len(x):
            s = x
    print(str(s[0]) + " " + str(s[1]))
