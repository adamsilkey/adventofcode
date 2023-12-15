#! /usr/bin/env python3

YEAR = "2023"
AOC_DAY = "15"

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


inp = load_file(filename).split(',')


def hash_(s: str):
    value = 0
    for c in s:
        c = ord(c)
        value += c
        value *= 17
        value %= 256
    
    return value

p1 = 0
for s in inp:
    p1 += hash_(s)

print(f"{p1=}")

Label = namedtuple("Label", "name box op focal")

labels: list[Label] = []
for label in inp:
    if '=' in label:
        name = label[:-2]
        op = label[-2]
        focal = int(label[-1])
    else:
        name = label[:-1]
        op = label[-1]
        focal = None

    labels.append(Label(name, hash_(name), op, focal))

boxes = [[] for _ in range(256)]

for label in labels:
    if label.op == '=':
        for idx, existing_label in enumerate(boxes[label.box]):
            if existing_label[0] == label.name:
                boxes[label.box][idx] = (label.name, label.focal)
                break
        else: # nobeak
            boxes[label.box].append((label.name, label.focal))
    else:
        for idx, existing_label in enumerate(boxes[label.box]):
            if existing_label[0] == label.name:
                boxes[label.box].pop(idx)

### focusing power
p2 = 0
for boxnum, box in enumerate(boxes):
    for slotnum, slot in enumerate(box, start=1):
        power = 1 + boxnum
        power *= slotnum
        power *= slot[1]


        p2 += power
print(f"{p2=}")




























if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
print("Execution time:", perf_counter() - __start_time)
print()
