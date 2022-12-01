#! /usr/bin/env python3.10
import itertools as it

from collections import Counter, deque

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



test_inp = load_lines("03.test")
inp = load_lines("03.in")

# inp = test_inp

## part 1

bits = [Counter() for _ in range(len(inp[0]))]

for line in inp:
    for idx, c in enumerate(line):
        bits[idx][c] += 1

gamma = ''.join(max(bit, key=bit.get) for bit in bits)
epsilon = ''.join(min(bit, key=bit.get) for bit in bits)

print(f"Part 1: {int(gamma, 2) * int(epsilon, 2)}")


## part 2
inp = test_inp

oxygen = inp[:]
co2 = inp[:]
bit_length = len(inp[0])
oxy_bit_criteria = Counter()
co2_bit_criteria = Counter()

for i in range(bit_length):
    oxy_bit_criteria.clear()

    for oxy_string in oxygen:
        oxy_bit_criteria[oxy_string[i]] += 1
    
    most_common = '0' if oxy_bit_criteria['0'] > oxy_bit_criteria['1'] else '1'
    oxygen = [oxy for oxy in oxygen if oxy[i] == most_common]

    co2_bit_criteria.clear()

    for co2_string in co2:
        co2_bit_criteria[co2_string[i]] += 1
    
    if co2_bit_criteria['1'] < co2_bit_criteria['0']:
        least_common = '1'
    else:
        least_common = '0'

    temp_co2 = [co for co in co2 if co[i] == least_common]

    co2 = temp_co2

    print(oxy_bit_criteria)
    print(co2_bit_criteria)
    print(f"oxy: {oxygen}")
    print(f"co2: {co2}")