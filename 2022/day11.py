#! /usr/bin/env python3.11

YEAR = '2022'
AOC_DAY = '11'

import itertools as it
import re
import sys
from collections import Counter, defaultdict, deque, namedtuple
from contextlib import suppress
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

p = load_file(FILENAME)

class Monkey:
    def __init__(self, id, items, operation, value, divisor, truemonkey, falsemonkey):
        self.id = id
        self.items: deque = items
        self.operation = operation
        self.value = value
        with suppress(ValueError):
            self.value = int(self.value)
        self.divisor = int(divisor)
        self.truemonkey = int(truemonkey)
        self.falsemonkey = int(falsemonkey)

        self.inspections = 0

    def increase_worry(self, x):
        self.inspections += 1
        if self.value == 'old':
            return self.square(x)
        elif self.operation == '*':
            return self.mult(x)
        elif self.operation == '+':
            return self.add(x)
        
    def test(self, x):
        if int(x) % self.divisor == 0:
            return self.truemonkey
        else:
            return self.falsemonkey

    def add(self, x):
        return int(x) + int(self.value)

    def mult(self, x):
        return int(x) * int(self.value)

    def square(self, x):
        return int(x) * int(x)
    
    def __repr__(self):
        return f"Monkey(id={self.id}, items={self.items}, operation={self._operation}, value={self.value}, divisor={self.divisor}, truemonkey={self.truemonkey}, falsemonkey={self.falsemonkey}"
    
    @classmethod
    def fromstring(cls, string):
        for line in string.split('\n'):
            match line.split():
                case 'Monkey', x:
                    id_ = int(x[0])
                case 'Starting', 'items:', *items:
                    items = deque([int(item.rstrip(',')) for item in items])
                case 'Operation:', *rest, operation, value:
                    if value.isdigit():
                        value = int(value)
                case 'Test:', *rest, divisor:
                    divisor = divisor
                case 'If', 'true:', *rest, truemonkey:
                    truemonkey = int(truemonkey)
                case 'If', 'false:', *rest, falsemonkey:
                    falsemonkey = int(falsemonkey)
        
        return cls(
            id_,
            items,
            operation,
            value,
            divisor,
            truemonkey,
            falsemonkey,
        )



# initialize
monkeystrings = p.split('\n\n')
monkeys = []
for monkey in monkeystrings:
    monkey = Monkey.fromstring(monkey)
    #print(monkey)
    monkeys.append(monkey)

all_divisors = 1
for monkey in monkeys:
    all_divisors *= monkey.divisor
    

def go(monkeys: list[Monkey]):
    for i in range(10000):
        monkeys_not_done = [False for _ in monkeys]
        while not any(monkeys_not_done):
            for idx,monkey in enumerate(monkeys):
                while monkey.items:
                    original_value = item = int(monkey.items.popleft())
                    item = monkey.increase_worry(item)

                    # p1 worry
                    # item //= 3
                    # p2 managing worry
                    throw_to = monkey.test(item)
                    next_monkey = monkeys[throw_to]

                    item = item % all_divisors

                    # if monkey.operation == '*' and next_monkey.operation == '+':
                    #     item = (item // monkey.value) - (item % monkey.divisor)
                    # if monkey.operation == '*' and next_monkey.operation == '**':



                    # if next_monkey.value == 'old':
                    #     item = item % next_monkey.divisor
                    #     pass
                    # elif next_monkey.operation == '*':
                    #     # item = item % next_monkey.divisor
                    #     pass
                    # elif next_monkey.operation == '+' and monkey.operation != '+':
                    #     item = item % next_monkey.divisor
                    #     pass

                    # if next_monkey.value == 'old':
                    #     item //= item
                    # elif next_monkey.operation == '*':
                    #     item //= int(monkey.value)
                    # elif next_monkey.operation == '+':
                    #     if monkey.value == 'old':
                    #         item //= item
                    #     elif monkey.operation == '*':
                    #         item //= int(monkey.value)

                    # if next_monkey.value == 'old':
                    #     if monkey.value == 'old':
                    #         item //= item
                    #     elif monkey.operation == '*':
                    #         item //= int(monkey.value)
                    #     # item = original_value
                    #     # item //= worry_manager
                    # elif next_monkey.operation == '+':
                    #     if monkey.value == 'old':
                    #         item //= item
                    #     elif monkey.operation == '*':
                    #         item //= int(monkey.value)
                    #     # worry_manager = int(original_value)
                    #     # item //= worry_manager
                    #     pass
                    # elif next_monkey.operation == '*':
                    #     if monkey.operation == '*':
                    #         item //= int(monkey.value)
                    #     elif monkey.operation == 'old':
                    #         item //= item
                    #     # item //= worry_manager

                    monkeys[throw_to].items.append(item)
                monkeys_not_done[idx] = True
        # print(f"round {i}")
            # print(monkey.items)
        # input()
                

go(monkeys)

for monkey in monkeys:
    print(monkey.id, ': ', monkey.inspections)






















if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
