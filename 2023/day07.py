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
    
    def __init__(self, hand: str, bid: int, version=1):
        self.hand = hand
        self.bid = bid
        self.version = version
    
    def __repr__(self):
        return f"Hand(hand={self.hand!r},bid={self.bid!r}, version={self.version!r})"
    
    def __str__(self):
        return self.hand
    
    def __eq__(self, other):
        if self.rank != other.rank:
            return False
        else:
            # Check every value in turn to see if they're not equal
            for left, right in zip(self.hand, other.hand):
                left = self.convert_card(left)
                right = self.convert_card(right)

                if left != right:
                    return False
            else: # no break, they're equal
                return True

    def __gt__(self, other):
        # check if hand rank doesn't match
        if self.rank != other.rank:
            return self.rank > other.rank
        # check values in order, skipping over equal cards
        else:
            for left, right in zip(self.hand, other.hand):
                left = self.convert_card(left)
                right = self.convert_card(right)

                if left != right:
                    return left > right
            else: # equal hands
                return False

    def __lt__(self, other):
        # check if hand rank doesn't match
        if self.rank != other.rank:
            return self.rank < other.rank
        # check values in order, skipping over equal cards
        else:
            for left, right in zip(self.hand, other.hand):
                left = self.convert_card(left)
                right = self.convert_card(right)

                if left != right:
                    return left < right
            else: # equal hands
                return False

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def convert_card(self, char_: str, /) -> int:
        """Converts card string to card rank value"""

        if len(char_) != 1:
            raise ValueError(f"Invalid character passed to convert_card(): {char_}")

        # Jack value is 11 / Joker value is 0
        j_value = "11" if self.version == 1 else "0"
        char_ = char_.replace("A", "14").replace("T", "10").replace("J", j_value).replace("Q", "12").replace("K", "13")

        return int(char_)

    @property
    def rank(self):
        hc = Counter(self.hand)

        # Part 2
        if self.version == 2 and 'J' in hc:
            if len(hc) == 1:
                return 7 # five of a kind
            joker_hc = Counter(self.hand)
            num_js = joker_hc['J']
            del joker_hc['J']
            key = joker_hc.most_common(1)[0][0]
            joker_hc[key] += num_js

            hc = joker_hc

        # Because we have five card hands, we know that the counter values
        # of certain hands will equate to certain hand types
        # E.g. 'AAAA4' will convert to {'A': 4, '4': 1}.
        # With a length of 2, we know it's four of a kind
        #
        # You could have just as easily done this by looking at values instead
        # but length is what I came up with in the moment
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


p1 = []
p2 = []
for line in inp:
    hand, bid = line.split()
    
    p1.append(Hand(hand, int(bid)))
    p2.append(Hand(hand, int(bid), version=2))

p1.sort()
p2.sort()

p1_result = 0
p2_result = 0

for i, hand in enumerate(p1, 1):
    p1_result += hand.bid * i

for i, hand in enumerate(p2, 1):
    p2_result += hand.bid * i

print(f"{p1_result=}")
print(f"{p2_result=}")















if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
