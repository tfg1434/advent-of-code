import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "in.txt")) as file:
    lines = file.read().splitlines()

gamma = ""
epsilon = ""

for x in range(len(lines[0])):
    zeros = 0
    ones = 0

    for y in range(len(lines)):
        if lines[y][x] == "0":
            zeros += 1
        else:
            ones += 1
    
    if (zeros > ones):
        gamma += "0"
        epsilon += "1"
    else: # ones > zeros
        gamma += "1"
        epsilon += "0"

print(int(gamma, 2) * int(epsilon, 2))

