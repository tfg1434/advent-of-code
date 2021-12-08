import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "in.txt")) as file:
    lines = file.readlines()

input = [x.rstrip("\n").split(" ") for x in lines]

depth = 0
hPos = 0

for instr in input:
    if (instr[0] == "forward"):
        hPos += int(instr[1])
    elif (instr[0] == "up"):
        depth -= int(instr[1])
    elif (instr[0] == "down"):
        depth += int(instr[1])


print(depth * hPos)