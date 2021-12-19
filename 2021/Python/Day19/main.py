import re
from itertools import permutations

scanners = []

with open('in.txt') as file:
    lines = file.read().splitlines()
    txt = "\n".join(lines)

labels = re.finditer(r"---.*---", txt)
labels = [x for x in labels]

def rotate(mat):
    N=len(mat)

    # Consider all squares one by one
    for x in range(0, int(N / 2)):
         
        # Consider elements in group  
        # of 4 in current square
        for y in range(x, N-x-1):
             
            # store current cell in temp variable
            temp = mat[x][y]
 
            # move values from right to top
            mat[x][y] = mat[y][N-1-x]
 
            # move values from bottom to right
            mat[y][N-1-x] = mat[N-1-x][N-1-y]
 
            # move values from left to bottom
            mat[N-1-x][N-1-y] = mat[N-1-y][x]
 
            # assign temp to left
            mat[N-1-y][x] = temp

for i, group in enumerate(labels):
    if i < len(labels) - 1:
        nextGroup = labels[i+1]
        scanner = txt[group.end()+1:nextGroup.start()-2]
    else:
        scanner = txt[group.end()+1:]

    scanner = [[int(n) for n in line.split(",")] for line in scanner.splitlines()]
    scanners.append(scanner)

def permutate(scan, perm, negate):
    res = []

    for item in scan:
        res.append([negate[0] * item[perm[0]], negate[1] * item[perm[1]], negate[2] * item[perm[2]]])

    return res

N = len(lines)
dists = [(0, 0, 0)]
negates = [(1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1), (-1, 1, 1), (-1, 1, -1), (-1, -1, 1), (-1, -1, -1)]
assert len(negates) == 8

def solve(A, B):
    an = set([tuple(x) for x in A])

    for perm in permutations([0, 1, 2]):
        for negate in negates:
            a = A
            b = permutate(B, perm, negate)

            for pointA in a:
                for pointB in b:
                    dAB = [pointB[0] - pointA[0], pointB[1] - pointA[1], pointB[2] - pointA[2]]
                    translated = []
                    count = 0

                    for thisB in b:
                        absPoint = (thisB[0] - dAB[0], thisB[1] - dAB[1], thisB[2] - dAB[2])
                        if absPoint in an:
                            count += 1
                        translated.append(list(absPoint))

                    #counts as mach condition
                    if count >= 12:
                        print("found")
                        dists.append(tuple(dAB))
                        return translated, True
    
    return None, False

good = scanners[0]
indexes = set()
indexes.add(0)
aligned = {}
aligned[0] = scanners[0]
every = []
every += [tuple(x) for x in scanners[0]]
notAligned = set()

print(scanners)

while len(indexes) < len(scanners):
    for i in range(len(scanners)):
        if i in indexes: continue

        for j in indexes:
            print(f"checking {i} with {j}")

            if (i, j) in notAligned: continue

            translate, yesno = solve(aligned[j], scanners[i])
            if yesno:
                indexes.add(i)
                aligned[i] = translate
                every += [tuple(x) for x in translate]
                break

            notAligned.add((i, j))

print(len(set(every)))

print(dists)
p2 = []
for a in dists:
    for b in dists:
        p2.append(sum([abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2])]))
print(max(dists), min(dists))


# def permutate(lst, pIndex):
#     for r, row in enumerate(lst):
#         lst[r] = list(list(permutations(row))[pIndex])




