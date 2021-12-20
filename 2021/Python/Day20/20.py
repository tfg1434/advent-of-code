import numpy as np

def enhance(lut, img, blink=0):
    img = np.pad(img, 3, constant_values=blink)

    if blink == 0: res = np.zeros(img.shape, dtype=np.uint8)
    else: res = np.ones(img.shape, dtype=np.uint8)

    h, w = img.shape

    for i in range(1, h-1):
        for j in range(1, w-1):
            idx = img[i-1:i+2, j-1:j+2].flatten()
            idx = int("".join(map(str, idx)), 2)
            res[i, j] = lut[idx]
    
    #                                                          lut values are 9 bits
    return res[1:-1, 1:-1], (lut[0] if blink == 0 else lut[int("111111111", 2)])

def show(img):
    for row in img:
        print("".join({ 0: ".", 1: "#" }[x] for x in row))


d = {".": 0, "#": 1}
LUT = np.array([d[c] for c in input()], dtype=np.uint8)

input()

img = []
while True:
    try:
        img.append(input())
    except EOFError:
        break
img = np.array([list(map(lambda c: d[c], row)) for row in img], dtype=np.uint8)
blink = 0

for _ in range(50):
    img, blink = enhance(LUT, img, blink)

show(img)
print(img.sum())
