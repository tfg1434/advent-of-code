from functools import *
import os
import math
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "in.txt")) as file:
    lines = file.readlines()

sum = 0
sum = reduce(lambda acc, s: acc + math.floor(int(s) / 3 - 2), lines, 0)

print(sum)

