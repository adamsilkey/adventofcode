#! /usr/bin/env python3

YEAR = '2023'
AOC_DAY = '08'

import sys

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


import functools
import itertools as it
import re
import sys
from collections import Counter, defaultdict, deque, namedtuple
from dataclasses import dataclass
from math import prod


LR = namedtuple("LR", "L R")

inp = load_file(filename)

instructions, raw_nodes = inp.split("\n\n")

nodes = {}

for node in raw_nodes.splitlines():
    node, lr = node.split(' = ')

    left, right = lr.strip()[1:-1].split(", ")

    nodes[node] = LR(left, right)


# for node, lr in nodes.items():
#     print(node, lr)


# part 1
# node = 'AAA'

# steps = 0
# for direction_ in it.cycle(instructions.strip()):
#     # print(direction_)
#     steps += 1
#     if direction_ == 'L':
#         next_node = nodes[node].L
#     else:
#         next_node = nodes[node].R
    
#     node = next_node
#     if node == 'ZZZ':
#         print(steps)
#         break
        

# part 2

p2_paths = {node: None for node in nodes if node.endswith('A')}
p2 = [node for node in nodes if node.endswith('A')]

# print(p2_paths)

p2_total = 0
def p2_runner(node):
    steps = 0
    for direction_ in it.cycle(instructions.strip()):
        # print(direction_)
        steps += 1
        if direction_ == 'L':
            next_node = nodes[node].L
        else:
            next_node = nodes[node].R
        
        node = next_node
        if node.endswith('Z'):
            print(steps)
            return steps

lcms = (p2_runner(node) for node in p2)
from math import lcm
print(lcm(*lcms))
# for direction_ in it.cycle(instructions.strip()):
#     if direction_ == 'L':
#         new_p2 = [nodes[node].L for node in p2]
#     else:
#         new_p2 = [nodes[node].R for node in p2]
#     for node in p2:
#         if not node.endswith('Z'):
#             # print(node)
#             break
#     else: # no break
#         print(p2_total)
#         import sys;sys.exit()

#     p2 = new_p2
#     p2_total += 1


























if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
