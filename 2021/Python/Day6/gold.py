import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "in.txt")) as file:
    lines = file.read().splitlines()

fishes = list(map(int, lines[0].split(",")))

types = [0] * 10
for fish in fishes:
    types[fish] += 1

for i in range(256):
    nts = [0] * 10

    for j in range(len(types) - 1):
        nts[j] += types[j + 1]

    # fish of type 6 += fish of type 0
    nts[6] += types[0]
    #fish of type 8 += fish of type 0
    nts[8] += types[0]

    types = nts

print(sum(types))
        
