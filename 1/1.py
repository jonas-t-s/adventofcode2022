import os
import numpy as np
file = "./input"

readedlines =[[]]
with open(file) as inp:
    state = 0
    for line in inp.readlines():
        if line == "\n":
            state +=1
            readedlines.append([])
        else:
            readedlines[state].append(int(line))
print(readedlines)
result = []
for entity in readedlines:
    result.append(np.sum(entity))
print(np.max(result))