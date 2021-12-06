import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "in.txt")) as file:
    lines = file.read().splitlines()

fishes = list(map(int, lines[0].split(',')))

for i in range(80):
    toAppend = []

    for f, fish in enumerate(fishes):
        if (fish == 0):
            fishes[f] = 7
            toAppend.append(8)

        fishes[f] -= 1

    for fish in toAppend:
        fishes.append(fish)

sum = 0
for fish in fishes:
    sum += fish

print(len(fishes))
        
