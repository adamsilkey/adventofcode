#! /usr/bin/env python3.11

YEAR = '2022'
AOC_DAY = '04'

import itertools as it
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



p = load_lines()

pairs = 0
for line in p:
    a,b = line.split(",")
    a1, a2 = a.split('-')
    b1, b2 = b.split('-')

    a1 = int(a1)
    a2 = int(a2)
    b1 = int(b1)
    b2 = int(b2)

    a = set(range(a1, a2+1))
    b = set(range(b1, b2+1))

    if (a & b):
        pairs += 1
    
    print(a)
    print(b)


print(pairs)

def partone():
    pairs = 0
    for line in p:
        a,b = line.split(",")
        a1, a2 = a.split('-')
        b1, b2 = b.split('-')

        a1 = int(a1)
        a2 = int(a2)
        b1 = int(b1)
        b2 = int(b2)

        if a1 >= b1 and a2 <= b2:
            print("a in b")
            print(a,b)
            pairs += 1
        elif b1 >= a1 and b2 <= a2:
            print("b in a")
            print(a,b)
            pairs += 1

    print(pairs)
































if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
