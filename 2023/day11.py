#! /usr/bin/env python3

YEAR = '2023'
AOC_DAY = '11'

import sys
from time import perf_counter

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
from math import lcm, prod

DEBUG = True

__start_time = perf_counter()


inp = load_lines(filename)


Point = namedtuple("Point", "r c")


# galaxy = [c for c in [line for line in inp]]
galaxy = []
for line in inp:
    row = []
    for c in line:
        row.append(c)
    galaxy.append(row[:])
print('original galaxy')
for row in galaxy:
    print(row)
print()


rows_to_expand = []
for idx, row in enumerate(galaxy):
    if all(c == '.' for c in row):
        rows_to_expand.append(idx)


columns_to_expand = []
for col_idx in range(len(galaxy[0])):
    for row in galaxy:
        if row[col_idx] != ".":
            break
    else:
        # no break, we found a column with all
        columns_to_expand.append(col_idx)

print(columns_to_expand)

# WE DID IT

coords = []
for r, row in enumerate(galaxy):
    for c, char_ in enumerate(row):
        if char_ != '.':
            coords.append(Point(r,c))

print()
print(coords)


def cartesian_distance(a: Point, b: Point, expansion=1):
    distance = abs(a.r - b.r) + abs (a.c - b.c)
    row_range = range(min(a.r, b.r), max(a.r, b.r))
    col_range = range(min(a.c, b.c), max(a.c, b.c))
    for i in row_range:
        if i in rows_to_expand:
            distance += expansion
    for i in col_range:
        if i in columns_to_expand:
            distance += expansion
    return distance


p1 = 0
for i, a in enumerate(coords):
    for i2, b in enumerate(coords[i+1:]):
        p1 += cartesian_distance(a,b)

print(p1)

p2 = 0
            ### I ACTUALLY DON'T KNOW WHY THIS IS OFF BY ONE AHHHHHH
for test in [9, 99, 999_999]:
    p2 = 0
    for i, a in enumerate(coords):
        for i2, b in enumerate(coords[i+1:]):
            # p2 += cartesian_distance(a,b, 1000000)
            p2 += cartesian_distance(a,b, test)

    print(test, p2)


#### Part 2












































if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
print("Execution time:", perf_counter() - __start_time)
print()