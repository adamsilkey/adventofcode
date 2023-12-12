#! /usr/bin/env python3

YEAR = "2023"
AOC_DAY = "12"

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
from math import lcm, prod

DEBUG = True

__start_time = perf_counter()


inp = load_lines(filename)

DAMAGED = '#'
OPERATIONAL = '.'
QUESTION = '?'

def build_options(condition: str):
    options = []
    products = it.product('#.', repeat=condition.count(QUESTION))
    if QUESTION not in condition:
        return [condition]
    for round in products:
        new_str = []
        round = list(round)
        round.reverse()
        for c in condition:
            if c == QUESTION:
                new_str.append(round.pop())
            else:
                new_str.append(c)
        new_str = ''.join(new_str)
        # new_str.replace(".", "G")
        options.append(''.join(new_str))

    return options


def solve(contiguous, options):
    re_string = r"^\.*"
    for n in contiguous:
        # re_string += r"#{" + str(n) + r"}G+"
        re_string += "#" * n + r"\.+"
    re_string = re_string[:-3]
    re_string += r"\.*$"
    print(re_string)
    solver = re.compile(re_string)

    sum_ = 0
    for option in options:
        # if bool(solver.match(option)):
        if bool(solver.search(option)):
            sum_ += 1
            # print(option)
            # input()
    
    return sum_


# contiguous = [1,1,3]
# condition = '???.###'
# contiguous = [3,2,1]
# condition = '?###????????'
# options = build_options(condition)
# # for option in options:
# #     print(option)

# print(solve(contiguous, options))
# sys.exit()

# print(solve(contiguous, ["#.#.###"]))
# print(solve(contiguous, build_options(condition)))
# sys.exit()

sum_ = 0
for line in inp:
    condition, contiguous = line.split()
    contiguous = [int(i) for i in contiguous.split(",")]
    # print(condition, contiguous)

    questions = condition.count("?")
    # sum1 += 2 ** (questions - 1)
    # sum2 += len(build_options(condition))
    options = build_options(condition)

    sum_ += solve(contiguous, options)


print(sum_)








































if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
print("Execution time:", perf_counter() - __start_time)
print()
