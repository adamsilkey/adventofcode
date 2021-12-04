#! /usr/bin/env python3.10
import itertools as it

from collections import deque

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


bits = []
for i in range(len(inp[0])):
    bits.append({0:0, 1:0})

for line in inp:
    for idx, c in enumerate(line):
        if c == '0':
            bits[idx][0] += 1
        else:
            bits[idx][1] += 1

print(bits)

epsilon = ''
gamma = ''

for bit in bits:
    if bit[0] > bit[1]:
        gamma += '0'
        epsilon += '1'
    else:
        epsilon += '0'
        gamma += '1'


print(gamma)
print(epsilon)

# manually calculate because who can remember how to do binary string conversions


## part 2

# oxy = inp[:]
# counter = 0

# while len(oxy) > 1:
#     _ = []
#     if bits[0][counter] > bits[1][counter]:
#         greatest = '0'
#     else:
#         greatest = '1'
    
#     for ox in oxy:
#         if ox.startswith(greatest):
#             _.append(ox)

#     ox = _

#     print(ox)
#     counter += 1
#     input()


oxy_copy = inp[:]
co_copy = inp[:]
counter = 0
greatest = ''

while len(oxy_copy) > 1 or len(co_copy) > 1:
    oxy_work = []
    co_work = []

    print(oxy_copy)
    print(co_copy)

    oxy_rating = {0:0, 1:0}
    co_rating = {0:0, 1:0}

    for oxy in oxy_copy:
        if oxy[counter] == '1':
            oxy_rating[1] += 1
        else:
            oxy_rating[0] += 1
    
    if oxy_rating[0] > oxy_rating[1]:
        greatest = '0'
    else:
        greatest = '1'

    for co in co_copy:
        if co[counter] == '1':
            co_rating[1] += 1
        else:
            co_rating[0] += 1
    
    if co_rating[0] > co_rating[1]:
        least = '1'
    else:
        least = '0'

    print(oxy_rating)
    print(co_rating)

    for oxy in oxy_copy:
        # if oxy.startswith(greatest):
        if oxy[counter] == greatest:
            oxy_work.append(oxy)
            
    for co in co_copy:
        # if co.startswith(least):
        if co[counter] == least:
            co_work.append(co)
    
    oxy_copy = oxy_work
    co_copy = co_work

    # input()

    if len(oxy_copy) == 1:
        oxy_rating_final = oxy_copy[0]

    if len(co_copy) == 1:
        co_rating_final= co_copy[0]

    counter += 1


print(oxy_rating_final)
print(co_rating_final)

