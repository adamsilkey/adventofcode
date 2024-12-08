#! /usr/bin/env python3

YEAR = "2024"
AOC_DAY = "08"

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

p1 = p2 = 0

inp = load_file(filename)


class Map:

    def __init__(self, map: str):
        grid = []
        for line in map.strip().splitlines():
            grid.append([c for c in line])

        self.rawmap = grid

        self.grid = dict()
        self.nodes = dict()
        self.antinodes = set()

        for r, row in enumerate(grid):
            for c, char in enumerate(row):
                self.grid[Point(r,c)] = char

                if char != '.':
                    if char not in self.nodes:
                        self.nodes[char] = []
                    self.nodes[char].append(Point(r,c))

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

    def find_antinodes(self, a: Point, b: Point):
        dr = abs(a.r - b.r)
        dc = abs(a.c - b.c)

        # standardize
        if a.r > b.r:
            # print('standardzin')
            a, b = b, a

        # If a is east of b and same row
        elif a.c > b.c and a.r == b.r:
            a, b = b, a
        print(a, b)

        # cases
        # a is n of b
        if a.r == b.r:
            a2r = a.r - dr
            a2c = a.c
            b2r = b.r + dr
            b2c = b.c
        # a is w of b
        elif a.c == b.c:
            a2r = a.r
            a2c = a.c - dc
            b2r = b.r
            b2c = b.c + dc
        # a is nw of b
        elif a.c < b.c:
            # print(dr, dc)
            a2r = a.r - dr
            a2c = a.c - dc
            b2r = b.r + dr
            b2c = b.c + dc
        # a is ne of b
        elif a.c > b.c:
            a2r = a.r - dr
            a2c = a.c + dc
            b2r = b.r + dr
            b2c = b.c - dc
        else:
            raise("shouldn't have happened")

        return Point(a2r, a2c), Point(b2r, b2c)


    def find_antinode_vectors(self, a: Point, b: Point):
        dr = abs(a.r - b.r)
        dc = abs(a.c - b.c)

        # standardize
        if a.r > b.r:
            a, b = b, a

        # If a is east of b and same row
        elif a.c > b.c and a.r == b.r:
            a, b = b, a

        # cases
        # a is n of b
        if a.r == b.r:
            a2dr = -dr
            a2dc = 0
            b2dr = dr
            b2dc = 0
        # a is w of b
        elif a.c == b.c:
            a2dr = 0
            a2dc = -dc
            b2dr = 0
            b2dc = dc
        # a is nw of b
        elif a.c < b.c:
            a2dr = -dr
            a2dc = -dc
            b2dr = dr
            b2dc = dc
        # a is ne of b
        elif a.c > b.c:
            a2dr = -dr
            a2dc = dc
            b2dr = dr
            b2dc = -dc
        else:
            raise("shouldn't have happened")

        return a, b, a2dr, a2dc, b2dr, b2dc

    def find_all_antinode_vectors(self):
        for k, v in self.nodes.items():
            for node_pair in it.permutations(v, r=2):
                a, b, a2dr, a2dc, b2dr, b2dc = self.find_antinode_vectors(node_pair[0], node_pair[1])

                self.antinodes.add(a)
                self.antinodes.add(b)

                ainbounds = True
                binbounds = True

                while ainbounds or binbounds:
                    a = Point(a.r + a2dr, a.c + a2dc)
                    b = Point(b.r + b2dr, b.c + b2dc)

                    if self.inbounds(a):
                        self.antinodes.add(a)
                    else:
                        ainbounds = False

                    if self.inbounds(b):
                        self.antinodes.add(b)
                    else:
                        binbounds = False

        return(len(self.antinodes))

    def find_all_antinodes(self):
        for k, v in self.nodes.items():
            print(f"Checking out {k}")
            for node_pair in it.permutations(v, r=2):
                a, b = self.find_antinodes(node_pair[0], node_pair[1])

                if self.inbounds(a):
                    print(a)
                    self.antinodes.add(a)
                if self.inbounds(b):
                    print(b)
                    self.antinodes.add(b)

        return(len(self.antinodes))

    def map_debug(self):
        map = []
        # for h in range(self.height):
        #     s = ['.'] * self.width
        #     map.append(s)
        for row in self.rawmap:
            map.append([c for c in row])

        for node in self.antinodes:
            r, c = node
            map[r][c] = '#'

        for row in map:
            print(''.join(row))




map = Map(inp)

p1 = map.find_all_antinodes()
map.map_debug()

print('''============
......#....#
...#....0...
....#0....#.
..#....0....
....0....#..
.#....A.....
...#........
#......#....
........A...
.........A..
..........#.
..........#.''')

print('=============================')

p2 = map.find_all_antinode_vectors()
map.map_debug()
print('''============
##....#....#
.#.#....0...
..#.#0....#.
..##...0....
....0....#..
.#...#A....#
...#..#.....
#....#.#....
..#.....A...
....#....A..
.#........#.
...#......## ''')



























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
