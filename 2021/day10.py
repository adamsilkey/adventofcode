#! /usr/bin/env python3.10

YEAR = '2021'
AOC_DAY = '10'

import itertools as it
import sys
from collections import Counter, defaultdict, deque
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


ll = load_lines(filename)


pairs = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

# pairs_reversed = {v, k for k, v in pairs.items()}

left = set(pairs.keys())
right = set(pairs.values())


def scan_line(s: str):
    stack = []
    for c in s:
        if c in left:
            stack.append(c)
        else:
            check = stack.pop()
            if pairs[check] != c:
                # Found a bad egg
                # print(f"found a bad egg: {c}")
                return c

egg = scan_line("{([(<{}[<>[]}>{[]{[(<()>")

print(egg)

bad_eggs = []

for line in ll:
    if bad_egg := scan_line(line):
        bad_eggs.append(bad_egg)

print(bad_eggs)

syntax_score = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

p1 = 0
for c in bad_eggs:
    p1 += syntax_score[c]

print(f"{p1=}")

# ===== Part 2


def find_incomplete(s: str):
    stack = []
    for c in s:
        if c in left:
            stack.append(c)
        else:
            check = stack.pop()
            if pairs[check] != c:
                # Found a bad egg
                return None

    return [pairs[c] for c in stack[::-1]]


def autocomplete_score(s: str):
    _autocomplete_points = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }

    score = 0
    for c in s:
        score *= 5
        score += _autocomplete_points[c]

    print(f"{s}: {score}")
    return score

print(autocomplete_score("])}>"))
print(autocomplete_score("}}]])})]"))

p2 = []
for line in ll:
    if incomplete := find_incomplete(line):
        p2.append(autocomplete_score(incomplete))

p2.sort()
print(f"p2: {p2[len(p2)//2]}")

