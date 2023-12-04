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

games = {}
for line in inp:
    card, _, values = line.partition(":")
    card = int(card.split()[-1])

    part_a, _, part_b = values.partition("|")
    winners = set(int(a) for a in part_a.split())
    numbers = set(int(b) for b in part_b.split())

    games[card] = len(winners.intersection(numbers))

total_cards = Counter({card: 1 for card in games})

p1 = 0
for card_id, score in games.items():
    p1 += pow(2, score - 1) if score > 1 else score
    for i in range(card_id+1, card_id+score+1):
        total_cards[i] += total_cards[card_id]

print(f"{p1=}")
p2 = sum(v for v in total_cards.values())
print(f"{p2=}")





if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
