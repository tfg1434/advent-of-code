import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "in.txt")) as file:
    lines = file.readlines()

def getWinPos(n: int) -> list[int]:
    y = n

    list = []
    for _ in range(3):
        list.append(y)

        y += 1

    return list

amnt = len(lines) - 2
lastSum = 999999
ans = 0

for i in range(amnt):
    sum = 0

    for j in getWinPos(i):
        sum += int(lines[j])

    if sum > lastSum:
        ans += 1

    lastSum = sum

print(ans)



