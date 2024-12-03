#! /usr/bin/env python3

YEAR = "2024"
AOC_DAY = "03"

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

pattern = re.compile(r"mul\(\d+,\d+\)")

from operator import mul

for line in inp:
    for match in pattern.finditer(line):
        # print(match.group(0))
        a, b = re.findall(r"\d+", match.group(0))
        # print(a, b)
        p1 += int(a) * int(b)
        # sub = line[match.start:match.end]
        # print(sub)

p2pattern = re.compile(r"do\(\)|don't\(\)")

for line in inp:
    good_index = deque([0])

    start_matching = True
    for match in p2pattern.finditer(line):
        print(match)
        if match.group(0).startswith('don') and start_matching == True:
            start_matching = False
            print(match.group(0))
            good_index.append(match.start())
        elif match.group(0).startswith('do(') and start_matching == False:
            print(match.group(0))
            good_index.append(match.start())
            start_matching = True

    print(good_index)

    pattern = re.compile(r"mul\(\d+,\d+\)")
    while len(good_index) > 1:
        start = good_index.popleft()
        end = good_index.popleft()

        for match in pattern.finditer(line[start:end]):
            a, b = re.findall(r"\d+", match.group(0))
            p2 += int(a) * int(b)

    if len(good_index) == 1:
        start = good_index.popleft()
        for match in pattern.finditer(line[start:]):
            a, b = re.findall(r"\d+", match.group(0))
            p2 += int(a) * int(b)



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
