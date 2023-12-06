#! /usr/bin/env python3

YEAR = '2023'
AOC_DAY = '06'

import sys

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


import functools
import itertools as it
import re
import sys
from collections import Counter, defaultdict, deque, namedtuple
from dataclasses import dataclass
from math import prod


inp = load_lines(filename)
times = [int(time) for time in inp[0].split(":")[1].split()]
distances = [int(distance) for distance in inp[1].split(":")[1].split()]

Race = namedtuple("Race", "time distance")

races = [Race(*race) for race in zip(times, distances)]

def calc_winners(race: Race):
    winners = []
    for speed in range(race.time+1):
        time = race.time - speed
        if time * speed > race.distance:
            winners.append(speed)
    
    return len(winners)

print(f"Part 1: {prod(calc_winners(race) for race in races)}")

time = int("".join(str(time) for time in times))
distance = int("".join(str(dist) for dist in distances))

losers = 0
for speed in range(time+1):
    t = time - speed
    if t * speed <= distance:
        losers += 1

    else:
        break

p2 = time - losers - losers + 1

"""
There are three general approaches to Day 06 - Part 2:
    
- O(n) Brute force (find all winners)
- O(n) Brute force (find the losers)
- O(1) Quadratic formula

In practice, finding all the losers is significantly faster than
finding all the winners, as you have to check for far fewer items.

Below, you can see benchmark difference in pure cycles between
brute force (winners) and brute force (losers).
"""

print(f"Part 2 time: {time:,}")
print(f"Part 2 - cycles to find 1/2 of losers: {losers:,}")
print(f"Part 2 - cycles to find all the winners: {losers + p2:,}")
print()
print(f"Part 2 Puzzle Solution: {p2}")
















if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
