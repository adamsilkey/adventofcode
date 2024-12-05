#! /usr/bin/env python3

YEAR = "2024"
AOC_DAY = "05"

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
from math import lcm, prod

DEBUG = True

__start_time = perf_counter()

inp = load_file(filename)

p1 = p2 = 0


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

raw_rules, raw_printruns = load_file(filename).split('\n\n')

raw_rules = [line for line in raw_rules.split('\n')]
raw_printruns = [line for line in raw_printruns.split('\n')]

printruns = []
for line in raw_printruns:
    printruns.append([int(a) for a in line.split(',')])

rules = dict()

comprules = set()

for line in raw_rules:
    # print(line)
    a, _, b = line.partition('|')
    a = int(a)
    b = int(b)
    if a not in rules:
        rules[a] = [b]
    else:
        rules[a].append(b)

    comprules.add((a,b))

# for k, v in rules.items():
#     print(k, v)

# for line in printruns:
#     print(line)

bad_regexs = dict()
# bad_regexs = []

for k in rules:
    for v in rules[k]:
        bad_regexs[(k,v)] = re.compile(f"{v},.*{k}")

# print(bad_regexs)

badlines = []

for line in printruns:
    # print(line)
    rawline = ','.join([str(i) for i in line])
    for match in bad_regexs.values():
        if match.search(rawline):
            # print("Bad!")
            badlines.append(line)
            break
    else:
        middle = line[len(line)//2]
        # print(middle)
        p1 += middle
    # rawline = ','.join(line)
    # print(rawline)



#=============== P2

def compare(a, b):
    print(a,b)
    if (a,b) in comprules:
        return -1
    elif (b,a) in comprules:
        print('swap them!')
        return 1
    else:
        return 0

from functools import cmp_to_key

for line in badlines:
    print('===========')
    print(line)
    print("start sorting")
    line = sorted(line, key=cmp_to_key(compare))
    print(line)
    middle = line[len(line)//2]
    print(middle)
    p2 += middle




























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
