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

# Create Grid. Pad '.'s all around to avoid having to deal with bounds issues
grid = []
grid.append(['.' for _ in range(len(schematic[0]) + 2)])
for line in schematic:
    grid.append(['.'] + [c for c in line] + ['.'])


def find_number_bounds(grid, r, c):
    """Returns the slice of a number based on our grid"""
    start = c
    stop = c
    
    while grid[r][start].isdigit():
        start -= 1
    start += 1  # add back the extra digit cause we have no do/while

    while grid[r][stop].isdigit():
        stop += 1
    
    return slice(start, stop)

seen = set()
part_numbers = []
gear_ratio = 0

for r, row in enumerate(grid):
    for c, symbol in enumerate(row):
        if symbol not in "0123456789.":
            parts = []

            # Look in all directions
            for d in directions.values():
                dr = r + d.r
                dc = c + d.c

                # Did we find a part we haven't seen yet?
                if grid[dr][dc].isdigit() and Point(dr, dc) not in seen: 

                    # Find the slice bounds
                    bounds = find_number_bounds(grid, dr, dc)

                    # Add those points to seen, so we don't look at parts we've already seen
                    for i in range(bounds.start, bounds.stop):
                        seen.add(Point(dr, i))
                    
                    # Generate the part number based on the range
                    part_number = int(''.join(grid[dr][bounds]))

                    # Add part to parts
                    parts.append(part_number)
            
            # Handle Part 2 and Gearing
            if symbol == '*' and len(parts) == 2:
                gear_ratio += functools.reduce(lambda x, y: x * y, parts)
            
            # Extend our overal part numbers
            part_numbers.extend(parts)

print(f"Part 1: {sum(part_numbers)}")
print(f"Part 2: {gear_ratio}")










if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
