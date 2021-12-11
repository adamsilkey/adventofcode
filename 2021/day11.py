#! /usr/bin/env python3.10

YEAR = '2021'
AOC_DAY = '11'
DEBUG = True

import itertools as it
import sys
from collections import Counter, defaultdict, deque, namedtuple
from dataclasses import dataclass
from enum import Enum

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



ll = load_file(filename)








Point = namedtuple("Point", ["x", "y"])

directions = dict(
    NW = Point(-1, -1),
    N = Point(0, -1),
    NE = Point(1, -1),
    W = Point(-1, 0),
    E = Point(1, 0),
    SW = Point(-1, 1),
    S = Point(0, 1),
    SE = Point(1, 1),
)

class OctopusCavern:

    def __init__(self, cavern_map: str):
        self.grid = []
        for line in cavern_map.strip().splitlines():
            self.grid.append([int(i) for i in line])
        
        self.dimension = len(self.grid)

    def inbounds(self, point: Point):
        return 0 <= point.x < self.dimension and 0 <= point.y < self.dimension
    
    def increment(self, pt: Point) -> bool:
        self.grid[pt.y][pt.x] += 1

        return self.grid[pt.y][pt.x] > 9

    def step_one(self, debug=False):
        # First, the energy level of each octopus increases by 1
        for y, row in enumerate(self.grid):
            for x, _ in enumerate(row):
                self.increment(Point(x, y))
        if debug: self.print()
        if debug: input()

    # Step Two
    def flash(self, pt: Point, flashed: set, debug=False):

        if pt in flashed:
            return flashed

        flashed.add(pt)

        for d in directions.values():
            adjacent = Point(pt.x + d.x, pt.y + d.y)
            if debug: print(adjacent)
            if self.inbounds(adjacent) and self.increment(adjacent): # and adjacent not in flashed:
                if debug: print("Flashing")
                # ESTUPIDO ------> self.flash(pt, flashed, debug)
                self.flash(adjacent, flashed, debug)
            elif debug:
                print(f"{self.inbounds(adjacent)=}")
                if self.inbounds(adjacent):
                    self.print()
                input()

            

        return flashed

    def step_two(self, debug = False) -> int:
        flashed = set()
        for y, row in enumerate(self.grid):
            for x, i in enumerate(row):
                if debug: print(Point(x,y), i)
                if debug: self.print()
                if debug: input()
                if i > 9:
                    if debug: print("flash")
                    flashed = self.flash(Point(x,y), flashed, debug)

        return len(flashed)

    # Step Three
    def step_three(self, debug=False):
        for y, row in enumerate(self.grid):
            for x, i in enumerate(row):
                if i > 9:
                    self.grid[y][x] = 0

    def print(self):
        for y, row in enumerate(self.grid):
            for x, i in enumerate(row):
                if i > 9:
                    i = ' '
                    #  raise ValueError(f"{i} is too high! Coordinate: ({x},{y})")
                print(i, end='')
            print()
        
        # Make a new line to demarcate the end of the grid
        print()

    def cycle(self, pprint=False, debug1=False, debug2=False, debug3=False):
        if debug1: print("Step One:")
        self.step_one(debug1)

        if debug2: print("Step Two:")
        flashed_total = self.step_two(debug2)

        if debug3: print("Step Three:")
        self.step_three(debug3)

        if pprint:
            self.print()

        return flashed_total

    def simulate(self, rounds):
        flashed_total = 0
        for _ in range(rounds):
            flashed_total += self.cycle()

        return flashed_total



p1_test = '''
11111
19991
19191
19991
11111
'''.strip()

p1_test = '''
284
257
589
'''

def part1_test(p1_test):

    p1_test = OctopusCavern(p1_test)

    p1_test.print()
    p1_test.cycle(pprint=True, )
    p1_test.cycle(pprint=True)

# part1_test(p1_test)

# import sys;sys.exit()

p1 = OctopusCavern(ll)

print(f"p1: {p1.simulate(100)}")

p2 = OctopusCavern(ll)

counter = 0
while True:
    counter += 1
    if p2.cycle() == 100:
        print(f"p2: {counter}")
        break