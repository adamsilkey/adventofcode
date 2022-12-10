#! /usr/bin/env python3.11

YEAR = '2022'
AOC_DAY = '10'

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

p = deque(load_lines(FILENAME))

Point = namedtuple("Point", ["x", "y"])



def addx(v):
    return v

register_x = 1
cycles = 1
stack = {}
active = 0
total = 0

while True:
    # start of cycle
    cycles += 1
    if not p:
        break
    if not active:
        ins = p.popleft()
        if ins != 'noop':
            ins, value = ins.split()
            active = 1
    elif active:
        active -= 1
        if active == 0:
            register_x += int(value)
    
    if cycles in [20, 60, 100, 140, 180, 220]:
        total += (register_x * cycles)

    # end of cycle

print(total)

    































if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
