#! /usr/bin/env python3.10

YEAR = '2021'
AOC_DAY = '15'

import itertools as it
import math
import sys
from collections import Counter, defaultdict, deque, namedtuple
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


def load_ints(filename: str) -> list[int]:
    """Returns a list of ints"""

    return [int(i) for i in load_lines(filename)]


def load_comma_separated_ints(filename: str) -> list[int]:
    """Returns a list of ints from a comma separated list of ints"""

    return [int(i) for i in load_file(filename).strip().split(",")]


Node = namedtuple("Node", ["r", "c"])



def load_puzzle(filename):
    ll = load_lines(filename)

    graph = []
    for line in ll:
        graph.append([int(c) for c in line])

    max_r = len(graph)
    max_c = len(graph[0])

    distances = {}
    for r in range(max_r):
        for c in range(max_c):
            distances[Node(r,c)] = math.inf

    distances[Node(0,0)] = 0

    not_visited = set(distances.keys())
    # not_visited.remove(Node(0,0))

    def inbounds(node: Node):
        return 0 <= node.r < max_r and 0 <= node.c < max_c

    check_next = Node(0,0)

    return check_next, distances, not_visited, graph, inbounds


check_next, distances, not_visited, graph, inbounds = load_puzzle(filename)


def determine_shortest(node: Node, distances: dict, not_visited: set, graph, inbounds):

    directions = [
        Node(-1, 0),    # N
        Node(1, 0),     # S
        Node(0, 1),     # E
        Node(0, -1),    # W
    ]

    shortest = math.inf

    for d in directions:
        next_node = Node(node.r + d.r, node.c + d.c)

        if next_node not in not_visited:
            continue
        if not inbounds(next_node):
            continue

        distance = graph[next_node.r][next_node.c] + distances[node]
        if distance < distances[next_node]:
            distances[next_node] = distance

        if distance < shortest:
            shortest = distance

    not_visited.remove(node)

    # print(shortest)

    check_next = None
    shortest = math.inf
    for node, distance in distances.items():
        # print(node, distance)
        if distance < shortest and node in not_visited:
            shortest = distance
            check_next = node

    return check_next, distances, not_visited


cn, ds, nv = check_next, distances, not_visited

while cn:
    cn, ds, nv = determine_shortest(cn, ds, nv, graph, inbounds)
    print(cn)
    # for k, v in ds.items():
    #     if v != math.inf:
    #         # print(k, v)
    # print()
    # input()
for k, v in ds.items():
    print(k, v)

# ntc, ds, nv = determine_shortest(ntc, ds, nv, graph, inbounds)
# print(ntc)
# for k, v in ds.items():
#     if v != math.inf:
#         print(k, v)
# print()


# Start at 0,0. Check all the nodes around.

# For each point, check to the N, S, E, W
# Be sure to check for out of bounds

# r, c = 0, 0

# # 0,1 -> Check to the E
# new_distance = distances[r][c+1] + distances[r][c]

# if new_distance < distances[r][c+i]:
#     distances[r][c+i] = new_distance

# # 1,0 -> Check S
# new_distance = distances[r+1][c] + distances[r][c]

# if new_distance < distances[r][c+1]:
#     distances[r+1][c] = new_distance


# def determine_shortest(node: Node, graph, distances, visited: set, inbounds):

#     add_to_visited = set()

#     for d in directions:

#         new_distance = graph[next_node.r][next_node.c] + distances[node]
#         if new_distance < distances[next_node]:
#             distances[next_node] = new_distance

#         if new_distance < shortest:
#             shortest = new_distance
#             add_to_visited.clear()
#             add_to_visited.add(next_node)
#         elif new_distance == shortest:
#             add_to_visited.add(next_node)   

#     visited.update(add_to_visited)

#     return distances, visited




































if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
