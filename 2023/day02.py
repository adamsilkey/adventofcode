#! /usr/bin/env python3

YEAR = '2023'
AOC_DAY = '02'

import functools
import itertools as it
import re
import sys
from collections import Counter, defaultdict, deque, namedtuple
from dataclasses import dataclass

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



inp = load_lines(filename)

p1_max = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

p1 = 0
p2 = 0

for line in inp:
    game_id, _, cubes = line.partition(':')
    game_id = re.search('\d+', game_id)[0]

    max_colors = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    for subset in cubes.split(";"):
        for color in subset.split(","):
            n, color = color.strip().split()
            max_colors[color] = max(int(n), max_colors[color])
    
    if Counter(max_colors) <= Counter(p1_max):
        p1 += int(game_id)
    p2 += functools.reduce(lambda x, y: x*y, max_colors.values())

print(f"{p1=}")
print(f"{p2=}")























if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
