score1 = 0
pos1 = 7
score2 = 0
pos2 = 1

dice_i = 1
timesRolled = 0

def roll_n(n=3):
    global dice_i
    global timesRolled

    timesRolled += n
    total = 0

    for _ in range(n):
        total += dice_i
        dice_i += 1

        if dice_i > 100:
            dice_i = 1
    
    return total

def wrap(pos):
    res = 0

    for _ in range(pos):
        res += 1

        if res > 10:
            res = 1

    return res

while True:
    roll = roll_n()
    pos1 = wrap(pos1 + roll)
    score1 += pos1
    #print(f"player 1 rolls {roll} and moves to square {pos1} for a total score of {score1}")

    if score1 >= 1000:
        print(score2 * timesRolled)

        break

    roll = roll_n()
    pos2 = wrap(pos2 + roll)
    score2 += pos2
    #print(f"player 2 rolls {roll} and moves to square {pos2} for a total score of {score2}")

    if score2 >= 1000:
        print(score1 * timesRolled)
        
        break

timesRolled = 0
def diracRoll():
    global timesRolled
    timesRolled += 1

    return [1, 2, 3]

dp = {}
def solve2(pos1, pos2, score1, score2):
    if score1 >= 21: return (1, 0)
    if score2 >= 21: return (0, 1)

    if (pos1, pos2, score1, score2) in dp:
        return dp[(pos1, pos2, score1, score2)]
    
    res = (0, 0)
    for i in [1, 2, 3]:
        for j in [1, 2, 3]:
            for k in [1, 2, 3]:
                newPos1 = (pos1 + i + j + k) % 10
                newScore1 = score1 + wrap(pos1 + i + j + k)

                u1, u2 = solve2(pos2, newPos1, score2, newScore1)
                res = (res[0] + u2, res[1] + u1)
    
    dp[(pos1, pos2, score1, score2)] = res

    return res

print(solve2(7, 1, 0, 0))





