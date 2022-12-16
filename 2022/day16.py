#! /usr/bin/env python3.11

YEAR = '2022'
AOC_DAY = '16'

import itertools as it
import heapq
import math
import re
import sys
from collections import Counter, defaultdict, deque, namedtuple
from contextlib import suppress
from dataclasses import dataclass
from functools import cmp_to_key
from itertools import zip_longest
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



# monkeystrings = p.split('\n\n')
Node = namedtuple("Node", ["r", "c"])
Point = namedtuple("Point", ["x", "y"])
Range = namedtuple("Range", ["start", "end"])
# from string import ascii_lowercase

# def manhattan(a, b):
#     return sum(abs(val1-val2) for val1, val2 in zip(a,b))

p = load_lines(FILENAME)

# valves = {}
rates = {}
tunnels = {}

for line in p:
    _, valve, _, _, rate, _, _, _, _, *tuns = line.split()
    rate = int(re.findall(r'\-?\d+', rate)[0])
    # valves[valve] = False
    rates[valve] = rate
    tunnels[valve] = [t.strip(',') for t in tuns]
    # print(valve, rate, tunnels)



import networkx as nx
from copy import deepcopy

g = nx.Graph()

# # We start in tunnel AA
# g.add_node('AA')
# for t in tunnels['AA']:
#     g.add_edge('AA', t)

for valve, tunnel in tunnels.items():
    g.add_node(valve)
    g.graph[valve] = rates[valve]
    for t in tunnel:
        g.add_edge(valve, t)

# print(g.graph)


valuable_nodes = []
valuable_paths = []
# We start at valve AA
valuable_nodes.append('AA')

def find_all_paths(node):
    paths = []
    for target in g.nodes:
        if g.graph[target] != 0:
            path = nx.shortest_path(g, source=node, target=target)
            paths.append(path)

    return paths

def simulate(start_node, minutes):
    
    paths = find_all_paths(start_node)
    # print(paths)

    best = 0
    target = None

    for path in paths:
        dest = path[-1]
        weight = rates[dest] * (30 - minutes - len(path))
        print(path, '->', weight)
        # we want to find the cheapest path to go to next
        if weight > best:
            best = weight
            target = dest
            distance = len(path) - 1
    
    print(target, distance)
    return target, distance



# ### Run P1
# total = 0
# rate = 0
# target = 'AA'
# # turn 1 - move from A
# minutes = 0
# distance = 0

# nodes_to_check = set(deepcopy(valuable_nodes))
# while minutes <= 30:
#     print(minutes, target)
#     # increase total by rate
#     total += rate
#     # move
#     if distance:
#         distance -= 1
#         minutes += 1
#         continue

#     # increase rate
#     rate += rates[target]
#     rates[target] = 0
#     if nodes_to_check:
#         nodes_to_check.remove(target)

#         # find new target
#         target, distance = simulate(target, minutes)

#     # increase time
#     minutes += 1
#     # # turn 2 - open valve
#     # rate += rates[target]

# print(total)

sys.exit()



    
#     print()
#     print(node, rates[node])

# valuable_paths.sort(key=len)
# # print(valuable_paths)
# for path in valuable_paths:
#     print(path)
# print(len(valuable_paths))

# calculate shortest






















# def find_next_valve()
# def simulate_flow(starting_valve):
#     total = 0
#     rate = 0
#     reachable = set()
#     # move - step 1
#     valve = starting_valve
#     for time in range(29):
#         total += rate
#         # can I open a valve?
#         if rates[valve] != 0:
#             rates += rates[valve]
#             rates[valve] = 0
#         else: # I have to move
#             next, top = None, 0
#             for val, pres in tunnels[valve].items():
#                 if pres > top:
#                     next = val
#                     top = pres
            
#             # We found some pressure, so continue
#             if top != 0:
#                 continue



































if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
