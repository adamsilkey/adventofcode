#! /usr/bin/env python3

YEAR = "2024"
AOC_DAY = "07"

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


inp = load_lines(filename)

p1 = p2 = 0

data = dict()

for line in inp:
    a, _, b = line.partition(':')
    data[int(a)] = [int(n) for n in b.strip().split()]


possible = 0
match = 0
notpossible = 0
for k, v in data.items():
    print(k, v)

    l = len(v) - 1
    combinations = [s for s in it.product('*+', repeat=l)]

    for combo in combinations:
        combo = [c for c in combo]
        combo.append('+')
        test = deque([c for items in zip(v, combo) for c in items])
        test.append(0)

        n = test.popleft()
        while test:
            op = test.popleft()
            next = test.popleft()
            if op == '*':
                n *= next
            elif op == '+':
                n += next

        if k == n:
            print('found one')
            p1 += n
            break








# print(possible)
# print(match)
# print(notpossible)




























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
