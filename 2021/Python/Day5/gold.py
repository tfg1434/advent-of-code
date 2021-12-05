import os
import math
import numpy as np
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "in.txt")) as file:
    lines = file.read().splitlines()

def processLine(line):
    l = line.split(" -> ")

    return list(map(lambda s: list(map(int, s.split(","))), l))

lineSegs = list(map(processLine, lines))

print(lineSegs)

def covering(x, y):
    count = 0
    for seg in lineSegs:
        fr = seg[0]
        to = seg[1]
        isH = fr[1] == to[1]
        isV = fr[0] == to[0]

        if isH:
            count += 1 if (fr[0] <= x <= to[0] or to[0] <= x <= fr[0]) and y == fr[1] else 0
        elif isV:
            count += 1 if (fr[1] <= y <= to[1] or to[1] <= y <= fr[1]) and x == fr[0] else 0

    return count

# grid = np.full(shape=(1000, 1000), fill_value=0, dtype=int)

ans = 0

for x in range(1000):
    if (x % 100) == 0:
        print(x)

    for y in range(1000):
        if (covering(x, y) >= 2):
            ans += 1

print(ans)

