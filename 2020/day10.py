#! /usr/bin/env python3

from itertools import combinations

print("day 10")

with open("input/2020-10.in") as f:
    day9 = [line.strip() for line in f]


def parse_data(data):
    return [int(line.strip()) for line in data]


def jolt_chain(adapters: list):
    adapters.append(0)
    adapters.append(max(adapters)+3)
    adapters.sort()
    jolts = {1: 0, 2: 0, 3: 0}
    for idx, jolt in enumerate(adapters):
        if idx + 1 == len(adapters):
            break
        jolt_difference = adapters[idx+1] - adapters[idx]
        jolts[jolt_difference] += 1

    print(f"part_one {jolts[1] * jolts[3]}")


jolt_chain(parse_data(day9))




def test():
    test_data = """
    16
    10
    15
    5
    1
    11
    7
    19
    6
    12
    4
    """.strip().split("\n")

    test_data = parse_data(test_data)
    jolt_chain(test_data)

# test()


def test2():
    test_data = """
    28
    33
    18
    42
    31
    14
    46
    20
    48
    47
    24
    23
    49
    45
    19
    38
    39
    11
    1
    32
    25
    35
    8
    17
    7
    9
    4
    2
    34
    10
    3""".strip().split("\n")

    test_data = parse_data(test_data)
    jolt_chain(test_data)

# test()
# test2()