#! /usr/bin/env python3.11

YEAR = '2022'
AOC_DAY = '09'

import itertools as it
import re
import sys
from collections import Counter, defaultdict, deque, namedtuple
from dataclasses import dataclass
from string import ascii_letters, ascii_lowercase, ascii_uppercase

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
    FILENAME = f"input/{AOC_DAY}.test"
else:
    FILENAME = f"input/{AOC_DAY}.in"

title = f"Advent of Code {YEAR} - Day {AOC_DAY} - {'Test' if test else 'Production'}"

print(f"=" * len(title))
print(title)
print(f"=" * len(title))

def load_file(filename: str = FILENAME) -> str:
    """Loads an AOC file, returns a string"""

    with open(filename) as f:
        return f.read().rstrip("\n")


def load_lines(filename: str = FILENAME) -> list[str]:
    """Returns a list of lines"""

    return load_file(filename).split("\n")


def load_ints(filename: str = FILENAME) -> list[int]:
    """Returns a list of ints"""

    return [int(i) for i in load_lines(filename)]


def load_comma_separated_ints(filename: str = FILENAME) -> list[int]:
    """Returns a list of ints from a comma separated list of ints"""

    return [int(i) for i in load_file(filename).strip().split(",")]



## Regex / list/map helpers
# number_of_stacks = max(map(int, stacks.pop().split()))
# qty, old, new = list(map(int, re.findall(r'\d+', move)))
#   - map(function, target)
#   - map needs to bec onverted to a list (or other object)
# Point = namedtuple("Point", ["x", "y"])

p = load_lines(FILENAME)

Point = namedtuple("Point", ["x", "y"])

DIRS = dict(
    U = Point(0, 1),
    L = Point(-1, 0),
    R = Point(1, 0),
    D = Point(0, -1),
)

class Knot:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Knot(x={self.x},y={self.y})"

    def move(self, direction):
        self.x += DIRS[direction].x
        self.y += DIRS[direction].y

    def tail_move(self, head):
        dx = 1 if head.x > self.x else -1
        dy = 1 if head.y > self.y else -1

        if head.x - self.x:
            self.x += dx
        if head.y - self.y:
            self.y += dy
    
    def need_move(self, head):
        if abs(head.x - self.x) > 1: 
            return True
        elif abs(head.y - self.y) > 1:
            return True
        return False


rope = [Knot(0,0) for _ in range(10)]
p1_seen = set((0,0))
p2_seen = set((0,0))

for line in p:
    direction, distance = line.split()
    for _ in range(int(distance)):
        rope[0].move(direction)
        for prev, knot in enumerate(rope[1:], 0):
            if knot.need_move(rope[prev]):
                knot.tail_move(rope[prev])
                p1_seen.add((rope[1].x, rope[1].y))
                p2_seen.add((rope[9].x, rope[9].y))
            else:
                break

print(f"p1: {len(p1_seen)}")
print(f"p2: {len(p2_seen)}")






































if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
