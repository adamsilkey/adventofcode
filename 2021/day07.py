#! /usr/bin/env python3.10

TEST = False
# TEST = True

AOC_DAY = '07'

import itertools as it
from collections import deque
from dataclasses import dataclass
from statistics import median


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


if TEST:
    filename = f"{AOC_DAY}.test"
else:
    filename = f"{AOC_DAY}.in"



print(median(ll))

# median = 321

from statistics import median

ll = [int(i) for i in load_file(filename).split(',')]

total = 0
for i in ll:
    total += abs(median(ll) - i)

print(total)

average = sum(ll)/len(ll)
average = round(average)
print(average)

# average = 458 #92439832
average = 457

part2 = 0
for i in ll:
    difference = abs(average - i)
    for i in range(difference + 1):
        part2 += i

print(part2)

