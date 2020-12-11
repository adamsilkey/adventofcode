#! /usr/bin/env python3

from itertools import combinations

print("day 10")

with open("input/2020-10.in") as f:
    day10 = f.readlines()


def parse_data(data):
    return [int(line.strip()) for line in data]


def jolt_chain(adapters: list):
    adapters.append(0)
    adapters.sort()
    adapters.append(adapters[-1] + 3)

    # Part One
    ones = 0
    threes = 0

    # Part Two 
    distinct_arrangements = 1
    chain_to_combos = {1: 1, 2: 1, 3: 2, 4: 4, 5: 7}  # chain-length, combos
    start = 0

    # Iterate to the second to last item, start counting from second list element
    for end, jolt_rating in enumerate(adapters[:-1], start=1):
        if adapters[end] - jolt_rating == 1:
            ones += 1
        else:       # Must be 3
            threes += 1
            distinct_arrangements *= chain_to_combos[end - start]
            start = i

    print(f"part one: {ones * threes}")
    print(f"part two: {distinct_arrangements}")


jolt_chain(parse_data(day10))
