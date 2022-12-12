#! /usr/bin/env python3.11

YEAR = '2022'
AOC_DAY = '12'

import itertools as it
import heapq
import math
import re
import sys
from collections import Counter, defaultdict, deque, namedtuple
from contextlib import suppress
from dataclasses import dataclass
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



'''
## Regex / list/map helpers
# number_of_stacks = max(map(int, stacks.pop().split()))
# qty, old, new = list(map(int, re.findall(r'\d+', move)))
#   - map(function, target)
#   - map needs to bec onverted to a list (or other object)
# Point = namedtuple("Point", ["x", "y"])


    
    # @classmethod
    # def fromstring(cls, string):
    #     for line in string.split('\n'):
    #         match line.split():
    #             case 'Monkey', x:
    #                 id_ = int(x[0])
    #             case 'Starting', 'items:', *items:
    #                 items = deque([int(item.rstrip(',')) for item in items])
    #             case 'Operation:', *rest, operation, value:
    #                 if value.isdigit():
    #                     value = int(value)
    #             case 'Test:', *rest, divisor:
    #                 divisor = divisor
    #             case 'If', 'true:', *rest, truemonkey:
    #                 truemonkey = int(truemonkey)
    #             case 'If', 'false:', *rest, falsemonkey:
    #                 falsemonkey = int(falsemonkey)
        
    #     return cls(
    #         id_,
    #         items,
    #         operation,
    #         value,
    #         divisor,
    #         truemonkey,
    #         falsemonkey,
    #     )
'''

# monkeystrings = p.split('\n\n')
# p = load_file(FILENAME)


from string import ascii_lowercase

Node = namedtuple("Node", ["r", "c"])


def load_puzzle(filename):
    p = load_lines(filename)

    # Set elevation
    elevation = {'S': 0, 'E': 25}
    for idx,c in enumerate(ascii_lowercase):
        elevation[c] = idx

    graph = []
    for irow, row in enumerate(p):
        graph_row = []
        for icol, col in enumerate(row):
            graph_row.append(elevation[col])
            if col == 'S':
                start_node = Node(irow, icol)
            if col == 'E':
                end_node = Node(irow, icol)
        
        graph.append(graph_row)

    max_r = len(graph)
    max_c = len(graph[0])

    distances = {}
    for r in range(max_r):
        for c in range(max_c):
            distances[Node(r,c)] = math.inf

    distances[start_node] = 0
    print(f"{distances[start_node]=}")

    not_visited = set(distances.keys())
    # not_visited.remove(Node(0,0))

    def inbounds(node: Node):
        return 0 <= node.r < max_r and 0 <= node.c < max_c

    # check_next = {Node(0,0): 0}
    check_next = []
    # heapq.heappush(check_next, (0, start_node))
    heapq.heappush(check_next, (0, start_node))

    return check_next, distances, not_visited, start_node, end_node, graph, inbounds


def load_puzzle_p2(filename):
    p = load_lines(filename)

    # Set elevation
    elevation = {'S': 0, 'E': 25}
    for idx,c in enumerate(ascii_lowercase):
        elevation[c] = idx

    starting_nodes = []
    graph = []
    for irow, row in enumerate(p):
        graph_row = []
        for icol, col in enumerate(row):
            graph_row.append(elevation[col])
            if col in ['S', 'a']:
                starting_nodes.append(Node(irow, icol))
            if col == 'E':
                end_node = Node(irow, icol)
        
        graph.append(graph_row)


    return graph, end_node, starting_nodes

def check_p2(graph, end_node, start_node):
    max_r = len(graph)
    max_c = len(graph[0])
    distances = {}
    for r in range(max_r):
        for c in range(max_c):
            distances[Node(r,c)] = math.inf

    distances[start_node] = 0
    # print(f"{distances[start_node]=}")

    not_visited = set(distances.keys())
    # not_visited.remove(Node(0,0))

    def inbounds(node: Node):
        return 0 <= node.r < max_r and 0 <= node.c < max_c

    # check_next = {Node(0,0): 0}
    check_next = []
    # heapq.heappush(check_next, (0, start_node))
    heapq.heappush(check_next, (0, start_node))

    return check_next, distances, not_visited, start_node, end_node, graph, inbounds

# print(graph)

def determine_shortest(check_next, distances: dict, not_visited: set, graph, inbounds):

    directions = [
        Node(-1, 0),    # N
        Node(1, 0),     # S
        Node(0, 1),     # E
        Node(0, -1),    # W
    ]

    node = heapq.heappop(check_next)[1]
    node_height = graph[node.r][node.c]
    # print()
    # print(f"Checking {node=}")
    # print(f"{node_height=}")

    for d in directions:
        next_node = Node(node.r + d.r, node.c + d.c)
        if not inbounds(next_node):
            continue

        # only check for the next nodes
        next_height = graph[next_node.r][next_node.c]
        if next_height - node_height > 1:
            # print(f"This next node is too big for me: {next_node=}")
            continue
        if next_node not in not_visited:
            continue
        # print(f"{next_node=}")
        # print(f"{next_height=}")
        # input()

        distance = distances[node] + 1
        if distance < distances[next_node]:
            distances[next_node] = distance
            heapq.heappush(check_next, (distance, next_node))

    not_visited.remove(node)

    return check_next, distances, not_visited

# check_next, distances, not_visited, start_node, end_node, graph, inbounds = load_puzzle(FILENAME)

# # print(graph)
# # input()
# while check_next:
#     check_next, distances, not_visited = determine_shortest(check_next, distances, not_visited, graph, inbounds)

# for node, distance in distances.items():
#     print(node, distance)

# print(f"Part 1: {end_node} {distances[end_node]}")

graph, end_node, starting_nodes = load_puzzle_p2(FILENAME)

shortest = math.inf

for node in starting_nodes:
    check_next, distances, not_visited, start_node, end_node, graph, inbounds = check_p2(graph, end_node, node)

# print(graph)
# input()
    while check_next:
        check_next, distances, not_visited = determine_shortest(check_next, distances, not_visited, graph, inbounds)

    # for node, distance in distances.items():
    #     print(node, distance)

    # print(f"Part 1: {end_node} {distances[end_node]}")
    if distances[end_node] < shortest:
        shortest = distances[end_node]

print(shortest)


sys.exit()

def run():
    import time

    # Part 1
    tic = time.perf_counter()
    check_next, distances, not_visited, graph, inbounds = load_puzzle(filename, 1)
    cn, ds, nv = check_next, distances, not_visited

    while cn:
        cn, ds, nv = determine_shortest(cn, ds, nv, graph, inbounds)

    last_node = Node(len(graph) - 1, len(graph[0]) - 1)
    print(f"Part 1: {last_node} {ds[last_node]}")
    toc = time.perf_counter()
    print(f"Elapsed: {toc - tic:0.4f} seconds")


    # Part 2
    tic = time.perf_counter()
    check_next, distances, not_visited, graph, inbounds = load_puzzle(filename, 2)
    cn, ds, nv = check_next, distances, not_visited

    while cn:
        cn, ds, nv = determine_shortest(cn, ds, nv, graph, inbounds)

    last_node = Node(len(graph) - 1, len(graph[0]) - 1)
    print(f"Part 2: {last_node} {ds[last_node]}")
    toc = time.perf_counter()
    print(f"Elapsed: {toc - tic:0.4f} seconds")

# run()





































if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")


'''
    elif part == 2:
        # graph = []
        # # increase = 0
        # for j in range(5):
        #     for line in ll:
        #         row = []
        #         for i in range(5):
        #             offset = j + i
        #             for c in line:
        #                 c = int(c) + offset
        #                 if c > 9:
        #                     c -= 9
        #                 row.append(c)
        #         graph.append(row)

        # max_r = len(graph)
        # max_c = len(graph[0])

        # distances = {}
        # for r in range(max_r):
        #     for c in range(max_c):
        #         distances[Node(r,c)] = math.inf
        pass

'''