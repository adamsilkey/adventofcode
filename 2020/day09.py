#! /usr/bin/env python3

from collections import namedtuple
from itertools import combinations
from typing import List

print("day 9")

with open("input/2020-09.in") as f:
    day9 = [line.strip() for line in f]

test_data = """
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
""".strip().split("\n")


def parse_data(data):
    data = [int(line) for line in data]

    return data


test_data = parse_data([line.strip() for line in test_data])


def preamble(inputs, preamble_length):
    i = 0
    target_idx = preamble_length

    while True:
        # print("---------")
        target = inputs[target_idx]
        # print(f"Looking for {target}")
        for comb in combinations(inputs[i:target_idx], 2):
            # print(f"{comb} -> sum: {sum(comb)}")
            if sum(comb) == target:
                break
        else: # no break, we've found a bad one
            print("there's nothing here captain")
            # print(i, target_idx, target)
            print(f"part_one: {target}")
            return target

        i += 1
        target_idx += 1


def encryption_weakness(inputs, target):
    for i, v in enumerate(inputs):
        sum_ = 0
        begin = i
        end = i
        while sum_ < target:
            sum_ += inputs[end]
            end += 1
            if sum_ == target:
                print("Found it!")
                weakness = inputs[begin:end]
                min_ = min(weakness)
                max_ = max(weakness)
                # print(weakness)
                # print(min_, max_)
                print(f"part two: {min_ + max_}")
                return

# target = preamble(test_data, 5)
# encryption_weakness(test_data, target)
#
# import sys;sys.exit()
target = preamble(parse_data(day9), 25)

encryption_weakness(parse_data(day9), target)

