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

directions = dict(
    # NL = Point(-1, -1),
    U = Point(0, 1),
    # NR = Point(1, -1),
    L = Point(-1, 0),
    R = Point(1, 0),
    # DL = Point(-1, 1),
    D = Point(0, -1),
    # UR = Point(1, 1),
)

class Rope:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.x},{self.y}"

    def move(self, direction):
        self.x += directions[direction].x
        self.y += directions[direction].y

    def tail_move(self, direction, head):
        dx = directions[direction].x
        dy = directions[direction].y
        if direction in ['U', 'D']:
            self.x = head.x
            self.y = head.y - dy
        elif direction in ['L', 'R']:
            self.x = head.x - dx
            self.y = head.y


head = Rope(0,0)
tail = Rope(0,0)
seen = set(Point(0,0))

def need_move(head, tail):
    # print(head)
    # print(tail)
    if abs(head.x - tail.x) > 1: 
        return True
    elif abs(head.y - tail.y) > 1:
        return True
    return False

# print(need_move(head, tail))


for line in p:
    direction, distance = line.split()
    print(direction, distance)
    for _ in range(int(distance)):
        head.move(direction)
        print(f"{head=}")
        if need_move(head, tail):
            print("Need move!")
            tail.tail_move(direction, head)
            seen.add(Point(tail.x, tail.y))
        print(f"{tail=}")
        print()

print(len(seen))






































if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
