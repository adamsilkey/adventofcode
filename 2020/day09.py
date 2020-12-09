#! /usr/bin/env python3

from itertools import combinations

print("day 9")

with open("input/2020-09.in") as f:
    day9 = [line.strip() for line in f]


def parse_data(data):
    return [int(line) for line in data]


def preamble(inputs, preamble_length):
    i = 0
    target_idx = preamble_length

    while True:
        target = inputs[target_idx]
        for comb in combinations(inputs[i:target_idx], 2):
            if sum(comb) == target:
                break
        else:  # no break, we've found a bad one
            print(f"part_one: {target}")
            return target

        i += 1
        target_idx += 1


def encryption_weakness(inputs, target):
    for i, v in enumerate(inputs):
        sum_ = 0
        begin = end = i
        while sum_ < target:
            sum_ += inputs[end]
            end += 1
            if sum_ == target:
                print("Found it!")
                weakness = inputs[begin:end]
                part_two = min(weakness) + max(weakness)
                print(f"part two: {part_two}")
                return part_two


def main():
    data = parse_data(day9)
    part_one = preamble(data, 25)
    encryption_weakness(data, part_one)


main()


def test():
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

    test_data = parse_data([line.strip() for line in test_data])
    target = preamble(test_data, 5)
    encryption_weakness(test_data, target)

