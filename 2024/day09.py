#! /usr/bin/env python3

YEAR = "2024"
AOC_DAY = "09"

import sys
from time import perf_counter

if not (YEAR and AOC_DAY):
    print("!!! Set YEAR/AOC_DAY")
    sys.exit(1)


def fail():
    print("!!! Need to define -p for production or -t for test")
    sys.exit(1)


if len(sys.argv) != 2:
    fail()

match sys.argv[1].lower():
    case "-t":
        test = True
    case "-p":
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
from functools import cmp_to_key
from math import lcm, prod

DEBUG = True

__start_time = perf_counter()

Point = namedtuple("Point", ["r", "c"])

compass = dict(
    NW = Point(-1, -1),
    N = Point(-1, 0),
    NE = Point(-1, 1),
    W = Point(0, -1),
    E = Point(0, 1),
    SW = Point(1, -1),
    S = Point(1, 0),
    SE = Point(1, 1),
)

p1 = p2 = 0



class Map:

    def __init__(self, map: str):
        grid = []
        for line in map.strip().splitlines():
            grid.append([c for c in line])

        self.rawmap = grid
        self.grid = dict()

        for r, row in enumerate(grid):
            for c, char in enumerate(row):
                self.grid[Point(r,c)] = char


        self.height = len(grid)
        self.width = len(grid[0])

        self.p1 = 0
        self.p2 = 0

    def inbounds(self, point: Point):
        return 0 <= point.r < self.height and 0 <= point.c < self.width

    def onedge(self, point: Point):
        if point.r == 0 or point.r == self.height or point.c == 0 or point.c == self.width:
            return True
        else:
            return False

    def print(self):
        map = []
        for row in self.rawmap:
            map.append([c for c in row])

        for node in self.antinodes:
            r, c = node
            map[r][c] = '#'

        for row in map:
            print(''.join(row))


inp = load_file(filename)



diskmap = []
num = True
disk_id = 0
current = None
current_len = 0

for c in inp:
    c = int(c)
    if num:
        for i in range(c):
            diskmap.append(disk_id)

        disk_id += 1
    else:
        for i in range(c):
            diskmap.append(None)
    num = not num


def diskmapstr():
    s = []
    for c in diskmap:
        if c is None:
            c == '.'
        s.append(str(c))

    return ''.join(s)

def diskmapprint():
    for c in diskmap:
        print(c, end='') if c is not None else print('.', end='')
    print()


free_ranges = []
current = diskmap[0]
num = True
start = end = 0
for idx, c in enumerate(diskmap):
    if c != current:
        end = idx
        if current is None:
            length = end - start
            free_ranges.append((length, start, end))

            # print(f"{current=}")
            # print(length)
        current = c
    start = end

# for free in free_ranges:
#     print(free)

# diskmapprint()

start = len(diskmap)
end = len(diskmap)
current = diskmap[-1]

target = diskmapstr()
while True:
    if start <= 0:
        break
    # iterate backwards, getting the size of the current range
    while True:
        start -= 1
        if current != diskmap[start]:
            break
    # move start back one
    start += 1
    l = end - start

    if current:
        # print(f"{current=}")
        found = None

        # find the first hole that will fit
        for idx, freespace in enumerate(free_ranges):
            if l <= freespace[0] and freespace[1] < start:
                found = free_ranges.pop(idx)
                # print(f"{found=}")
                # we have found a space that will fit
                break

        if found is not None:
            # print(f"found our backwards range: {start, end}")
            # insert new crap there
            free_l, free_s, free_e = freespace
            for i in range(l):
                diskmap[free_s + i] = current
                diskmap[start + i] = None
            # diskmapprint()

            # find the remaining free space and reinsert
            if free_l > l:
                new_free_range = (free_l - l, free_s + l, free_e)
                # print(f"{new_free_range=}")
                # print(free_ranges)
                # input()

                # merge any before and afters
                # merge any befores
                while True:
                    fl, fs, fe = new_free_range
                    if idx == 0:
                        break

                    bl, bs, be = free_ranges[idx - 1]
                    if be == new_free_range[1]:
                        new_free_range = (fe - bs, bs, fe)
                        free_ranges.pop(idx - 1)
                        idx -= 1
                    else:
                        break

                # merge any afters
                while True:
                    fl, fs, fe = new_free_range
                    if idx == len(free_ranges) - 1:
                        break

                    afl, afs, afe = free_ranges[idx + 1]
                    if new_free_range[2] == afs:
                        new_free_range = (afe - fs, fs, afe)
                        free_ranges.pop(idx + 1)
                    else:
                        break

                free_ranges.insert(idx, new_free_range)
            # print(diskmap[start:end])

    current = diskmap[start - 1]
    end = start


# diskmapprint()
print('calcluating p2')
for i, n in enumerate(diskmap):
    if n is not None:
        p2 += i * int(n)

# import sys;sys.exit()















# part 1=================

diskmap = []
num = True
disk_id = 0
current = None
current_len = 0

for c in inp:
    c = int(c)
    if num:
        for i in range(c):
            diskmap.append(disk_id)

        disk_id += 1
    else:
        for i in range(c):
            diskmap.append(None)
    num = not num


def diskmapprint():
    for c in diskmap:
        print(c, end='') if c is not None else print('.', end='')
    print()


start = 0
end = len(diskmap)

while True:
    while diskmap[start] is not None:
        start += 1
        if start >= len(diskmap):
            break

    if start >= len(diskmap):
        break

    while diskmap[start] is None:
        c = diskmap.pop()
        if c:
            diskmap[start] = c
            start += 1
        end -= 1

    if start >= len(diskmap):
        break



# diskmapprint()

for i, n in enumerate(diskmap):
    p1 += i * int(n)


























print(f"{p1=}")
print(f"{p2=}")

if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
print("Execution time:", perf_counter() - __start_time)
print()
