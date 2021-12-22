from collections import defaultdict

def sign(n):
    if n == 0: return n
    return 0 if n < 0 else 1

def solve1():
    s = set()
    while True:
        try:
            split = input().split()
        except:
            break

        split[1] = split[1].split(",")
        xs = [int(x) for x in split[1][0][2:].split("..")]
        ys = [int(y) for y in split[1][1][2:].split("..")]
        zs = [int(z) for z in split[1][2][2:].split("..")]
        
        if any(x < -50 or x > 50 for x in xs):
            continue
        if any(y < -50 or y > 50 for y in ys):
            continue
        if any(z < -50 or z > 50 for z in zs):
            continue

        if split[0] == "on":
            for x in range(xs[0], xs[1] + 1, sign(xs[1] - xs[0])):
                for y in range(ys[0], ys[1] + 1, sign(ys[1] - ys[0])):
                    for z in range(zs[0], zs[1] + 1, sign(zs[1] - zs[0])):
                        s.add((x, y, z))
        elif split[0] == "off":
            for x in range(xs[0], xs[1] + 1, sign(xs[1] - xs[0])):
                for y in range(ys[0], ys[1] + 1, sign(ys[1] - ys[0])):
                    for z in range(zs[0], zs[1] + 1, sign(zs[1] - zs[0])):
                        s.discard((x, y, z))

    return len(s)

def solve2():
    ans = 0
    cubes = []

    while True:
        print("iter")

        line = input()
        if not line: break

        split = line.split()
        split[1] = split[1].split(",")
        xstart, xstop = [int(x) for x in split[1][0][2:].split("..")]
        ystart, ystop = [int(y) for y in split[1][1][2:].split("..")]
        zstart, zstop = [int(z) for z in split[1][2][2:].split("..")]

        xstop += 1
        ystop += 1
        zstop += 1

        cube = [xstart, xstop, ystart, ystop, zstart, zstop, 0 if split[0] == "off" else 1]
        newCubes = []

        for item in cubes:
            xlap = xstop > item[0] and xstart < item[1]
            ylap = ystop > item[2] and ystart < item[3]
            zlap = zstop > item[4] and zstart < item[5]

            if xlap and ylap and zlap:
                if item[0] < xstart:
                    newCube = [item[0], xstart, item[2], item[3], item[4], item[5], item[6]]
                    item[0] = xstart
                    newCubes.append(newCube)
                if item[1] > xstop:
                    newCube = [xstop, item[1], item[2], item[3], item[4], item[5], item[6]]
                    item[1] = xstop
                    newCubes.append(newCube)
                if item[2] < ystart:
                    newCube = [item[0], item[1], item[2], ystart, item[4], item[5], item[6]]
                    item[2] = ystart
                    newCubes.append(newCube)
                if item[3] > ystop:
                    newCube = [item[0], item[1], ystop, item[3], item[4], item[5], item[6]]
                    item[3] = ystop
                    newCubes.append(newCube)
                if item[4] < zstart:
                    newCube = [item[0], item[1], item[2], item[3], item[4], zstart, item[6]]
                    item[4] = zstart
                    newCubes.append(newCube)
                if item[5] > zstop:
                    newCube = [item[0], item[1], item[2], item[3], zstop, item[5], item[6]]
                    item[5] = zstop
                    newCubes.append(newCube)
            else:
                newCubes.append(item)

        newCubes.append(cube)
        cubes = newCubes

    for cube in cubes:
        # 1 for on, 0 for off
        if cube[6] == 1:
            ans += (cube[1] - cube[0]) * (cube[3] - cube[2]) * (cube[5] - cube[4])
        
    print(ans)

solve2()

        

    