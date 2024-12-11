#! /usr/bin/env python3

YEAR = "2024"
AOC_DAY = "11"

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
from functools import cmp_to_key
from math import lcm, prod

DEBUG = True

__start_time = perf_counter()


p1 = p2 = 0

class Point:
    COMPASS = dict(
        # DIRECTION = (r, c)
        NW = (-1, -1),
        N = (-1, 0),
        NE = (-1, 1),
        W = (0, -1),
        E = (0, 1),
        SW = (1, -1),
        S = (1, 0),
        SE = (1, 1),
    )

    def __init__(self, r, c):
        self.r = r
        self.c = c

    def __repr__(self):
        return f"{self.__class__.__qualname__}({self.r}, {self.c})"

    def __str__(self):
        return f"({self.r},{self.c})"

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.r == other.r and self.c == other.c

    def __hash__(self):
        return hash((self.r, self.c))

    def move(self, d):
        if d not in self.COMPASS:
            raise KeyError(f"{d} not in compass")

        dr, dc = self.COMPASS[d]

        self.r += dr
        self.c += dc

        return self.r, self.c

    def check(self, d):
        if d not in self.COMPASS:
            raise KeyError(f"{d} not in compass")

        dr, dc = self.COMPASS[d]

        return self.__class__(self.r + dr, self.c + dc)


class Map:

    def __init__(self, map: str):
        grid = []
        for line in map.strip().splitlines():
            grid.append([c for c in line])

        self.rawmap = grid
        self.grid = dict()

        for r, row in enumerate(grid):
            for c, char in enumerate(row):
                self.grid[Point(r,c)] = int(char)

        self.height = len(grid)
        self.width = len(grid[0])

        self.p1 = 0
        self.p2 = 0

    def inbounds(self, point: Point):
        return 0 <= point.r < self.height and 0 <= point.c < self.width

    def onedge(self, point: Point):
        if point.r == 0 or point.r == self.height or point.c == 0 or point.c == self.width:
            return True
        else:
            return False

    def print(self):
        map = []
        for row in self.rawmap:
            map.append([c for c in row])

        for node in self.antinodes:
            r, c = node
            map[r][c] = '#'

        for row in map:
            print(''.join(row))


    def trailrating(self, point: Point, top=None):
        if top is None:
            top = []

        current_level = self.grid[point]

        if current_level == 9:
            top.append(point)
            return top

        for d in ['N', 'E', 'S', 'W']:
            next_point = point.check(d)

            if self.inbounds(next_point) and self.grid[next_point] == current_level + 1:
                top = self.trailrating(next_point, top)

        return top

    def heads_and_trails(self):
        p1 = 0
        p2 = 0
        for point, n in self.grid.items():
            if n == 0:
                trails = self.trailrating(point)
                p1 += len(set(trails))
                p2 += len(trails)

        return p1, p2






inp = load_file(filename)





'''
If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.

If the stone is engraved with a number that has an even number of digits, it is replaced by two stones.
The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved
on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)

If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
'''





inp = inp.split()
inp = deque([int(c) for c in inp])

# inp = deque(sorted([int(c) for c in inp]))
# inp = deque(inp)




def blink(l: deque[int]):

    newl = deque()

    for n in l:
        ns = str(n)

        if n == 0:
            n = 1
            newl.append(n)
        elif len(ns) % 2 == 0:
            half = len(ns) // 2
            a = int(ns[:half])
            b = int(ns[half:])
            newl.append(a)
            newl.append(b)
        else:
            n *= 2024
            newl.append(n)

    return newl



if True:
    d = inp
    for i in range(25):
        d = blink(d)
        print(f"{i+1}: {len(d)}")
        # input()

    p1 = len(d)





# rules = dict()
# count = Counter()

# # def better_blink(deq: deque[int]):
# #     for n in deque

# def blink_rule(n):
#     rules = []
#     ns = str(n)

#     if n == 0:
#         n = 1
#         rules.append(n)
#     elif len(ns) % 2 == 0:
#         half = len(ns) // 2
#         a = int(ns[:half])
#         b = int(ns[half:])
#         rules.append(a)
#         rules.append(b)
#     else:
#         n *= 2024
#         rules.append(n)

#     return rules





# d = inp
# d = deque([0])

# print(f"0: {len(d)}: {d}")
# for i in range(75):
#     d = blink(d)
#     print(f"{i+1}: {len(d)}: {d}")
#     # print(f"{i+1}: {len(d)}")
#     input()

# p2 = len(d)






















print(f"{p1=}")
print(f"{p2=}")

if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
print("Execution time:", perf_counter() - __start_time)
print()
