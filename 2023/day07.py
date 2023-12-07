#! /usr/bin/env python3

YEAR = '2023'
AOC_DAY = '07'

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


inp = load_lines(filename)

class Hand:
    
    CARD_VALUE = {
        "A"
    }
    def __init__(self, hand: str, bid: int):
        self.hand = hand
        self.bid = bid
    
    def __repr__(self):
        return self.hand
    
    def __str__(self):
        return self.hand
    
    def __eq__(self, other):
        if not self.rank == other.rank:
            return False
        else:
            for left, right in zip(self.hand, other.hand):
                left = self.convert_card(left)
                right = self.convert_card(right)

                if left != right:
                    return False
            else: # no break
                return True

    def __gt__(self, other):
        if self.rank == other.rank:
            for left, right in zip(self.hand, other.hand):
                left = self.convert_card(left)
                right = self.convert_card(right)

                if left != right:
                    return left > right
            else: # equal hands
                return left > right
        else:
            return self.rank > other.rank

    def __lt__(self, other):
        if self.rank == other.rank:
            for left, right in zip(self.hand, other.hand):
                left = self.convert_card(left)
                right = self.convert_card(right)

                if left != right:
                    return left < right
            else: # equal hands
                return left < right
        else:
            return self.rank < other.rank

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    @staticmethod
    def convert_card(s: str) -> int:
        s = s.replace("A", "14").replace("T", "10").replace("J", "11").replace("Q", "12").replace("K", "13")

        return int(s)


    @staticmethod
    def compare_hand(left: list[int], right: list[int]):
        lc = Counter(left)
        rc = Counter(right)
        pass

    @property
    def rank(self):
        hc = Counter(self.hand)

        match len(hc):
            case 1: # five of a kind
                return 7
            case 2: # four of a kind or full house
                if 4 in hc.values():
                    return 6
                else:
                    return 5
            case 3: # three of a kind or two pair
                if 3 in hc.values():
                    return 4
                else:
                    return 3
            case 4: # one pair
                return 2
            case 5:
                return 1

    # @staticmethod
    # def convert_hand(hand: str):
    #     hand = list(hand)
    #     hand = ",".join(hand)+","
    #     hand = list(int(card) for card in hand.split(",")[:-1])
    #     hand.sort(reverse=True)

    #     return hand

hands = []
for line in inp:
    a, b = line.split()
    
    hands.append(Hand(a, int(b)))

# for hand in hands:
#     print(hand.hand, hand.rank)

hands.sort()


p1 = 0

for i, hand in enumerate(hands, 1):
    p1 += hand.bid * i

print(p1)
# print(hands)















if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
