#! /usr/bin/env python3.10
import itertools as it

from collections import deque

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


def test():
    print(load_file("int_test.txt"))
    print(load_lines("int_test.txt"))
    print(load_ints("int_test.txt"))


### Load day from 02.in

moves = load_lines("02.in")
# moves = load_lines("02.test")

# part 2

hoz = 0
depth = 0
aim = 0
for move in moves:
    direction, num = move.split()
    num = int(num)
    print(direction, num)


    if direction == 'forward':
        hoz += num
        depth += aim * num
    elif direction == 'back':
        hoz -= num
    elif direction == 'down':
        aim += num
    elif direction == 'up':
        aim -= num

    print(hoz, depth)


print(hoz, depth)
print(hoz * depth)



import sys;sys.exit()


# part 1

hoz = 0
depth = 0
for move in moves:
    direction, num = move.split()
    num = int(num)
    print(direction, num)


    if direction == 'forward':
        hoz += num
    elif direction == 'back':
        hoz -= num
    elif direction == 'down':
        depth += num
    elif direction == 'up':
        depth -= num

    print(hoz, depth)


print(hoz, depth)
print(hoz * depth)


