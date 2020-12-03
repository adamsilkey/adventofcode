#! /usr/bin/env python3

print("day 3")

with open("input/2020-03.in") as f:
    day3 = [line.strip() for line in f]

trees = []

for line in day3:
    trees.append([c for c in line])
    for i in range(90):
        for c in line:
            trees[-1].append(c)


slope = (3, 1)

starting_pos = (0, 0)

collisions = 0

tree = "#"

a,b,c,d,e = 0,0,0,0,0


try:
    for idx, line in enumerate(trees):
        if trees[idx][idx*1] == tree:
            a += 1
        if trees[idx][idx*3] == tree:
            b += 1
        if trees[idx][idx*5] == tree:
            c += 1
        if trees[idx][idx*7] == tree:
            d += 1

        if trees[idx][idx//2] == tree:
            if idx % 2 == 0:
                e += 1


except IndexError:
    print("treeline not big enough")
    pass

print(a,b,c,d,e)
print(a*b*c*d*e)


# PART ONE
"""

print("day 3")

with open("input/2020-03.in") as f:
    day3 = [line.strip() for line in f]

trees = []

for line in day3:
    trees.append([c for c in line])
    for i in range(50):
        for c in line:
            trees[-1].append(c)

print(trees)

slope = (3, 1)

starting_pos = (0, 0)

collisions = 0

tree = "#"

try:
    for idx, line in enumerate(trees):
        if trees[idx][idx*3] == tree:
            print("TREE!")
            collisions += 1

except IndexError:
    print("treeline not big enough")
    pass


print(collisions)


part_one = 0
part_two = 0

print(f"part_one: {part_one}")
print(f"part_two: {part_two}")

"""
