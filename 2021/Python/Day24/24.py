from functools import lru_cache

with open("24.in") as file:
    lines = [line.split() for line in file.read().splitlines()]
    # instructions = [line.split() for line in lines]

# z is the only state to keep track off
@lru_cache(maxsize=None)
def solve(z=0, depth=0):
    for i in range(0, 10):#range(9, 0, -1):
        state = [0, 0, 0, 0]

        def translate(n):
            if "w" <= n <= "z":
                return state[ord(n) - ord("w")]
            
            return int(n)

        def sett(n, v):
            state[ord(n) - ord("w")] = v

        sett("z", z)
        sett(lines[depth][1], i)
        ii = depth + 1

        while True:
            # done
            if ii == len(lines):
                if translate("z") != 0:
                    return None
                
                return "" # str(i)

            instr = lines[ii]
            op = instr[0]
            a = instr[1]

            if op == "inp":
                res = solve(translate("z"), ii)
                if res is not None:
                    return str(i) + res
                break
            elif op == "add":
                sett(a, translate(a) + translate(instr[2]))
            elif op == "mul":
                sett(a, translate(a) * translate(instr[2]))
            elif op == "div":
                sett(a, translate(a) // translate(instr[2]))
            elif op == "mod":
                sett(a, translate(a) % translate(instr[2]))
            elif op == "eql":
                sett(a, int(translate(a) == translate(instr[2])))
            
            ii += 1

print(solve())


# dax = []
# ddz = []
# day = []
# for i, line in enumerate(lines):
#     if "add x " in line and "add x z" not in line:
#         dax.append(int(line.split()[2]))
#     if "div z" in line:
#         ddz.append(int(line.split()[2]))
#     # add z y is always the last instruction
#     if "add y" in line and i % 18 == 0:
#         day.append(int(line.split()[2]))

# def run(ch, z, w):
#     x = dax[ch] + (z % 26)
#     z = 




# variables = { "w": 0, "x": 1, "y": 2, "z": 3 }
# def run(state, line):
#     def maybeLit(x):
#         if x in variables:
#             return state[variables[x]]
        
#         return int(x)

#     state = list(state)
#     split = line.split()
#     op, a, b = split[0], split[1], split[2]

#     if op == "add":
#         state[variables[a]] += maybeLit(b)
#     elif op == "mul":
#         state[variables[a]] *= maybeLit(b)
#     elif op == "div":
#         state[variables[a]] //= maybeLit(b)
#     elif op == "mod":
#         state[variables[a]] %= maybeLit(b)
#     elif op == "eql":
#         state[variables[a]] = int(state[variables[a]] == maybeLit(b))

#     return tuple(state)








# dp = {}

# def solve(values, depth=0):
#     if depth == len(instructions):
#         z = values["z"]
#         if z == 0:
#             return "" 
        
#         return None

#     if instructions[depth][0] == "inp":
#         s = instructions[depth][1]

#         for i in range(9, 0, -1):
#             e = i

#             newValues = values.copy()
#             newValues[s] = e
#             res = best(newValues, depth+1)

#             if res is not None:
#                 return f"{e} {res}"

#         return None
#     else:
#         values = runInstr(values, instructions[depth])
#         return solve(values, depth + 1)

# def best(values, depth=0):
#     state = f"{depth}: {values}"
#     if state in dp: 
#         return dp[state]

#     print(state)

#     res = best(depth)
#     dp[state] = res

#     return res

# def runInstr(values, instr):
#     op = instr[0]
#     a = instr[1] 
#     if len(instr) == 3:
#         bLit = instr[2]
#         if bLit in values:
#             b = values[bLit]
#         else:
#             b = int(bLit)

#     if op == "inc":
#         values[a] += 1
#     elif op == "mul":
#         values[a] *= b
#     elif op == "div":
#         values[a] = values[a] // b
#     elif op == "mod":
#         values[a] = values[a] % b
#     elif op == "eql":
#         if values[a] == b:
#             values[a] = 1
#         else:
#             values[a] = 0

#     return values

# print(solve({}))
