#! /usr/bin/env python3.11

YEAR = '2022'
AOC_DAY = '14'

import itertools as it
import heapq
import math
import re
import sys
from collections import Counter, defaultdict, deque, namedtuple
from contextlib import suppress
from dataclasses import dataclass
from functools import cmp_to_key
from itertools import zip_longest
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



# monkeystrings = p.split('\n\n')
Node = namedtuple("Node", ["r", "c"])
# from string import ascii_lowercase


p = load_file(FILENAME)


# 4     5  5
# 9     0  0
# 4     0  3
cavestring = '''
0 ......+...
1 ..........
2 ..........
3 ..........
4 ....#...##
5 ....#...#.
6 ..###...#.
7 ........#.
8 ........#.
9 #########.
'''.strip()

class Cave:

    def __init__(self, cavestring, corner_r, corner_c):
        self.cave = []
        for line in cavestring.splitlines():
            # print(line)
            num, caveicons = line.split()
            self.cave.append([icon for icon in caveicons])
    
    def __repr__(self):
        return f"Cave(cavestring={self.cavestring})"

    def __str__(self):
        final_string = ''
        for row in self.cave:
            final_string += ''.join(row)
            final_string += '\n'
        
        return final_string


    # def build_cave(self, cavestring, corner_r, corner_c):

cave = Cave(cavestring, 0, 494)
print(cave)


































if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
