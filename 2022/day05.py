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



p = load_lines()
# print(p)

stuff = {
    # Per the requests of advent of code, the actual puzzle input is considered
    # copyrighted, so I've removed the hardcoded values from here
    1 : list(),
    2 : list(),
    3 : list(),
    4 : list(),
    5 : list(),
    6 : list(),
    7 : list(),
    8 : list(),
    9 : list(),
}




# p2
for line in p:
    qty,old,new = re.findall(r'\d+', line)
    new_stack = []
    for i in range(int(qty)):
        if stuff[int(old)]:
            new_stack.append(stuff[int(old)].pop())
    new_stack.reverse()
    for crate in new_stack:
        stuff[int(new)].append(crate)
        

#p1
print(stuff)
for i in stuff:
    print(stuff[i][-1], end='')
# for line in p:
#     qty,old,new = re.findall(r'\d+', line)
#     for i in range(int(qty)):
#         stuff[int(new)].append(stuff[int(old)].pop())
        

# #p1
# print(stuff)




































if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
