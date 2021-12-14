#! /usr/bin/env python3.10

YEAR = '2021'
AOC_DAY = '14'

import itertools as it
import sys
from collections import Counter, defaultdict, deque, namedtuple
from dataclasses import dataclass

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
    filename = f"{AOC_DAY}.test"
else:
    filename = f"{AOC_DAY}.in"

title = f"Advent of Code {YEAR} - Day {AOC_DAY} - {'Test' if test else 'Production'}"

print(f"=" * len(title))
print(title)
print(f"=" * len(title))

def load_file(filename: str) -> str:
    """Loads an AOC file, returns a string"""

    with open(filename) as f:
        return f.read().rstrip("\n")


# Rule = namedtuple("Rule", ["pair", "element"])


template, raw_rules = load_file(filename).split("\n\n")
template = template.strip()
rules = {}
for rule in raw_rules.splitlines():
    pair, element = rule.split(" -> ")
    rules[pair] = element


# part 1
for _ in range(10):
    new_template = f'{template[0]}'
    for i, c in enumerate(template[:-1]):
        pair = f"{c}{template[i+1]}"
        if pair in rules:
            pair = f"{c}{rules[pair]}{template[i+1]}"

        new_template += pair[1:]
        # print(pair, new_template)

    template = new_template
    # print(i, template)


p1 = Counter(template)
print(p1)


pairs = Counter()
for i, c in enumerate(template[:-1]):
    pairs[f"{c}{template[i+1]}"] += 1

print(pairs)

for _ in range(40):
    new_pairs = Counter()
    for pair in pairs:
        count = pairs[pair]
        new_pairs.update({f"{pair[0]}{rules[pair]}": count})
        new_pairs.update({f"{rules[pair]}{pair[1]}": count})

    pairs = new_pairs

    # print(pairs)
    # input()

single_latters = Counter()

for pair in pairs:
    # single_latters.update({pair[0]: pairs[pair]})
    single_latters.update({pair[1]: pairs[pair]})

single_latters[template[0]] += 1

print(single_latters)

# print(Counter('NBBBCNCCNBBNBNBBCHBHHBCHB'))
# print(Counter('NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB'))