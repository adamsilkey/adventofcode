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

DIRS = dict(
    D = Node(1, 0),
    DL = Node(1, -1),
    DR = Node(1, 1),
)

class CavePart2:
    SAND_ORIGIN = Node(0, 500)

    def __init__(self, layout, left_col, right_col, lower_row):
        self.layout = layout
        self.left_col = left_col
        self.right_col = right_col
        self.lower_row = lower_row
        self.total_sand = 0

        self.grid = []
        for r in range(0, lower_row + 2): # one more row for part 2
            row = ['.' for c in range(1000)]
            self.grid.append(row)

        # add the infinite floor
        row = ['#' for c in range(1000)]
        self.grid.append(row)

        for rockform in layout:
            self.add_rock_formation(rockform)
    
    def inbounds(self, node: Node):
        return 0 <= node.r < self.dimension and self.left_col <= node.c < self.right_col

    @classmethod
    def fromfile(cls, filename):
        layout = []
        left_col = math.inf
        right_col = -math.inf
        lower_row = 0
        with open(filename) as f:
            for line in f:
                rockstructure = []
                coords = line.split(' -> ')
                # print(coords)
                for coord in coords:
                    c, r = coord.split(',')
                    c = int(c)
                    r = int(r)
                    rockstructure.append(Node(r, c))

                    # find the left/right bounds
                    if c < left_col:
                        left_col = c
                    if c > right_col:
                        right_col = c
                    if r > lower_row:
                        lower_row = r


                layout.append(rockstructure)
        
        return cls(layout, left_col, right_col, lower_row)

    def add_rock_formation(self, rockformation):
        for start, end in zip(rockformation[0:-1], rockformation[1:]):

            start = Node(start.r, start.c)
            end = Node(end.r, end.c)

            if start > end:
                end, start = start, end
            
            if start.c - end.c == 0:
                for r in range(start.r, end.r+1):
                    self.grid[r][start.c] = '#'
            else: # column
                for c in range(start.c, end.c+1):
                    self.grid[start.r][c] = '#'

    # def __repr__(self):
    #     return f"Cave(cavestring={self.cavestring})"

    def __str__(self):
        final_string = ''
        for row in self.grid:
            final_string += ''.join(row)
            final_string += '\n'
        
        return final_string
    
    def drop_sand(self):
        sand = Node(self.SAND_ORIGIN.r, self.SAND_ORIGIN.c)

        # check next
        while True:
            blocks = ['#', 'o']
            d = DIRS["D"]
            dr = DIRS["DR"]
            dl = DIRS["DL"]

            next = Node(sand.r + d.r, sand.c + d.c)
            if not self.grid[next.r][next.c] in blocks:
                sand = Node(next.r, next.c)
                continue
            next = Node(sand.r + dl.r, sand.c + dl.c)
            if not self.grid[next.r][next.c] in blocks:
                sand = Node(next.r, next.c)
                continue
            next = Node(sand.r + dr.r, sand.c + dr.c)
            if not self.grid[next.r][next.c] in blocks:
                sand = Node(next.r, next.c)
                continue

            self.grid[sand.r][sand.c] = 'o'
            self.total_sand += 1
            if sand == self.SAND_ORIGIN:
                print(self.total_sand)
                return True
            break

    def run(self):
        while True:
            if self.drop_sand():
                break




cave = CavePart2.fromfile(FILENAME)
# print(cave)
cave.run()
# print(cave)










sys.exit()

class CavePart1:
    SAND_ORIGIN = Node(0, 500)

    def __init__(self, layout, left_col, right_col, lower_row):
        self.layout = layout
        self.left_col = left_col
        self.right_col = right_col
        self.lower_row = lower_row
        self.p1 = 0

        self.grid = []
        for r in range(0, lower_row + 1):
            row = ['.' for c in range(self.left_col, self.right_col + 1)]
            self.grid.append(row)

        for rockform in layout:
            self.add_rock_formation(rockform)
    
    @classmethod
    def fromfile(cls, filename):
        layout = []
        left_col = math.inf
        right_col = -math.inf
        lower_row = 0
        with open(filename) as f:
            for line in f:
                rockstructure = []
                coords = line.split(' -> ')
                # print(coords)
                for coord in coords:
                    c, r = coord.split(',')
                    c = int(c)
                    r = int(r)
                    rockstructure.append(Node(r, c))

                    # find the left/right bounds
                    if c < left_col:
                        left_col = c
                    if c > right_col:
                        right_col = c
                    if r > lower_row:
                        lower_row = r


                layout.append(rockstructure)
        
        return cls(layout, left_col, right_col, lower_row)

    def add_rock_formation(self, rockformation):
        for start, end in zip(rockformation[0:-1], rockformation[1:]):

            start = Node(start.r, start.c - self.left_col)
            end = Node(end.r, end.c - self.left_col)

            if start > end:
                end, start = start, end
            
            if start.c - end.c == 0:
                for r in range(start.r, end.r+1):
                    self.grid[r][start.c] = '#'
            else: # column
                for c in range(start.c, end.c+1):
                    self.grid[start.r][c] = '#'

    # def __repr__(self):
    #     return f"Cave(cavestring={self.cavestring})"

    def __str__(self):
        final_string = ''
        for row in self.grid:
            final_string += ''.join(row)
            final_string += '\n'
        
        return final_string
    
    def drop_sand(self):
        sand = Node(self.SAND_ORIGIN.r, self.SAND_ORIGIN.c - self.left_col)

        # check next
        while True:
            blocks = ['#', 'o']
            d = DIRS["D"]
            dr = DIRS["DR"]
            dl = DIRS["DL"]

            next = Node(sand.r + d.r, sand.c + d.c)
            if not self.grid[next.r][next.c] in blocks:
                sand = Node(next.r, next.c)
                continue
            next = Node(sand.r + dl.r, sand.c + dl.c)
            if not self.grid[next.r][next.c] in blocks:
                sand = Node(next.r, next.c)
                continue
            next = Node(sand.r + dr.r, sand.c + dr.c)
            if not self.grid[next.r][next.c] in blocks:
                sand = Node(next.r, next.c)
                continue

            self.grid[sand.r][sand.c] = 'o'
            self.p1 += 1
            break

    def run(self):
        try:
            while True:
                self.drop_sand()
                # print(self)
                # input()
        except IndexError:
            print(self.p1)




cave = CavePart1.fromfile(FILENAME)
# print(cave)
cave.run()
print(cave)


































if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
