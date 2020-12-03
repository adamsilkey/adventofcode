#! /usr/bin/env python3

print("day 3")

with open("input/2020-03.in") as f:
    trees = [line.strip() for line in f]

tree_len = len(trees[0])
tree = "#"
a = b = c = d = e = 0

for idx, line in enumerate(trees):
    if trees[idx][(idx * 1) % tree_len] == tree:
        a += 1
    if trees[idx][(idx * 3) % tree_len] == tree:
        b += 1
    if trees[idx][(idx * 5) % tree_len] == tree:
        c += 1
    if trees[idx][(idx * 7) % tree_len] == tree:
        d += 1
    if trees[idx][(idx // 2) % tree_len] == tree:
        if idx % 2 == 0:
            e += 1

print(f"Part One: {b}")
print(f"Part Two: {(a, b, c, d, e)}")
print(f"Part Two: {a * b * c * d * e}")
