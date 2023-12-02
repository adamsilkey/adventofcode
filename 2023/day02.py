#! /usr/bin/env python3

YEAR = '2023'
AOC_DAY = '02'

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

RED = 12
GREEN = 13
BLUE = 14

sum = 0

for line in inp:
    bad = False
    _, n, *colors = line.split()
    n = int(n[:-1])
    colors = ' '.join(colors)
    colors = colors.split(';')
    red = []
    green = []
    blue = []
    for colorset in colors:
        colors = colorset.strip().split()
        colors = list(zip(colors, colors[1:]))[::2]
        for color in colors:
            if color[1].startswith('red'):
                red.append(int(color[0]))
            if color[1].startswith('green'):
                green.append(int(color[0]))
            if color[1].startswith('blue'):
                blue.append(int(color[0]))
    print(max(red), max(green), max(blue))
    sum += max(red) * max(green) * max(blue)
        
print(sum)

# for line in inp:
#     bad = False
#     _, n, *colors = line.split()
#     n = int(n[:-1])
#     colors = ' '.join(colors)
#     colors = colors.split(';')
#     for colorset in colors:
#         red, green, blue = 0, 0, 0
#         colors = colorset.strip().split()
#         colors = list(zip(colors, colors[1:]))[::2]
#         for color in colors:
#             if color[1].startswith('red'):
#                 red += int(color[0])
#             if color[1].startswith('green'):
#                 green += int(color[0])
#             if color[1].startswith('blue'):
#                 blue += int(color[0])
#         print(red, green, blue)
#         if red > RED or green > GREEN or blue > BLUE:
#             bad = True
#     if not bad:
#         sum += n
        
#     #     if color[1].endswith(';'):
#     #         red, green, blue = 0, 0, 0
#     # else:
#     #     sum += n
    

#     # print(colors)
# print(sum)






















if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
