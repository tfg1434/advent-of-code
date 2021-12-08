from functools import *
import os
import math
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "in.txt")) as file:
    lines = file.readlines()

def calcRec(x):
    fuel = max(0, math.floor(x / 3 - 2))

    while x > 0:
        return fuel + calcRec(fuel)

    return x

sum = 0
sum = reduce(lambda acc, s: acc + calcRec(int(s)), lines, 0)

print(sum)

