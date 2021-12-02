import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "in.txt")) as file:
    lines = file.readlines()

prevLine = 999999
count = 0

for line in lines:
    line = int(line)

    if line > prevLine:
        count += 1

    prevLine = line

print(count)