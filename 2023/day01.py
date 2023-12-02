#! /usr/bin/env python3.11

YEAR = '2023'
AOC_DAY = '01'

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



print(filename)

inp = load_lines(filename)
# print(inp)

def part1():
    import re
    sum = 0
    for line in inp:
        digits = "".join(re.findall(r'\d+', line))
        sum += int(f"{digits[0]}{digits[-1]}")

    print(sum)

digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

import re
# nums = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine))', "zoneight234")
# print(nums)
sum = 0
for line in inp:
    nums = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', line)
    print(nums)
    try:
        a = nums[0]
        b = nums[-1]
        if a in digits:
            a = digits[a]
        if b in digits:
            b = digits[b]
        calibration_value = f"{a}{b}"
        print(calibration_value)
        sum += int(f"{a}{b}")
    except IndexError:
        pass

print(sum)
























if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
