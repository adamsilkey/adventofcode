#! /usr/bin/env python3

YEAR = '2023'
AOC_DAY = '04'

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


inp = load_lines(filename)


sum = 0

games = {}
for line in inp:
    card, _, values = line.partition(":")
    card = int(card.split()[-1])

    part_a, _, part_b = values.partition("|")
    winners = [int(a) for a in part_a.split()]
    numbers = [int(b) for b in part_b.split()]

    score = 0
    for winner in winners:
        if winner in numbers:
            score += 1
    
    games[card] = score


total_cards = Counter()
for key in games:
    total_cards[key] = 1

for k, v in games.items():
    print(f"processing card {k}, values {v}")
    for n in range(total_cards[k]):
        for i in range(k+1, k+v+1):
            total_cards[i] += 1

print(sorted(total_cards.items()))

sum = 0
for v in total_cards.values():
    sum += v
print(sum)





def p1():
    for line in inp:
        card, _, values = line.partition(":")
        card = int(card.split()[-1])

        part_a, _, part_b = values.partition("|")
        winners = [int(a) for a in part_a.split()]
        numbers = [int(b) for b in part_b.split()]

        score = 0
        for winner in winners:
            if winner in numbers:
                score += 1
        
        if score == 0:
            continue
        elif score == 1:
            score = 1
        else:
            score = pow(2, score - 1)
        
        sum += score


    print(sum)








if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
