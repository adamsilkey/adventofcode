#! /usr/bin/env python3.11

YEAR = '2022'
AOC_DAY = '05'

import itertools as it
import re
import sys
from collections import Counter, defaultdict, deque, namedtuple
from dataclasses import dataclass
from string import ascii_letters, ascii_lowercase, ascii_uppercase

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



p = load_file()
stack_string, moves = p.split('\n\n')

def parse_stacks(stack_string: str):
    stacks = stack_string.split('\n')
    number_of_stacks = max(map(int, stacks.pop().split()))
    final_stacks = {i: [] for i in range(1, number_of_stacks + 1)}

    while stacks:
        line = stacks.pop()
        # We start with -3, so we can just always add 4 and not
        # worry about out of bounds errors
        idx = -3
        for i in range(1, number_of_stacks + 1):
            idx += 4
            if line[idx] != ' ':
                final_stacks[i].append(line[idx])

    return final_stacks


moves = moves.split('\n')

#p1
stacks = parse_stacks(stack_string)
for move in moves:
    qty, old, new = list(map(int, re.findall(r'\d+', move)))
    for i in range(qty):
        stacks[new].append(stacks[old].pop())

print("p1: ", end='')
for stack in stacks:
    print(stacks[stack][-1], end='')
print()

# p2
stacks = parse_stacks(stack_string)
for move in moves:
    qty, old, new = list(map(int, re.findall(r'\d+', move)))
    new_stack = []
    for i in range(qty):
        if stacks[old]:
            new_stack.append(stacks[old].pop())
    new_stack.reverse()
    for crate in new_stack:
        stacks[new].append(crate)
        
print("p2: ", end='')
for stack in stacks:
    print(stacks[stack][-1], end='')






































if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
