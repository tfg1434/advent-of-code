from functools import *
import os
import math
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "in.txt")) as file:
    lines = file.readlines()
    path1 = lines[0].split(',')
    path2 = lines[1].split(',')

def manDist(pos):
    return abs(pos[0]) + abs(pos[1])

def populateSet(path):
    ret = set()
    pos = (0, 0)

    for instr in path:
        dir = instr[0]
        count = int(instr[1:])

        for _ in range(count):
            if (dir == "U"):
                pos = (pos[0], pos[1] - 1)
            elif (dir == "R"):
                pos = (pos[0] + 1, pos[1])
            elif (dir == "D"):
                pos = (pos[0], pos[1] + 1)
            elif (dir == "L"):
                pos = (pos[0] - 1, pos[1])

            ret.add(pos)

    return ret
    
set1 = populateSet(path1)
set2 = populateSet(path2)

intersections = set1 & set2
ans = map(manDist, intersections)
print(min(ans))






