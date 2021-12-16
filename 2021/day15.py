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

    check_next = {Node(0,0): 0}

    return check_next, distances, not_visited, graph, inbounds




def determine_shortest(check_next: dict, distances: dict, not_visited: set, graph, inbounds):

    directions = [
        Node(-1, 0),    # N
        Node(1, 0),     # S
        Node(0, 1),     # E
        Node(0, -1),    # W
    ]

    shortest = min(check_next.values())
    for node, distance in check_next.items():
        if distances[node] == shortest:
            break

    check_next.pop(node)

    for d in directions:
        next_node = Node(node.r + d.r, node.c + d.c)

        if next_node not in not_visited:
            continue
        if not inbounds(next_node):
            continue

        distance = graph[next_node.r][next_node.c] + distances[node]
        if distance < distances[next_node]:
            distances[next_node] = distance
            check_next[next_node] = distance

    not_visited.remove(node)

    return check_next, distances, not_visited


# part 1

def part_one():
    check_next, distances, not_visited, graph, inbounds = load_puzzle(filename)
    cn, ds, nv = check_next, distances, not_visited

    while cn:
        cn, ds, nv = determine_shortest(cn, ds, nv, graph, inbounds)
        # print(cn)
        # for k, v in ds.items():
        #     if v != math.inf:
        #         # print(k, v)
        # print()
        # input()
    for k, v in ds.items():
        print(k, v)

# part_one()
# import sys;sys.exit()


def load_puzzle_part2(filename):
    ll = load_lines(filename)

    graph = []
    # increase = 0
    for j in range(5):
        for line in ll:
            row = []
            for i in range(5):
                offset = j + i
                for c in line:
                    c = int(c) + offset
                    if c > 9:
                        c -= 9
                    row.append(c)
            graph.append(row)

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

    check_next = {Node(0,0): 0}

    return check_next, distances, not_visited, graph, inbounds


def part_two():
    import time
    tic = time.perf_counter()
    check_next, distances, not_visited, graph, inbounds = load_puzzle_part2(filename)
    cn, ds, nv = check_next, distances, not_visited

    while cn:
        cn, ds, nv = determine_shortest(cn, ds, nv, graph, inbounds)

    last_node = Node(len(graph) - 1, len(graph[0]) - 1)
    print(last_node, ds[last_node])
    toc = time.perf_counter()
    print(f"Elapsed: {toc - tic:0.4f} seconds")


part_two()






























if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
