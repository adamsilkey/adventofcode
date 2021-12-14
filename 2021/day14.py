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


def puzzle_input(filename):

    template, raw_rules = load_file(filename).split("\n\n")
    template = template.strip()
    rules = {}
    for rule in raw_rules.splitlines():
        pair, element = rule.split(" -> ")
        rules[pair] = element

    return template, rules


def part_one_like_a_brute(template, rules):

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
    most = p1.most_common()[0]
    least = p1.most_common()[-1]

    print(f"p1: {most} - {least} = {most[1] - least[1]}")


def part_two_so_elegant(template, rules):

    pairs = Counter()
    for i, c in enumerate(template[:-1]):
        pairs[f"{c}{template[i+1]}"] += 1

    for _ in range(40):
        new_pairs = Counter()
        for pair in pairs:
            count = pairs[pair]
            new_pairs.update({f"{pair[0]}{rules[pair]}": count})
            new_pairs.update({f"{rules[pair]}{pair[1]}": count})

        pairs = new_pairs

    all_the_single_letters = Counter()

    for pair in pairs:
        # Add every second character, or else you'll get double results
        all_the_single_letters.update({pair[1]: pairs[pair]})

    # Add on the very first letter
    all_the_single_letters[template[0]] += 1

    most = all_the_single_letters.most_common()[0]
    least = all_the_single_letters.most_common()[-1]

    print(f"p2: {most} - {least} = {most[1] - least[1]}")


template, rules = puzzle_input(filename)
part_one_like_a_brute(template, rules)
part_two_so_elegant(template, rules)



if test:
    print()
    print("============ This was a test!!!! ============")
