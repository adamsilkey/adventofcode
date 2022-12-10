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

class CRT:
    def __init__(self, height: int, length: int) -> None:
        self.height = height
        self.length = length
        self.display = ['.' for _ in range(self.height * self.length)]
        self.x = 1
        self.cycles = 0
        self.signal_strength = 0
    
    def __repr__(self):
        return f"CRT(height={self.height}, length={self.length})"

    def __str__(self):
        final = ''
        # Set start/end so that we end up with [0:self.length]
        start = -(self.length)
        end = 0
        for row in range(self.height):
            start += self.length
            end += self.length
            final += ''.join(self.display[start:end])
            final += '\n'
        return final
    
    def draw_pixel(self) -> None:
        pos = (self.cycles - 1) % self.length
        if self.x - 1 <= pos <= self.x + 1:
            self.display[self.cycles - 1] = '#'
        
        if self.cycles % self.length == 20:
            self.signal_strength += self.x * self.cycles
    
    def execute(self, instruction: str) -> None:
        match instruction.split():
            case ['addx', x]:
                self.addx(x)
            case ['noop']:
                self.noop()

    def addx(self, x: int) -> None:
        for _ in range(2):
            self.cycles += 1
            self.draw_pixel()
        self.x += int(x)
    
    def noop(self) -> None:
        self.cycles += 1
        self.draw_pixel()


class Program:
    def __init__(self, height: int, length: int, filename: str):
        self.height = height
        self.length = length
        self.filename = filename
        self.crt = CRT(self.height, self.length)
    
    def __repr__(self):
        return f"Program(height={self.height}, length={self.length}, filename={self.filename}"
    
    def run(self):
        with open(self.filename) as f:
            for instruction in f:
                self.crt.execute(instruction)
        
        print(f"p1: {self.crt.signal_strength}")
        print("p2:")
        print()
        print(self.crt)
        

program = Program(6, 40, FILENAME)
program.run()





























if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
