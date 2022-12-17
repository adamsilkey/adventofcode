#! /usr/bin/env python3.11

YEAR = '2022'
AOC_DAY = '17'

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



Node = namedtuple("Node", ["r", "c"])
Point = namedtuple("Point", ["x", "y"])
Range = namedtuple("Range", ["start", "end"])

p = load_file(FILENAME)

print(p)







from itertools import cycle



hline = set([
        Node(4,2), Node(4,3), Node(4,4), Node(4,5),
        ])

cross = set([
                   Node(6,3),
        Node(5,2), Node(5,3), Node(5,4),
                   Node(4,3),
                   ])

lshape = set([
                              Node(6,4),
                              Node(5,4),
        Node(4,2), Node(4,3), Node(4,4),
        ])

vline = set([
        Node(7,2),
        Node(6,2),
        Node(5,2),
        Node(4,2),
        ])

box = set([
        Node(5,2), Node(5,3),
        Node(4,2), Node(4,3),
        ])


class Cave:

    shapes = cycle([hline, cross, lshape, vline, box])

    @classmethod
    def fromstring(cls, cyclestring):
        return cls(cycle(cyclestring))

    def __init__(self, cycle):
        self.blocks = set()
        for i in range(7):
            self.blocks.add(Node(0,i))

        self.highest = 0
        self.cycle = cycle

    def spawn(self):
        return self.move(next(self.shapes), self.highest, 0)
    
    def move(self, shape, dr, dc):
        xshape = set()
        for node in shape:
            r = node.r + dr
            c = node.c + dc

            # If we are going to move out of bounds, just return the shape
            if c < 0 or c > 6:
                # print('moving out of bounds, returning shape')
                # print(c)
                return shape
            xshape.add(Node(r, c))

            # Check if we are going to hit an existing shape when moving
            # horizontally
            if dc and self.blocks.intersection(xshape):
                return shape

        return xshape

    def show(self):
        blocks = sorted(list(self.blocks))[::-1]
        current_row = blocks[0].r
        row = ['.' for _ in range(7)]
        for node in blocks:
            if node.r < current_row:
                current_row = node.r
                print(''.join(row))
                row = ['.' for _ in range(7)]

            row[node.c] = '#'


    def simulate(self, shape):

        while True:
            dc = next(self.cycle)
            # print(dc)
            if dc == '<': dc = -1
            if dc == '>': dc = 1
            # adjust all rocks in the direction
            shape = self.move(shape, 0, dc)
            # print(f"horizontal move {dc}")
            # print(shape)

            # move all rocks down, store in a potential move
            xshape = self.move(shape, -1, 0)
            # print(f"vertical move -1")
            # print(xshape)
            # print()
            # input()

            # check to see if these any of these new poitns overlap with
            # existing rocks
            if self.blocks.intersection(xshape):
                # add to overall set
                for node in shape:
                    self.blocks.add(node)

                    # set the new highest point
                    if node.r > self.highest:
                        self.highest = node.r

                return
            else:
                shape = xshape

    
    def run(self, rounds):
        # spawn shape
        for i in range(1, rounds + 1):
            if i % 100000 == 0:
                print(i)
            shape = self.spawn()
            self.simulate(shape)
            # print(sorted(list(self.blocks))[::-1])
            # self.show()
            # input()


        print(f"{self.highest=}")
        return self.highest


cave = Cave.fromstring(p)
cave.run(2022)

p2 = 1_000_000_000_000

cave.run(p2)

















'''
class Shape:

    def __init__(self, shape):
        self.shape = shape
        self.height = len(self.shape)
        self.width = len(self.shape[0]) # all shapes are square

    def __str__(self):

        str_ = ''
        for row in self.shape:
            str_ += ''.join(row)
            str_ += '\n'

        return str_


hline = Shape([[c for c in '####']])

cross = Shape([
        [' ', '#', ' '],
        ['#', '#', '#'],
        [' ', '#', ' ']
        ])

lshape = Shape([
        [' ', ' ', '#'],
        [' ', ' ', '#'],
        ['#', '#', '#']
        ])

vline = Shape([
        ['#'],
        ['#'],
        ['#'],
        ['#'],
        ])

box =   Shape([
        ['#', '#'],
        ['#', '#'],
        ])


from itertools import cycle
shapes = cycle([hline, cross, lshape, vline, box])

jets = cycle(p.strip())

# example of printing shapes
for i in range(10):
    shape = next(shapes)
    print(shape)



class Chamber:
    def __init__(self):
        self.grid = deque()
        self.left_edge = 2
        self.bottom_edge = 3
        for i in range(1_000_000):
            self.addrow()

    def addrow(self):
        new_row = [' ' for _ in range(7)]

        self.grid.appendleft(new_row)

    def __str__(self):
        str_ = ('+-------+\n')
        for row in self.grid:
            str_ += '|'
            str_ += ''.join(row)
            str_ += '|'
            str_ += '\n'
        str_ += '+-------+'

        return str_


chamber = Chamber()

# print(chamber)
print(len(chamber.grid))
'''


















































































if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")



exit()

