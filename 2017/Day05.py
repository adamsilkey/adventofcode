with open('input.txt') as f:
    lines = f.readlines()

lis = []

for line in lines:
    lis.append(int(line))

print(lis)

import sys

def jump(lis):
    i = 0
    total = 0
    while i < len(lis):
        total +=1
        jump = lis[i]
        lis[i] += 1
        i += jump

    return lis, total

print(jump([0,3,0,1,-3]))
print(jump(lis))
