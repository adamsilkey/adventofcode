#! /usr/bin/env python3

YEAR = '2023'
AOC_DAY = '03'

import sys

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
    filename = f"input/{AOC_DAY}.test"
else:
    filename = f"input/{AOC_DAY}.in"

title = f"Advent of Code {YEAR} - Day {AOC_DAY} - {'Test' if test else 'Production'}"

print(f"=" * len(title))
print(title)
print(f"=" * len(title))

def load_file(filename: str) -> str:
    """Loads an AOC file, returns a string"""

    with open(filename) as f:
        return f.read().rstrip("\n")


def load_lines(filename: str) -> list[str]:
    """Returns a list of lines"""

    return load_file(filename).split("\n")


def load_ints(filename: str) -> list[int]:
    """Returns a list of ints"""

    return [int(i) for i in load_lines(filename)]


def load_comma_separated_ints(filename: str) -> list[int]:
    """Returns a list of ints from a comma separated list of ints"""

    return [int(i) for i in load_file(filename).strip().split(",")]


import functools
import itertools as it
import re
import sys
from collections import Counter, defaultdict, deque, namedtuple
from dataclasses import dataclass


schematic = load_lines(filename)

Point = namedtuple("Point", ["r", "c"])

directions = dict(
    NW = Point(-1, -1),
    N = Point(-1, 0),
    NE = Point(-1, 1),
    W = Point(0, -1),
    E = Point(0, 1),
    SW = Point(1, -1),
    S = Point(1, 0),
    SE = Point(1, 1),
)


MIN = 0
MAX_Y = len(schematic)
MAX_X = len(schematic[0])

grid = []
grid.append(['.' for _ in range(MAX_X + 2)])
for line in schematic:
    grid.append(['.'] + [c for c in line] + ['.'])



def find_number(grid, r, c):
    left = c
    right = c
    
    # print(grid[r][left])
    # input()

    while grid[r][left].isdigit():
        left -= 1
    left += 1  # add back the extra digit cause we have no do/while

    while grid[r][right].isdigit():
        right += 1
    right -= 1 # see above

    return left, right


seen = set()

part_numbers = []

gear_ratio = 0

for r, row in enumerate(grid):
    for c, symbol in enumerate(row):
        if symbol not in "0123456789.":
            # look in all directions
            gear_score = 0
            gears = []
            for d in directions.values():
                new_point = Point(r + d.r, c + d.c)
                if grid[new_point.r][new_point.c].isdigit() and new_point not in seen: 
                    print("we found a number")
                    # find the adjacent numbers, add it to seen
                    left, right = find_number(grid, new_point.r, new_point.c)
                    # print(left, right)
                    for i in range(left, right + 1):
                        seen.add(Point(new_point.r, i))
                    part_number = int(''.join(grid[new_point.r][left:right+1]))
                    part_numbers.append(part_number)
                    # part_numbers.append(int(''.join(grid[new.r][left:right+1])))
                    gear_score += 1
                    gears.append(part_number)
            if gear_score == 2:
                gear_ratio += gears[0] * gears[1]


print(part_numbers)
print(gear_ratio)

print(sum(part_numbers))





# for y, line in enumerate(schematic):
#     for x, c in enumerate(line):
#         if c not in "0132456789.":
#             print(f"found special character: {c}")
#             # look in all directions
#             for dir_ in directions:
#                 pass










p1 = 0
p2 = 0

print(f"{p1=}")
print(f"{p2=}")























if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
