#! /usr/bin/env python3

YEAR = "2024"
AOC_DAY = "06"

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


inp = load_file(filename)

p1 = p2 = 0


class Map:

    URLD = '^>v<'
    dirs = [
        compass['N'],
        compass['E'],
        compass['S'],
        compass['W'],
    ]

    def __init__(self, map: str):
        grid = []
        for line in map.strip().splitlines():
            grid.append([c for c in line])


        self.current_direction = None

        self.grid = dict()
        self.seen = set()

        for r, row in enumerate(grid):
            for c, char in enumerate(row):
                if char in self.URLD:
                    self.current = Point(r, c)
                    self.seen.add(Point(r,c))

                    self.direction = self.URLD.index(char)

                self.grid[Point(r,c)] = char

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

    def move(self):
        self.seen.add(self.current)
        # next = Point(self.current.r + self.URLD[self.direction].r, self.current.c + self.URLD[self.direction].c)
        dr, dc = self.dirs[self.direction]

        next = Point(self.current.r + dr, self.current.c + dc)

        if not self.inbounds(next):
            '''handle end'''
            print(self.current.r, self.current.c)
            print(next.r, next.c)
            print("hopping off!!! this is p1")
            print(len(self.seen))

            return len(self.seen)
        elif self.grid[next] == '#':
            '''handle turn'''
            self.direction = (self.direction + 1) % len(self.dirs)
        else:
            self.current = next

    def run(self):
        while True:
            res = self.move()
            if res is not None:
                break

        return res





map = Map(inp)

map.run()
























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
