import sys
import math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.




lon = float(input().replace(',', '.'))
lat = float(input().replace(',', '.'))

pos = lat+lon

n = int(input())


fib = []
for i in range(n):
    defib = input().split(';')
    #Number, Name, Address, Contact Phone Number (degrees), Longitutde (Degrees), Latitude (degrees),
    fib.append(defib)


closest = None

for i in fib:
    flon = float(i[4].replace(',', '.'))
    flat = float(i[5].replace(',', '.'))
    if flon == lon:
        if flat == lat:
            dist = 0
            i.append(dist)
            pass
    #maths
    x = (flon - lon) * math.cos( (lat + flat) / 2 )
    y = (flat - lat)
    dist = math.sqrt((x ** 2) + (y ** 2) ) * 6371
    #Add to
    i.append(dist)

#Sort
fib = sorted(fib, key=lambda x: x[6] )
#Win
print(fib[0][1])
