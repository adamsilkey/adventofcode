#! /usr/bin/env python3

YEAR = "2024"
AOC_DAY = "02"

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

inp = load_lines(filename)

p1 = p2 = 0

reports = []

for line in inp:
    reports.append([int(i) for i in line.split()])


# for line in reports:
#     print(line)

def goodline(line):
    increasing = None
    for i, value in enumerate(line[:-1], start=1):
        if value > line[i]:
            if increasing is None:
                increasing = True
            elif increasing == False:
                break
            if abs(value - line[i]) > 3:
                break
        elif value < line[i]:
            if increasing is None:
                increasing = False
            elif increasing == True:
                break
            if abs(value - line[i]) > 3:
                break
        else:
            # not safe
            break
    else:
        print('good')
        return True
    return False

# print(p1)

for line in reports:
    print(line)
    bad = 0
    subset = []
    if goodline(line):
        p1 += 1
        p2 += 1
        print('good')
        continue
    else:
        # build optional lines
        for i in range(len(line)):
            subline = line[::]
            subline.pop(i)
            print(subline)
            if goodline(subline):
                print('p2 good')
                p2 += 1
                break

print(p1)
print(p2)









if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
print("Execution time:", perf_counter() - __start_time)
print()
