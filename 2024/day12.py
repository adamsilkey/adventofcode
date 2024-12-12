#! /usr/bin/env python3

YEAR = "2024"
AOC_DAY = "12"

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

# Point = namedtuple("Point", ["r", "c"])

# compass = dict(
#     NW = Point(-1, -1),
#     N = Point(-1, 0),
#     NE = Point(-1, 1),
#     W = Point(0, -1),
#     E = Point(0, 1),
#     SW = Point(1, -1),
#     S = Point(1, 0),
#     SE = Point(1, 1),
# )

p1 = p2 = 0




class Point:
    CARDINAL = ['N', 'E', 'S', 'W']

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

    def print(self):
        map = []
        for row in self.rawmap:
            map.append([c for c in row])

        for node in self.antinodes:
            r, c = node
            map[r][c] = '#'

        for row in map:
            print(''.join(row))


    # def find_garden_plot(self, point: Point, veggie: str = None, plot: set = None, perimeter: int = None):
    #     # Base case
    #     if plot is None:
    #         plot = set()
    #     if perimeter is None:
    #         perimeter = 0
    #     if veggie is None:
    #         veggie = self.grid[point]

    #     # add point to plot
    #     self.plot.add(point)

    #     check_next = set()

    #     for d in Point.CARDINAL:
    #         next_point = point.check(d)

    #         if next_point in self.plot:
    #             continue

    #         if self.inbounds(next_point) and self.grid[next_point] == veggie:
    #             if next_point not in self.plot:
    #                 check_next.add(next_point)
    #         else:
    #             perimeter += 1

    def bfs(self, point: Point):

        queue = deque([point])
        plot = set() #aka visited
        seen = set()
        sides = dict()
        perimeter = set()
        veggie = self.grid[point]

        while queue:
            point = queue.popleft()
            # print(f"Checking {point}")
            plot.add(point)

            for d in Point.CARDINAL:
                # if point == Point(2,2) and d == 'W':
                #     print('what the FUUUUUUCK')
                np = point.check(d)
                perimeter_key = (np, d)
                if np in plot or perimeter_key in perimeter or perimeter_key in seen:
                    continue

                # Add to seen, don't check it again
                seen.add(perimeter_key)

                if not self.inbounds(np) or not self.grid[np] == veggie:
                    # print(np)
                    # try:
                    #     print(f"differnet plot found: {self.grid[np]}")
                    # except KeyError:
                    #     print("ou of bounds")

                    perimeter.add(perimeter_key) ## Need to add both the node and the direction we're looking
                    # print(f"perimeter: {perimeter_key}")
                    # input()

                    ## Add sides
                    if d in ['N', 'S']:
                        key = (np.r, d)
                        if key not in sides:
                            sides[key] = []
                        sides[key].append(np.c)
                    elif d in ['E', 'W']:
                        key = (np.c, d)
                        if key not in sides:
                            sides[key] = []
                        sides[key].append(np.r)

                    continue

                if np not in plot:
                    # print(f'adding to queue: {np}')
                    queue.append(np)
                else:
                    raise('uh wat')

        # Just go over it a second time
        total_sides = 0
        for k, v in sides.items():
            total_sides += 1
            print(k)
            v.sort()
            i = v.pop()
            while v:
                n = v.pop()
                if i - n > 1:
                    total_sides += 1
                i = n

        print(f"Veggie: {veggie}. Area: {len(plot)}. Perimeter: {len(perimeter)}. Sides: {total_sides}")
        return plot, perimeter, total_sides

    def run(self):
        p1 = p2 = 0
        visited = set()
        for k, v in self.grid.items():
            if k not in visited:
                print(f"Looking at a plot of land! {k}: {v}")
                plot, perimeter, sides = self.bfs(k)
                p1 += len(plot) * len(perimeter)
                p2 += len(plot) * sides
                visited |= plot

        return p1, p2







inp = load_file(filename)

map = Map(inp)

p1, p2 = map.run()











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
