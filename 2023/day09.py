#! /usr/bin/env python3

YEAR = '2023'
AOC_DAY = '09'

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
from math import lcm, prod

DEBUG = True

__start_time = perf_counter()


inp = load_lines(filename)

histories = []
for line in inp:
    histories.append([int(i) for i in line.split()])


def make_stack(seq):
    stack = []
    while True:
        print(stack)
        stack.append(seq)
        if all(i == 0 for i in seq):
            if DEBUG:
                for l in stack:
                    print(l)
            break
        else:
            seq = [b - a for a, b in zip(seq, seq[1:])]
    
    return stack


def part_1(stack):
    stack = make_stack(stack)
    while stack:
        if DEBUG: print(stack)
        last = stack.pop()
        try:
            next_value = stack[-1][-1] + last[-1]
            stack[-1].append(next_value)
        except IndexError:
            break
            pass
    if DEBUG: print(next_value)
    return next_value

# part_1(make_stack(histories[1]))
# sys.exit()

p1 = 0
for his in histories:
    p1 += part_1(his)
print(p1)


























if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
print("Execution time:", perf_counter() - __start_time)
print()