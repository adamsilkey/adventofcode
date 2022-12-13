#! /usr/bin/env python3.11

YEAR = '2022'
AOC_DAY = '13'

import itertools as it
import heapq
import math
import re
import sys
from collections import Counter, defaultdict, deque, namedtuple
from contextlib import suppress
from dataclasses import dataclass
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



'''
## Regex / list/map helpers
# number_of_stacks = max(map(int, stacks.pop().split()))
# qty, old, new = list(map(int, re.findall(r'\d+', move)))
#   - map(function, target)
#   - map needs to bec onverted to a list (or other object)
# Point = namedtuple("Point", ["x", "y"])


    
    # @classmethod
    # def fromstring(cls, string):
    #     for line in string.split('\n'):
    #         match line.split():
    #             case 'Monkey', x:
    #                 id_ = int(x[0])
    #             case 'Starting', 'items:', *items:
    #                 items = deque([int(item.rstrip(',')) for item in items])
    #             case 'Operation:', *rest, operation, value:
    #                 if value.isdigit():
    #                     value = int(value)
    #             case 'Test:', *rest, divisor:
    #                 divisor = divisor
    #             case 'If', 'true:', *rest, truemonkey:
    #                 truemonkey = int(truemonkey)
    #             case 'If', 'false:', *rest, falsemonkey:
    #                 falsemonkey = int(falsemonkey)
        
    #     return cls(
    #         id_,
    #         items,
    #         operation,
    #         value,
    #         divisor,
    #         truemonkey,
    #         falsemonkey,
    #     )
'''

# monkeystrings = p.split('\n\n')
Node = namedtuple("Node", ["r", "c"])
# from string import ascii_lowercase


p = load_file(FILENAME)

global level 
level = 0

def checkpairs(packet_a, packet_b):
    global level
    print(f"{level=}")
    
    for left, right in zip_longest(packet_a, packet_b):
        if left is None:
            return True
        elif right is None:
            return False

        if isinstance(left, int) and isinstance(right, int):
            print(left, right)
            if left > right:
                return False
            elif left < right:
                return True
        
        elif isinstance(left, list) and isinstance(right, list):
            level += 1
            res = checkpairs(left, right)
            level -= 1
            print(level)
            if res is not None:
                return res
        
        else:
            if isinstance(left, int):
                left = [left]
            elif isinstance(right, int):
                right = [right]
            level += 1
            res = checkpairs(left, right)
            level -= 1
            print(level)
            if res is not None:
                return res
        



    # for a, b in zip_longest(packet_a, packet_b):
    #     if isinstance(a, int) and isinstance(b, int):
    #         print(a,b)
    #         if a > b:
    #             return False, level
    #         elif a < b:
    #             return True, level
    #         # elif a == b:
    #         #     return None
    #             # return None
    #         # check for None
        
    #     #check for mismatches
    #     if isinstance(a, int):
    #         a = [a]
    #     elif isinstance(b, int):
    #         b = [b]

    #     if isinstance(a, list) and isinstance(b, list):
    #         level += 1
    #         print(level)
    #         res = checkpairs(a, b, level)
    #         if res is None:
    #             continue
    #         result = res[0]
    #         level = res[1]
    #         level = level - 1
    #         if result is True:
    #             return True, level
    #         elif result is False:
    #             return False, level
        
    #     if level == 0:
    #         if a is None:
    #             return True, level
    #         if b is None:
    #             return False, level
    
    # if not packet_a:
    #     return True, level
    # elif not packet_b:
    #     return False, level
    
    # # return None, level




packetpairs = p.split('\n\n')
total = 0
for idx, packetpair in enumerate(packetpairs,1):
    a, b = packetpair.split('\n')
    packet_a = eval(a)
    packet_b = eval(b)
    print(f"Round {idx}",a, b)
    res = checkpairs(packet_a, packet_b)
    print(res)
    if res is None: raise
    if res is True:
        total += idx
    print()


print(total)



































if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
