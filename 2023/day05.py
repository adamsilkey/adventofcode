#! /usr/bin/env python3

YEAR = '2023'
AOC_DAY = '05'

import sys

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


Range = namedtuple("Range", "dest source length")

inp = load_file(filename).split("\n\n")

seeds = [int(a) for a in inp[0].split(":")[1].split()]

p2_seeds = inp[0].split(":")[1].split()

def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)

p2_seed_range = {}
for start, stop in pairwise(p2_seeds):
    start = int(start)
    stop = start + int(stop)
    p2_seed_range[range(start, stop)] = range(start, stop)

print(p2_seed_range)

def map_instructions(s: str):
    final_map = {}
    for line in s.splitlines()[1:]:
        dest, source, length = [int(n) for n in line.split()]
        final_map[range(source, source+length)] = range(dest, dest+length)
    
    return final_map


def overlaps(x: range, y: range):
    return max(x.start, y.start) < min(x.stop, y.stop)


def split_overlapping_ranges(x: range, y: range):
    # If there's no overlap, just return the original range
    if not overlaps(x, y):
        return x



print(overlaps(range(55,68), range(50, 69)))

sys.exit()


def generate_new_map(seeds_map, next_map):
    final_map = {}
    for seed_source, seed_dest in seeds_map.items():
        for next_source, next_dest in next_map.items():
            pass





seeds_to_soil = map_instructions(inp[1])
print(seeds_to_soil)
sys.exit()
soil_to_fertilizer = map_instructions(inp[2])
fertilizer_to_water =map_instructions(inp[3])
water_to_light = map_instructions(inp[4])
light_to_temperature = map_instructions(inp[5])
temperature_to_humidity = map_instructions(inp[6])
humidity_to_location = map_instructions(inp[7])

sys.exit()


def map_instructions(s: str):
    final_map = []
    for line in s.splitlines()[1:]:
        dest, source, length = [int(n) for n in line.split()]
        final_map.append(Range(dest, source, length))
    
    return final_map

seeds_to_soil = map_instructions(inp[1])
soil_to_fertilizer = map_instructions(inp[2])
fertilizer_to_water =map_instructions(inp[3])
water_to_light = map_instructions(inp[4])
light_to_temperature = map_instructions(inp[5])
temperature_to_humidity = map_instructions(inp[6])
humidity_to_location = map_instructions(inp[7])

def follow_map(n, map_: Range):
    for range_ in map_:
        if range_.source <= n < range_.source + range_.length:
            return range_.dest + n - range_.source
    
    return n



def find_location(seed):
    # print(seed)
    soil = follow_map(seed, seeds_to_soil)
    fertilizer = follow_map(soil, soil_to_fertilizer)
    water = follow_map(fertilizer, fertilizer_to_water)
    light = follow_map(water, water_to_light)
    temperature = follow_map(light, light_to_temperature)
    humidity = follow_map(temperature, temperature_to_humidity)
    location = follow_map(humidity, humidity_to_location)

    return location

locs = [find_location(seed) for seed in seeds]

print(f"p1: {min(locs)}")



### P2

locs = []
for pair in p2_seed_range:
    locs2 = [find_location(n) for n in range(pair.start, pair.stop)]
    locs.extend(locs2)

print(min(locs))



# p1 = 0
# p2 = 0

# print(f"{p1=}")
# print(f"{p2=}")






















if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
