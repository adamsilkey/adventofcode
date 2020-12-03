#! /usr/bin/env python3

import sys

print("day 3")

with open("input/2020-03.in") as f:
    day3 = [line.strip() for line in f]

trees = [line * 90 for line in day3]

tree = "#"

a = b = c = d = e = 0

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
    exit()

print(f"Part One: {b}")
print(f"Part Two: {(a,  b, c, d, e)}")
print(f"Part Two: {a * b * c * d * e}")
