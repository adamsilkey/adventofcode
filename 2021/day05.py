#! /usr/bin/env python3.10

TEST = False

import itertools as it
import re
from collections import deque
from dataclasses import dataclass


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

if TEST:
    ll = load_lines("05.test")
else:
    ll = load_lines("05.in")



class Vents:
    def __init__(self):
        self.vents = [[0 for _ in range(1000)] for i in range(1000)]

    # def line(self, x, y, dx, dy):
    #     for i in range(x, dx+1):
    #         for j in range(y, dy+1):
    #             self.vents[i][j] += 1

    def line(self, x1, y1, x2, y2):
        # print(x1 == x2 or y1==y2)

        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1

        if (x1 == x2 or y1 == y2):
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    self.vents[j][i] += 1


    def print(self):
        for row in self.vents:
            for num in row:
                if num:
                    print(num, end='')
                else:
                    print('.', end='')
            print()


vents = Vents()

pattern = re.compile(r"(\d*),(\d*) -> (\d*),(\d*)")

for line in ll:
    a = pattern.match(line.strip())
    x1 = int(a.group(1))
    y1 = int(a.group(2))
    x2 = int(a.group(3))
    y2 = int(a.group(4))

    # print(x1,y1,x2,y2)
    vents.line(x1,y1,x2,y2)
    # vents.print()
    # input()


total = 0
for row in vents.vents:
    for vent in row:
        if vent > 1:
            total += 1

# print(total)


# Part 2

class Vents2:
    def __init__(self):
        self.vents = [[0 for _ in range(1000)] for i in range(1000)]

    def line(self, x1, y1, x2, y2):
        if (x1 == x2 or y1 == y2):
            if x1 > x2:
                x1, x2 = x2, x1
            if y1 > y2:
                y1, y2 = y2, y1
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    self.vents[j][i] += 1
        
        else:  #diagonal
            # a = (x1, y1)
            # b = (x2, y2)

            # if a > b:
            #     a, b = b, a

            # if a[0] < b[0]:
            #     for i in range(b[0] - a[0] + 1):
            #         print(i)
            #         self.vents[a[1] + i][a[0] + i] += 1
            # else:
            #     for i in range(b[0] - a[0] + 1):
            #         self.vents[a[1] - i][a[0] + i] += 1

            if x1 < x2:
                dx = 1
            else:
                dx = -1

            if y1 < y2:
                dy = 1
            else:
                dy = -1
            
            for i in range(abs(x1 - x2) + 1):
                self.vents[y1 + (i * dy)][x1 + (i * dx)] += 1



    def print(self):
        for row in self.vents:
            for num in row:
                if num:
                    print(num, end='')
                else:
                    print('.', end='')
            # print()


vents = Vents2()

pattern = re.compile(r"(\d*),(\d*) -> (\d*),(\d*)")

for line in ll:
    a = pattern.match(line.strip())
    x1 = int(a.group(1))
    y1 = int(a.group(2))
    x2 = int(a.group(3))
    y2 = int(a.group(4))

    print(x1,y1,x2,y2)
    vents.line(x1,y1,x2,y2)
    # vents.print()
    # input()


total = 0
for row in vents.vents:
    for vent in row:
        if vent > 1:
            total += 1

print(f"p2: {total}")