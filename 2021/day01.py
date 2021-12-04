#! /usr/bin/env python3.10
import itertools as it

from collections import deque

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


def test():
    print(load_file("int_test.txt"))
    print(load_lines("int_test.txt"))
    print(load_ints("int_test.txt"))


### Load day 1 from 01.in

day1 = load_ints("01.in")

## part 1

prev = 193
count = 0

for i in day1[1:]:
    if i > prev:
        count += 1
    prev = i

print(f"day 1, part 1: {count}")


## part 2

count = 0

for i in day1:
    try:
        a = day1[i] + day1[i+1] + day1[i+2]
        b = day1[i+1] + day1[i+2] + day1[i+3]

        if b > a:
            count += 1

    except IndexError:
        break

print(f"day 1, part 2: {count}")

count = 0

for i in day1[:-3]:
    if sum(day1[i+1:i+4]) > sum(day1[i:i+3]):
        count += 1

print(f"day 1, part 2: {count}")