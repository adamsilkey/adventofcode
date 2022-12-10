#! /usr/bin/env python3.11

YEAR = '2022'
AOC_DAY = '10'

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



## Regex / list/map helpers
# number_of_stacks = max(map(int, stacks.pop().split()))
# qty, old, new = list(map(int, re.findall(r'\d+', move)))
#   - map(function, target)
#   - map needs to bec onverted to a list (or other object)
# Point = namedtuple("Point", ["x", "y"])

p = deque(load_lines(FILENAME))

Point = namedtuple("Point", ["x", "y"])



def addx(v):
    return v

# register_x = 1
# cycles = 1
# stack = {}
# active = 0
# total = 0

# while True:
#     # start of cycle
#     cycles += 1
#     if not p:
#         break
#     if not active:
#         ins = p.popleft()
#         if ins != 'noop':
#             ins, value = ins.split()
#             active = 1
#     elif active:
#         active -= 1
#         if active == 0:
#             register_x += int(value)
    
#     if cycles in [20, 60, 100, 140, 180, 220]:
#         total += (register_x * cycles)

#     # end of cycle

# print(total)


## p2


def checkpixel(cycles, register_x):
    pixel = register_x
    pos = cycles - 1

    # if I'm at 41 cycles, my pos needs to be 1
    pos = pos % 40

    # if pos in [pixel - 1, pixel, pixel + 1]:
    if pos in range(pixel-1, pixel+2):
        return True
    else:
        return False

# print(checkpixel(41, 1))
# sys.exit()

def print_crt(crt):
    for idx, c in enumerate(crt):
        if idx % 40 == 0:
            print("")
        print(c, end='')
        
crt = ['.' for _ in range(40*6)]

register_x = 1
active = 0
cycles = 0

while True:
    # start of cycle
    cycles += 1
    if not p:
        break
    if not active:
        ins = p.popleft()
        if ins != 'noop':
            ins, value = ins.split()
            active = 1
        if checkpixel(cycles, register_x):
            crt[cycles - 1] = '#'
    elif active:
        if checkpixel(cycles, register_x):
            crt[cycles - 1] = '#'
        active -= 1
        if active == 0:
            register_x += int(value)
    

    DEBUG = False
    if DEBUG:
        print_crt(crt)
        print()
        print(f"{register_x=}")
        print(f"{cycles=}")
        input()
    # else:
    #     print_crt(crt)
    
print_crt(crt)
    # if cycles in [20, 60, 100, 140, 180, 220]:
    #     total += (register_x * cycles)

    # end of cycle
    # print_crt(crt)
    # input()































if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
