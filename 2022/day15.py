#! /usr/bin/env python3.11

YEAR = '2022'
AOC_DAY = '15'

import itertools as it
import heapq
import math
import re
import sys
from collections import Counter, defaultdict, deque, namedtuple
from contextlib import suppress
from dataclasses import dataclass
from functools import cmp_to_key
from itertools import zip_longest
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



# monkeystrings = p.split('\n\n')
Node = namedtuple("Node", ["r", "c"])
Point = namedtuple("Point", ["x", "y"])
# from string import ascii_lowercase


p = load_lines(FILENAME)


def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

points = {}
for line in p:
    a, b, c, d = map(int, re.findall(r'\-?\d+', line))
    points[Point(a,b)] = Point(c,d)


manhattans = {}

for sensor, beacon in points.items():
    print(sensor, beacon)
    print(manhattan(sensor, beacon))
    manhattans[sensor] = manhattan(sensor, beacon)

# exit()
def p1(sensor, manhattan):
    if test:
        ROW = 10
    else:
        ROW = 2_000_000
    if abs(sensor.y - manhattan) > ROW:
        # print(sensor)
        # sys.exit()
        print('not here boss')
        return None
    
    # get how much y has possibly moved
    y_travel = abs(ROW - sensor.y)

    # get the total x value
    remainder = abs(manhattan - y_travel)
    x_travel = sensor.x + remainder
    x2_travel = sensor.x - remainder

    return Point(x_travel, ROW), Point(x2_travel, ROW)


detected_spots = set()

# test
# manhattans = {Point(8,7): 9}
# print(manhattans)

for sensor, man in manhattans.items():
    res = p1(sensor, man)
    if res is not None:
        start, end = res[0], res[1]
        if start > end:
            end, start = start, end
        
        for x in range(start.x, end.x + 1):
            detected_spots.add(Point(x, start.y))

for sensor, beacon in points.items():
    try:
        detected_spots.remove(sensor)
    except KeyError:
        pass
    try:
        detected_spots.remove(beacon)
    except KeyError:
        pass


# lis = []
# for spot in detected_spots:
#     lis.append(spot.x)
#     print(spot)
# print(sorted(lis))
# print(detected_spots)
print(len(detected_spots))

# 4218893 (which is at +1)





































if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
