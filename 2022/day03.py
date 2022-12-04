#! /usr/bin/env python3.11

YEAR = '2022'
AOC_DAY = '03'

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

total = 0
for line in p:
    midway = len(line) // 2
    sack1 = line[0:midway]
    sack2 = line[midway:]
    shared = set(sack1).intersection(set(sack2))

    for toy in shared:
        if toy.islower():
            prio = (ord(toy) - ord('a') + 1)
            total += prio
        else:
            prio = (ord(toy) - ord('A') + 27)
            total += prio
print(f"p1: {total}")

sacks, count, total = [], 0, 0
for line in p:
    sacks.append(line)
    count +=1 

    if count == 3:
        # find badge
        badge = set(sacks[0]).intersection(set(sacks[1])).intersection(set(sacks[2])).pop()

        sacks = []
        count = 0
        if badge.islower():
            prio = (ord(badge) - ord('a') + 1)
            total += prio
        else:
            prio = (ord(badge) - ord('A') + 27)
            total += prio

print(f"p2: {total}")






























if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
