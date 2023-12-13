#! /usr/bin/env python3

YEAR = "2023"
AOC_DAY = "13"

import sys
from time import perf_counter

if not (YEAR and AOC_DAY):
    print("!!! Set YEAR/AOC_DAY")
    sys.exit(1)


def fail():
    print("!!! Need to define -p for production or -t for test")
    sys.exit(1)


if len(sys.argv) != 2:
    fail()

match sys.argv[1].lower():
    case "-t":
        test = True
    case "-p":
        test = False
    case _:
        fail()

if test:
    filename = f"input/{AOC_DAY}.test"
else:
    filename = f"input/{AOC_DAY}.in"

title = f"Advent of Code {YEAR} - Day {AOC_DAY} - {'Test' if test else 'Production'}"

print(f"=" * len(title))
print(title)
print(f"=" * len(title))


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


def load_comma_separated_ints(filename: str) -> list[int]:
    """Returns a list of ints from a comma separated list of ints"""

    return [int(i) for i in load_file(filename).strip().split(",")]


import functools
import itertools as it
import re
import sys
from collections import Counter, defaultdict, deque, namedtuple
from dataclasses import dataclass
from math import lcm, prod

DEBUG = True

__start_time = perf_counter()


inp = load_file(filename)

raw_maps = inp.split("\n\n")

Point = namedtuple("Point", "r c")

maps = []
for m in raw_maps:
    m = m.splitlines()
    maps.append([[c for c in row] for row in m])




def print_forest(m):
    for r in m:
        print(''.join(r))



def find_smudge_candidate(left, right):
    l = ''.join(left)
    r = ''.join(right)

    smudge_candidates = [i for i, (lc, rc) in enumerate(zip(l, r)) if lc != rc]
    if len(smudge_candidates) != 1:
        return None
    smudge_idx = smudge_candidates[0]
    print(f"{smudge_idx=}")

    return smudge_idx



def find_candidates(m: list[list[str]], part_2 = False):
    candidates = []
    for i, row in enumerate(m[:-1]):
        if row == m[i+1]:
            print('found potential', i)
            candidates.append(i)
        
        if part_2:
            smudge_idx = find_smudge_candidate(row, m[i+1])
            if smudge_idx is not None:
                print("found potential smudge", i)
                candidates.append(i)
    
    return candidates


def find_reflections(m: list[list[str]], candidates: list[int], part_2=False):

    if part_2:
        print('====================================== testing candidates:', candidates)
    for i in candidates:
        print('testing can:', i)
        left = i
        right = i + 1
        # print(left, right, len(m))

        smudge_used = False

        while True:
            left -= 1
            right += 1
            if left < 0 or right == len(m):
                print('reflection found', i)
                return i
            if m[left] != m[right]:
                if not part_2:
                    print('no reflection found')
                    break

                if smudge_used:
                    print('smudge already used')
                    break

                smudge_idx = find_smudge_candidate(m[left], m[right])
                if smudge_idx is None:
                    print('no smudge reflection found')
                    break

                smudge_used = True


                # l = list(l)
                # c = l[smudge_idx]
                # l[smudge_idx] = '.' if c == '#' else '#'
                # input()

                # Try and smudge our lines
    else:
        return None
    




def solve_forest(m, v_or_h=None, p1idx=None, part_2=False):
    # horizontal
    cans = find_candidates(m, part_2=part_2)
    if v_or_h == 'h':
        print("H. Removing candidate: ", p1idx)
        cans.remove(p1idx)
    ref = find_reflections(m, cans, part_2=part_2)

    if ref is not None:
        print("***found horizontatl candidate:", ref)
        return 'h', ref
    
    # vertical
    m = [r for r in zip(*m)]
    cans = find_candidates(m, part_2=part_2)
    if v_or_h == 'v':
        print("V. Removing candidate: ", p1idx)
        cans.remove(p1idx)
    ref = find_reflections(m, cans, part_2=part_2)
    if ref is not None:
        print("***found vertical candidate:", ref)
        print(ref)
        return 'v', ref
    
    raise Exception("No reflection found")




p1result = 0
p2result = 0
for m in maps:
    print_forest(m)
    direction, i = solve_forest(m)

    if direction == 'h':
        p1result += 100 * (i + 1)
    else: # v
        p1result += i + 1

    print(f"Part 1 line found: {i}. Direction: {direction}")
    # input()
    
    direction, i = solve_forest(m, direction, i, True)
    if direction == 'h':
        p2result += 100 * (i + 1)
    else: # v
        p2result += i + 1
    print()

print(p1result)
print(p2result)
















# case = """
# #.####.#..##..#
# ...##.##...###.
# #.#####.##.###.
# #.#####.##.###.
# ...##.##.#.###.
# #.####.#..##..#
# #.#...#..#.##..
# ###########..##
# #.####...#...##
# ..#...##.#.#..#
# ..#...##.#.#..#""".strip()

# case = [[c for c in row] for row in case.splitlines()]
# print_forest(case)
# # cans = find_candidates(case)
# # refs = find_reflections(case, cans)
# print(solve_forest(case))
# input()












# def find_reflections(m: list[list[str]]):
#     print()
#     for r in m:
#         print(''.join(r))
#     ### horizontal
#     for i, row in enumerate(m[:-1]):
#         print(row)
#         if row == m[i+1]:
#             print('found potential', i)
        
#             left = i
#             right = i+1

#             while True:
#                 left -= 1
#                 right += 1
#                 # if either are out of bounds, break, we found a reflection
#                 print(left, right)
#                 if left < 0 or right == len(m):
#                     print('horizontal reflection found!')
#                     return i + 2 # counting
#                 if m[left] != m[right]:
#                     print("no horizontal reflection found")
#                     break

#     ### Vertical
#     m = [r for r in zip(*m)]
#     for i, row in enumerate(m[:-1]):
#         print(row)
#         if row == m[i+1]:
#             print('found potential', i)
        
#             left = i
#             right = i+1

#             while True:
#                 left -= 1
#                 right += 1
#                 # if either are out of bounds, break, we found a reflection
#                 if left < 0 or right == len(m):
#                     print('vertical reflection found!')
#                     return i * 100
#                 if m[left] != m[right]:
#                     print("no vertical reflection found")
#                     break
    
#     print(f"{i=}")
#     # input()
#     return 0
        
    






































if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
print("Execution time:", perf_counter() - __start_time)
print()
