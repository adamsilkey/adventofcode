#! /usr/bin/env python3.10

YEAR = '2021'
AOC_DAY = '13'

import itertools as it
import sys
from collections import Counter, defaultdict, deque, namedtuple
from dataclasses import dataclass

if not (YEAR and AOC_DAY):
    print("!!! Set YEAR/AOC_DAY")
    sys.exit(1)

def fail():
    print("!!! Need to define -p for production or -t for test")
    sys.exit(1)

if len(sys.argv) != 2:
    fail()

match sys.argv[1].lower():
    case '-t':
        test = True
    case '-p':
        test = False
    case _:
        fail()

if test:
    filename = f"{AOC_DAY}.test"
else:
    filename = f"{AOC_DAY}.in"

title = f"Advent of Code {YEAR} - Day {AOC_DAY} - {'Test' if test else 'Production'}"

print(f"=" * len(title))
print(title)
print(f"=" * len(title))


def load_file(filename: str) -> str:
    """Loads an AOC file, returns a string"""

    with open(filename) as f:
        return f.read().rstrip("\n")


Point = namedtuple("Point", ["x", "y"])
Fold = namedtuple("Fold", ["direction", "amount"])


dots, raw_folds = load_file(filename).split("\n\n")


grid = set()
for line in dots.split("\n"):
    x, y = line.split(',')
    grid.add(Point(int(x), int(y)))


folds = []
for line in raw_folds.split("\n"):
    direction, amount = line.split("=")
    folds.append(Fold(direction[-1], int(amount)))





def fold(grid: set(), fold: Fold):

    max_x, max_y = 0, 0
    for dot in grid:
        if dot.x > max_x:
            max_x = dot.x
        if dot.y > max_y:
            max_y = dot.y


    # if fold.direction == 'x':
    #     transform = Point(fold.amount, 0)
    # else:
    #     transform = Point(0, fold.amount)

    new_grid = set()

    for dot in grid:
        print(f"original dot: {dot}")
        # straight add dots under the fold
        if fold.direction == 'x':
            if dot.x < fold.amount:
                print(dot)
                new_grid.add(dot)
                continue
            else:
                x = fold.amount - (dot.x - fold.amount)
                y = dot.y
        elif fold.direction == 'y':
            if dot.y < fold.amount:
                print(dot)
                new_grid.add(dot)
                continue
            else:
                x = dot.x
                y = fold.amount - (dot.y - fold.amount)

        dot = Point(x, y)
        print(dot)
        new_grid.add(dot)

    return max_x, max_y, new_grid


# Part 1
# print(len(grid))
# grid = fold(grid, folds[0])
# print(len(grid))


# Part 2
for one_fold in folds:
    max_x, max_y, grid = fold(grid, one_fold)

print(len(grid), max_x, max_y)

p2 = []
for y in range(max_y + 1):
    p2.append(['.' for x in range(max_x + 1)])

# for row in p2:
#     print(''.join(row))

for dot in grid:
    p2[dot.y][dot.x] = '#'


for row in p2:
    print(''.join(row))


