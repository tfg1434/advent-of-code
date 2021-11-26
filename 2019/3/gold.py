# from functools import *
# import os
# import math
# __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# with open(os.path.join(__location__, "in.txt")) as file:
#     lines = file.readlines()
#     path1 = lines[0].split(',')
#     path2 = lines[1].split(',')

# def populateList(path):
#     ret = list()
#     pos = (0, 0, 0)
#     c = 0

#     for instr in path:
#         dir = instr[0]
#         count = int(instr[1:])

#         for _ in range(count):
#             c += 1
            
#             if (dir == "U"):
#                 pos = (pos[0], pos[1] - 1, c)
#             elif (dir == "R"):
#                 pos = (pos[0] + 1, pos[1], c)
#             elif (dir == "D"):
#                 pos = (pos[0], pos[1] + 1, c)
#             elif (dir == "L"):
#                 pos = (pos[0] - 1, pos[1], c)

#             ret.append(pos)

#     return ret
    
# list1 = populateList(path1)
# list2 = populateList(path2)

# intersection = []
# for i, item in enumerate(list1):
#     if (i % 10 == 0): print(i)

#     if any(x[0] == item[0] and x[1] == item[1] for x in list2):
#         intersection.add(item)

# print(min(map(lambda x: x[2], intersection)))








