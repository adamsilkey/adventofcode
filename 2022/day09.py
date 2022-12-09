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
    UL = Point(-1, 1),
    U = Point(0, 1),
    UR = Point(1, 1),
    L = Point(-1, 0),
    R = Point(1, 0),
    DL = Point(-1, -1),
    D = Point(0, -1),
    DR = Point(1, -1),
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

        return self

    def tail_move(self, head):

        dx = (head.x - self.x) // 2
        dy = (head.y - self.y) // 2

        if head.x == self.x:
            self.y = head.y - dy
        elif head.y == self.y:
            self.x = head.x - dx
        else:
            # move diagonal
            if head.x > self.x:
                dx = 1
            elif head.x < self.x:
                dx = -1
            if head.y > self.y:
                dy = 1
            elif head.y < self.y:
                dy = -1
            self.x += dx
            self.y += dy

        # if dx and dy:
        #     self.x = head.x - dx
        #     self.y = head.y - dy
        # elif dx:
        #     self.x = head.x - dx
        #     self.y = head.y
        # elif dy:
        #     self.x = head.x
        #     self.y = head.y - dy
        return self
    
    def rope_move(self, dx, dy):
        self.x += dx
        self.y += dy
        pass


# head = Rope(0,0)
# tail = Rope(0,0)
# seen = set(Point(0,0))

def need_move(head, tail):
    # print(head)
    # print(tail)
    if abs(head.x - tail.x) > 1: 
        return True
    elif abs(head.y - tail.y) > 1:
        return True
    return False

# print(need_move(head, tail))

# p = load_lines(r"input/09a.test")

knotrope = [Rope(0,0) for _ in range(10)]
print(knotrope)
seen = set()
for line in p:
    # print("====================")
    # print(f"New move instruction {line}")
    direction, distance = line.split()
    for _ in range(int(distance)):

        # first, move the head
        # print(f'----- Head moving {direction} {_ + 1}------')
        knotrope[0].move(direction)

        # check each knot in turn
        for idx, _ in enumerate(knotrope[1:], 1):
            # check if the next knot needs to move
            if need_move(knotrope[idx - 1], knotrope[idx]):
                knotrope[idx].tail_move(knotrope[idx - 1])
            
                seen.add((knotrope[9].x, knotrope[9].y))
    #         print(idx, knotrope[9])
    # print("----- Final positionn ---------")
    # print(knotrope)
    # print(len(seen))
    # input()

print(len(seen))






































if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
