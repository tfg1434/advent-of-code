import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "in.txt")) as file:
    lines = file.read().splitlines()

def processLine(line):
    l = line.split(" -> ")

    return list(map(lambda s: list(map(int, s.split(","))), l))

lineSegs = list(map(processLine, lines))
map = {}
sign = lambda x: x and (1, -1)[x<0]

for seg in lineSegs:
    fr = seg[0]
    to = seg[1]
    dx = to[0] - fr[0]
    dy = to[1] - fr[1]

    # +1 bc we want to include the end point
    # length for diagonal is longest length
    for i in range(max(abs(dx), abs(dy)) + 1):
        x = fr[0] + sign(dx) * i
        y = fr[1] + sign(dy) * i

        if (dx == 0 or dy == 0):
            if (x, y) not in map:
                map[(x, y)] = 1
            else:
                map[(x, y)] += 1

ans = 0
for k in map:
    if map[k] >= 2:
        ans += 1

print(ans)
