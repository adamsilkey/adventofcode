#! /usr/bin/env python3

from itertools import combinations

print("day 10")

with open("input/2020-10.in") as f:
    # day9 = [line.strip() for line in f]
    day9 = f.readlines()
for line in day9:
    print(repr(line))



def parse_data(data):
    return [int(line.strip()) for line in data]


def jolt_chain(adapters: list):
    adapters.append(0)
    adapters.sort()
    adapters.append(adapters[-1] + 3)
    jolts = {1: 0, 2: 0, 3: 0}

    chain = 1
    total_paths = 1

    for idx, jolt in enumerate(adapters):
        if idx + 1 == len(adapters):
            break
        jolt_difference = adapters[idx+1] - adapters[idx]
        jolts[jolt_difference] += 1

        if jolt_difference == 1:
            chain += 1
        else:
            if chain == 3:
                total_paths *= 2
            elif chain == 4:
                total_paths *= 4
            elif chain == 5:
                total_paths *= 7
            chain = 1

    print(f"day10 part_one: {jolts[1] * jolts[3]}")
    print(f"day 10 part two : {total_paths}")


jolt_chain(parse_data(day9))
import sys;sys.exit()

# log(base2) of 8 = 

# (0), 1,     4, 5, 6, 7,    10, 11, 12,      15, 16, 19, (22)
# (0), 1,     4, 5, 6, 7,    10,     12,      15, 16, 19, (22)
# (0), 1,     4, 5,    7,    10, 11, 12,      15, 16, 19, (22)
# (0), 1,     4, 5,    7,    10,     12,      15, 16, 19, (22)
# (0), 1,     4,    6, 7,    10, 11, 12,      15, 16, 19, (22)
# (0), 1,     4,    6, 7,    10,     12,      15, 16, 19, (22)
# (0), 1,     4,       7,    10, 11, 12,      15, 16, 19, (22)
# (0), 1,     4,       7,    10,     12,      15, 16, 19, (22)


# For consecutive numbers
# 0 - 1               chain length of 2 -> 1 total routes  -- 2 ^ 0 (length)
# 0 - 1 - 2 =         chain length of 3 -> 2 total routes  -- 2 ^ 1 (length of chain - 1)
# 0 - 1 - 2 - 3 =     chain length of 4 -> 4 total routes  -- 2 ^ 2

# 0 - 1 - 2 - 3 - 4 = chain length of 5 -> 7 total routes  -- 2 ^ 3 - 1 
# 0 1 2 3 4 5         chain length of 6 -> 10 total routes?

#   0   1   2   3   4
#   0   1   2       4
#   0   1       3   4
#   0   1           4
#   0       2   3   4
#   0       2       4
#   0           3   4
#   0               4 (not a route)

# chain length of 5
# 0 1 2 3 4 5
# 0 1 2 3   5
# 0 1 2   4 5
# 0 1   3 4 5
# 0   2 3 4 5
# 0   2   4 5
# 0   2 3   5
# 0   2     5
# 0     3 4 5
# 0     3   5
# 0       4 5 (not a route)
# 0         5 (not a route)



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

test()

# import sys;sys.exit()

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

test2()