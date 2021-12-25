
with open("25.in") as file:
    lines = [list(line) for line in file.read().splitlines()]

def update(lines):
    moved = False

    newLines = [line.copy() for line in lines]
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if line[j-1] == ">" and c == ".":
                moved = True
                newLines[i][j-1] = "."
                newLines[i][j] = ">"
    lines = newLines

    newLines = [line.copy() for line in lines]
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if lines[i-1][j] == "v" and c == ".":
                moved = True
                newLines[i-1][j] = "."
                newLines[i][j] = "v"
    
    return newLines, moved

ls = lines
ans = 0
moved = True
while moved:
    ls, moved = update(ls)
    ans += 1
    
print(ans)



