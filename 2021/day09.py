#! /usr/bin/env python3.10

YEAR = '2021'
AOC_DAY = '09'

import itertools as it
import sys
from collections import Counter, defaultdict, deque
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


def load_lines(filename: str) -> list[str]:
    """Returns a list of lines"""

    return load_file(filename).split("\n")


def load_ints(filename: str) -> list[int]:
    """Returns a list of ints"""

    return [int(i) for i in load_lines(filename)]


def load_comma_separated_ints(filename: str) -> list[int]:
    """Returns a list of ints from a comma separated list of ints"""

    return [int(i) for i in load_file(filename).strip().split(",")]


ll = load_lines(filename)
caves = []
for row in ll:
    cave_row = [int(c) for c in row]
    caves.append(cave_row)


def look_around(num, x, y, caves):
    values = []
    # print(f"{num=} {x=} {y=}")

    # Above
    if y < len(caves) - 1:
        values.append(caves[y + 1][x + 0])
    # Below
    if y > 0:
        values.append(caves[y - 1][x + 0])
    # Left
    if x < len(caves[0]) - 1:
        values.append(caves[y + 0][x + 1])
    # Right
    if x > 0:
        values.append(caves[y - 0][x - 1])

    for val in values:
        if num >= val:
            return 0
    else: # no break
        # print(f"found one: {num} {values}")
        return num + 1



total = 0
for y, row in enumerate(caves):
    for x, height in enumerate(row):
        total += look_around(height, x, y, caves)

print(f"p1: {total}")
















def traverse_the_basin(caves, x, y, seen):
    # print(f"{num=} {x=} {y=}")

    if (x,y) == 9:
        return

    here = (x,y)

    if here in seen:
        return

    seen.add(here)

    # Above
    if y < len(caves) - 1:
        if caves[y + 1][x + 0] != 9:
            traverse_the_basin(caves, x+0, y+1, seen)
    # Below
    if y > 0:
        if caves[y - 1][x + 0] != 9:
            traverse_the_basin(caves, x+0, y-1, seen)
    # Left
    if x < len(caves[0]) - 1:
        if caves[y + 0][x + 1] != 9:
            traverse_the_basin(caves, x+1, y+0, seen)
    # Right
    if x > 0:
        if caves[y - 0][x - 1] != 9:
            traverse_the_basin(caves, x-1, y-0, seen)

    return



seen = set()

basin_sizes = [0]
for y, row in enumerate(caves):
    for x, height in enumerate(row):
        if caves[y][x] == 9:
            continue
        traverse_the_basin(caves, x, y, seen)
        size = len(seen) - sum(basin_sizes)
        basin_sizes.append(size)


print(sorted(basin_sizes))