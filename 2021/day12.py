#! /usr/bin/env python3.10

YEAR = '2012'
AOC_DAY = '12'

import itertools as it
import sys
from collections import Counter, defaultdict, deque
from dataclasses import dataclass

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
    filename = f"{AOC_DAY}.test"
else:
    filename = f"{AOC_DAY}.in"

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




# class Node:
#     def __init__(self, name: str):
#         self.name = name
#         self.links = set()
#         self.small = self.name.islower()   # all lowercase - small | all uppercase - big

#     def __str__(self):
#         return f"{self.name}: {self.links}"

#     def __hash__(self):
#         return hash(self.name)



def parse_input(lines):

    cavern_map = {}
    for line in lines:
        a, b = line.split('-')
        
        if a not in cavern_map:
            cavern_map[a] = []
        if b not in cavern_map:
            cavern_map[b] = []
        
        cavern_map[a].append(b)
        cavern_map[b].append(a)
    
    return cavern_map


ll = parse_input(load_lines(filename))

# for node, links in ll.items():
#     print(node, links)



def find_all_paths2(cavern_map, node=None, current_path=None, found_paths=None):
    if node is None:
        node = 'start'

    if found_paths is None:
        found_paths = []

    if current_path is None:
        current_path = []


    # Don't go visiting if we've already been to this small cave
    if node.islower() and node in current_path:
        if node in ['start', 'end']:
            return current_path, found_paths
        else:
            # current_path.append(node)

            counts = Counter([lower_node for lower_node in current_path if lower_node.islower()])
            # print(counts)
            # input()
            most_common = counts.most_common(2)
            total = 0
            for elem in most_common:
                total += elem[1]
            if total > 2:
                return current_path, found_paths
            # else:
            #     for next_node in cavern_map[node]:
            #         current_path, found_paths = find_all_paths2(cavern_map, next_node, current_path, found_paths)

    # print(current_path)
    current_path.append(node)

    if node == 'end':
        print(f"found the end: {current_path}")
        found_paths.append(','.join(current_path))   # Can't just append the list, because it's constantly getting eaten
        current_path.pop()
        return current_path, found_paths

    for next_node in cavern_map[node]:
        current_path, found_paths = find_all_paths2(cavern_map, next_node, current_path, found_paths)

    current_path.pop()
    
    return current_path, found_paths

# map_test1 = {"start": ["end"], "end": ["start"]}
# _, paths = find_all_paths(map_test1)
# print(paths)

# map_test2 = {"start": ["A"], "A": ["end"], "end":["A"]}
# _, paths = find_all_paths(map_test2)
# print(paths)
    
_, paths = find_all_paths2(ll)
print(paths)
print(f"p2: {len(paths)}")

import sys;sys.exit()












def find_all_paths(cavern_map, node=None, current_path=None, found_paths=None):
    if node is None:
        node = 'start'

    if found_paths is None:
        found_paths = []

    if current_path is None:
        current_path = []

    # if node == 'start' and len(current_path) > 1:
    #     return current_path, found_paths

    # Don't go visiting if we've already been to this small cave
    if node.islower() and node in current_path:
        return current_path, found_paths

    current_path.append(node)
    # print(current_path)

    if node == 'end':
        print(f"found the end: {current_path}")
        found_paths.append(','.join(current_path))   # Can't just append the list, because it's constantly getting eaten
        current_path.pop()
        return current_path, found_paths

    for next_node in cavern_map[node]:
        current_path, found_paths = find_all_paths(cavern_map, next_node, current_path, found_paths)

    current_path.pop()
    
    return current_path, found_paths

# map_test1 = {"start": ["end"], "end": ["start"]}
# _, paths = find_all_paths(map_test1)
# print(paths)

# map_test2 = {"start": ["A"], "A": ["end"], "end":["A"]}
# _, paths = find_all_paths(map_test2)
# print(paths)
    
_, paths = find_all_paths(ll)
print(paths)
print(len(paths))

# import sys;sys.exit()



