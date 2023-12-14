#! /usr/bin/env python3

YEAR = "2023"
AOC_DAY = "14"

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

system = [[c for c in row] for row in inp]

ROUND = 'O'
CUBE = '#'
EMPTY = '.'


Point = namedtuple("Point", "r c")

def rotate(system: list[list[str]]) -> list[list[str]]:
    return [col for col in zip(*system)]

def printmap(system):
    for row in system:
        print(''.join(row))

def slide(row: list[str]):
    new_row = []
    groups = ''.join(row).split(CUBE)
    for group in groups:
        rounds = [c for c in group if c == ROUND]
        new_row.extend(rounds)
        padding = len(group) - len(rounds)
        new_row.extend([EMPTY for _ in range(padding)])
        # if len(new_row) > 0:
        #     new_row.pop()

        new_row.append(CUBE)
    
    new_row.pop()
    return new_row

def slide_system(system):
    rotato = rotate(system)
    new_system = []
    for row in rotato:
        new_system.append(slide(row))
    
    printmap(new_system)
    new_system = rotate(new_system)
    print()
    printmap(new_system)
    new_system = rotate(new_system)
    print()
    printmap(new_system)
    new_system = rotate(new_system)
    print()
    printmap(new_system)

    return new_system



def solve(system):
    res = 0
    for i, row in enumerate(system[::-1], 1):
        print(row)
        count = row.count(ROUND)
        print(i, count)
        res += count * i
    
    print(res)
    return res

p1system = slide_system(system)
print()
printmap(p1system)
solve(p1system)
































if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
print("Execution time:", perf_counter() - __start_time)
print()
