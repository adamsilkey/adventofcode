#! /usr/bin/env python3.11

YEAR = '2022'
AOC_DAY = '06'

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


p = load_file()
# n = 4
n = 14

for idx, _ in enumerate(p):
    if len(set(p[idx:idx+n])) == n:
        print(idx+n)
        break
    






































if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
