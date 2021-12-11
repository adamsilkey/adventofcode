#! /usr/bin/env python3.10

YEAR = '2021'
AOC_DAY = '11'

import sys
from collections import namedtuple

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

    def step_one(self):
        # First, the energy level of each octopus increases by 1
        for y, row in enumerate(self.grid):
            for x, _ in enumerate(row):
                self.increment(Point(x, y))

    # Step Two
    def flash(self, pt: Point, flashed: set):

        if pt in flashed:
            return flashed

        flashed.add(pt)

        for d in directions.values():
            adjacent = Point(pt.x + d.x, pt.y + d.y)
            if self.inbounds(adjacent) and self.increment(adjacent): 
                self.flash(adjacent, flashed)

        return flashed

    def step_two(self) -> int:
        flashed = set()
        for y, row in enumerate(self.grid):
            for x, i in enumerate(row):
                if i > 9:
                    flashed = self.flash(Point(x,y), flashed)

        return len(flashed)

    # Step Three
    def step_three(self):
        for y, row in enumerate(self.grid):
            for x, i in enumerate(row):
                if i > 9:
                    self.grid[y][x] = 0

    def print(self):
        for y, row in enumerate(self.grid):
            for x, i in enumerate(row):
                if i > 9:
                    i = ' '
                print(i, end='')
            print()
        
        print()  # Make a new line to demarcate the end of the grid

    def cycle(self, pprint=False):
        self.step_one()

        flashed_total = self.step_two()

        self.step_three()

        if pprint:
            self.print()

        return flashed_total

    def simulate(self, rounds):
        flashed_total = 0
        for _ in range(rounds):
            flashed_total += self.cycle()

        return flashed_total


p1 = OctopusCavern(ll)
print(f"p1: {p1.simulate(100)}")

p2 = OctopusCavern(ll)
counter = 0
while True:
    counter += 1
    if p2.cycle() == 100:
        print(f"p2: {counter}")
        break
