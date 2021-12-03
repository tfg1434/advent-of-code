import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "in.txt")) as file:
    lines = file.read().splitlines()

x = 0
oxy = lines.copy()
while True:
    zeros = 0
    ones = 0

    for y in range(len(oxy)):
        if oxy[y][x] == "0":
            zeros += 1
        else:
            ones += 1

    if zeros > ones:
        oxy = [l for l in oxy if l[x] == "0"]
    elif zeros < ones or zeros == ones:
        oxy = [l for l in oxy if l[x] == "1"]

    if (len(oxy) == 1):
        break

    x += 1


x = 0
co2 = lines.copy()
while True:
    zeros = 0
    ones = 0

    for y in range(len(co2)):
        if co2[y][x] == "0":
            zeros += 1
        else:
            ones += 1

    if zeros > ones:
        oxy = [l for l in oxy if l[x] == "0"]
    elif zeros < ones or zeros == ones:
        oxy = [l for l in oxy if l[x] == "1"]

    if (len(oxy) == 1):
        break

    x += 1

print(oxy)
    


        

