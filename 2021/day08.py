#! /usr/bin/env python3.10

YEAR = '2021'
AOC_DAY = '08'

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
    filename = f"{AOC_DAY}.test"
else:
    filename = f"{AOC_DAY}.in"

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


# filename

digit0 = Counter({"a": 4, "b": 2, "c": 2, "e": 2, "f": 2, "g": 4})
digit1 = Counter({"c": 2, "f": 2})   # Len 2
digit2 = Counter({"a": 4, "c": 2, "d": 4, "e": 2, "g": 4})
digit3 = Counter({"a": 4, "c": 2, "d": 4, "e": 2, "f": 2, "g": 4})
digit4 = Counter({"b": 2, "c": 2, "d": 4, "f": 2}) # Len 4
digit5 = Counter({"a": 4, "b": 2, "d": 4, "f": 2, "g": 4})
digit6 = Counter({"a": 4, "b": 2, "d": 4, "e": 2, "f": 2, "g": 4})
digit7 = Counter({"a": 4, "c": 2, "f": 2}) # Len 3
digit8 = Counter({"a": 4, "b": 2, "c": 2, "d": 4, "e": 2, "f": 2, "g": 4}) # Len 7
digit9 = Counter({"a": 4, "b": 2, "c": 2, "d": 4, "f": 2, "g": 4})

# 1 - 2
# 4 - 4
# 7 - 3
# 8 - 7

# 10 unique signals | 4 digit output value
SevenSegmentDisplay = namedtuple("SevenSegmentDisplay", ["signal", "output"])

def parse_input(filename):
    ll = load_lines(filename)

    displays = []

    for line in ll:
        signal, _, output = line.partition("|")
        _display = SevenSegmentDisplay(signal.strip().split(), output.strip().split())
        displays.append(_display)

    return(displays)
    

displays = parse_input(filename)

for disp in displays:
    print(disp)

def part_one(displays):
    count = 0
    for disp in displays:
        for out in disp.output:
            if len(out) in [2,3,4,7]:
                count += 1
    
    print(f"p1: {count}")

part_one(displays)