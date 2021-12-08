from functools import *
import os
import math
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "in.txt")) as file:
    program = list(map(int, file.readlines()[0].split(",")))

def run(prog, i):
    if prog[i] == 99:
        return prog
    else:
        in1 = prog[prog[i + 1]]
        in2 = prog[prog[i + 2]]

        outPos = i + 3

        if prog[i] == 1:
            prog[prog[outPos]] = in1 + in2
        elif prog[i] == 2:
            prog[prog[outPos]] = in1 * in2

        return run(prog, i + 4)

program[1] = 12
program[2] = 2
print(run(program, 0)[0])


