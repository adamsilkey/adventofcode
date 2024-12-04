#! /usr/bin/env python3

YEAR = "2024"
AOC_DAY = "04"

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
    case "-t":
        test = True
    case "-p":
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

inp = load_file(filename)

p1 = p2 = 0


Point = namedtuple("Point", ["r", "c"])

compass = dict(
    NW = Point(-1, -1),
    N = Point(-1, 0),
    NE = Point(-1, 1),
    W = Point(0, -1),
    E = Point(0, 1),
    SW = Point(1, -1),
    S = Point(1, 0),
    SE = Point(1, 1),
)


class WordSearch:

    SEARCH = 'XMAS'

    def __init__(self, wordmap: str):
        self.grid = []
        for line in wordmap.strip().splitlines():
            self.grid.append([c for c in line])

        self.height = len(self.grid)
        self.width = len(self.grid[0])

        self.p1 = 0
        self.p2 = 0

    def inbounds(self, point: Point):
        return 0 <= point.r < self.height and 0 <= point.c < self.width

    def onedge(self, point: Point):
        if point.r == 0 or point.r == self.height or point.c == 0 or point.c == self.width:
            return True
        else:
            return False

    def look(self, point: Point, compasskey, next_char = 0):
        if self.grid[point.r][point.c] != self.SEARCH[next_char]:
            return False

        next_char += 1

        # We've hit a match if we'e hit 4
        if next_char == len(self.SEARCH):
            return True

        direction = compass[compasskey]
        dr = direction.r
        dc = direction.c
        next_point = Point(point.r + dr, point.c + dc)

        while self.inbounds(next_point):
            result = self.look(next_point, compasskey, next_char)

            if result == True:
                return True
            else:
                break

        return False

    def look_all_directions(self, point: Point):

        for k in compass.keys():
            print(k)
            if self.look(point, k) == True:
                self.p1 += 1


search = WordSearch(inp)

for line in search.grid:
    print(line)

for r in range(search.height):
    for c in range(search.width):
        search.look_all_directions(Point(r,c))


print(search.p1)


















# print(f"{p1=}")
# print(f"{p2=}")

if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
print("Execution time:", perf_counter() - __start_time)
print()
