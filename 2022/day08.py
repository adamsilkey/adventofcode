#! /usr/bin/env python3.11

YEAR = '2022'
AOC_DAY = '08'

import itertools as it
import re
import sys
from collections import Counter, defaultdict, deque, namedtuple
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



## Regex / list/map helpers
# number_of_stacks = max(map(int, stacks.pop().split()))
# qty, old, new = list(map(int, re.findall(r'\d+', move)))
#   - map(function, target)
#   - map needs to bec onverted to a list (or other object)

p = load_file(FILENAME)


Point = namedtuple("Point", ["x", "y"])

directions = dict(
    # NW = Point(-1, -1),
    N = Point(0, -1),
    # NE = Point(1, -1),
    W = Point(-1, 0),
    E = Point(1, 0),
    # SW = Point(-1, 1),
    S = Point(0, 1),
    # SE = Point(1, 1),
)



class Jungle:

    def __init__(self, cavern_map: str):
        self.grid = []
        for line in cavern_map.strip().splitlines():
            self.grid.append([int(i) for i in line])

        self.dimension = len(self.grid)
        self.visible = []
        for _ in range(self.dimension):
            self.visible.append([dict(N=None, S=None, E=None, W=None) for _ in range(self.dimension)])
        self.score = []
        for _ in range(self.dimension):
            self.score.append([1 for _ in range(self.dimension)])
        

    def inbounds(self, point: Point):
        return 0 <= point.x < self.dimension and 0 <= point.y < self.dimension
    
    def onedge(self, point: Point):
        if point.x == 0 or point.x == self.dimension or point.y == 0 or point.y == self.dimension:
            return True
        else:
            return False

    def score_direction(self, point: Point, direction_name):
        direction = directions[direction_name]
        dx = direction.x
        dy = direction.y
        next_point = Point(point.x + dx, point.y + dy)
        # print(f"{next_point=}")
        visible_trees = 0
        while self.inbounds(next_point):
            visible_trees += 1
            print(f"{next_point=} {visible_trees=}")
            # if next tree is taller than original tree, break
            # if next tree is lower than original tree, continue
            if self.grid[next_point.y][next_point.x] < self.grid[point.y][point.x]:
                next_point = Point(next_point.x + dx, next_point.y + dy)
            else:
                break
                # advance
                # print(f"{dx=}, {dy=}")
                # print(next_point)
        # no break, is visible
        print("HELLOO", visible_trees)
        self.score[point.y][point.x] *= visible_trees
    
    def score_all_directions(self, point: Point):
        # if self.onedge(point):
        #     x = point.x
        #     y = point.y
        #     for k in self.visible[y][x]:
        #         self.visible[y][x][k] = True
        # else:
        for k in directions:
            self.score_direction(point, k)
    
    # def look_direction(self, point: Point, direction_name):
    #     direction = directions[direction_name]
    #     dx = direction.x
    #     dy = direction.y
    #     next_point = Point(point.x + dx, point.y + dy)
    #     print(f"{next_point=}")
    #     while self.inbounds(next_point):
    #         # if next tree is taller than original tree, break
    #         if self.grid[next_point.y][next_point.x] >= self.grid[point.y][point.x]:
    #             self.visible[point.y][point.x][direction_name] = False
    #             break
    #         else:
    #             # advance
    #             # print(f"{dx=}, {dy=}")
    #             next_point = Point(next_point.x + dx, next_point.y + dy)
    #             print(next_point)
    #     # no break, is visible
    #     else:
    #         self.visible[point.y][point.x][direction_name] = True
    
    # def look_all_directions(self, point: Point):
    #     if self.onedge(point):
    #         x = point.x
    #         y = point.y
    #         for k in self.visible[y][x]:
    #             self.visible[y][x][k] = True
    #     else:
    #         for k in directions:
    #             self.look_direction(point, k)
    
    def score_trees(self):
        for y, row in enumerate(self.grid):
            for x, _ in enumerate(row):
                self.score_all_directions(Point(x,y))

    # def scan_trees(self):
    #     for y, row in enumerate(self.grid):
    #         for x, _ in enumerate(row):
    #             self.look_all_directions(Point(x,y))
    
    def determine_total_score(self):
        self.score_trees()
        top = 0
        for y, row in enumerate(self.grid):
            for x, _ in enumerate(row):
                if self.score[y][x] > top:
                    top = self.score[y][x]

        print(top)
        return(top)
        
    #     # print(visible)
    #     return visible
    # def determine_total_visible(self):
    #     self.scan_trees()
    #     visible = 0
    #     for y, row in enumerate(self.grid):
    #         for x, _ in enumerate(row):
    #             if any(True == visible for visible in self.visible[y][x].values()):
    #                 visible += 1
        
    #     # print(visible)
    #     return visible


jgl = Jungle(p)
    

# print(jgl.grid)
# print(jgl.visible)

# jgl.look_all_directions(Point(1,1))
# jgl.score_trees()
# print(jgl.visible)
# jgl.score_direction(Point(2,3), 'N')
# jgl.score_direction(Point(2,3), 'S')
# jgl.score_direction(Point(2,3), 'E')
# jgl.score_direction(Point(2,3), 'W')
# jgl.score_all_directions(Point(1,1))
jgl.determine_total_score()
# print(jgl.score)


    # def increment(self, pt: Point) -> bool:
    #     self.grid[pt.y][pt.x] += 1

    #     return self.grid[pt.y][pt.x] > 9

    # def step_one(self):
    #     # First, the energy level of each octopus increases by 1
    #     for y, row in enumerate(self.grid):
    #         for x, _ in enumerate(row):
    #             self.increment(Point(x, y))

    # # Step Two
    # def flash(self, pt: Point, flashed: set):

    #     if pt in flashed:
    #         return flashed

    #     flashed.add(pt)

    #     for d in directions.values():
    #         adjacent = Point(pt.x + d.x, pt.y + d.y)
    #         if self.inbounds(adjacent) and self.increment(adjacent): 
    #             self.flash(adjacent, flashed)

    #     return flashed

    # def step_two(self) -> int:
    #     flashed = set()
    #     for y, row in enumerate(self.grid):
    #         for x, i in enumerate(row):
    #             if i > 9:
    #                 flashed = self.flash(Point(x,y), flashed)

    #     return len(flashed)

    # # Step Three
    # def step_three(self):
    #     for y, row in enumerate(self.grid):
    #         for x, i in enumerate(row):
    #             if i > 9:
    #                 self.grid[y][x] = 0

    # def print(self):
    #     for y, row in enumerate(self.grid):
    #         for x, i in enumerate(row):
    #             if i > 9:
    #                 i = ' '
    #             print(i, end='')
    #         print()
        
    #     print()  # Make a new line to demarcate the end of the grid

    # def cycle(self, pprint=False):
    #     self.step_one()

    #     flashed_total = self.step_two()

    #     self.step_three()

    #     if pprint:
    #         self.print()

    #     return flashed_total

    # def simulate(self, rounds):
    #     flashed_total = 0
    #     for _ in range(rounds):
    #         flashed_total += self.cycle()

    #     return flashed_total


# p1 = OctopusCavern(ll)
# print(f"p1: {p1.simulate(100)}")

# p2 = OctopusCavern(ll)
# counter = 0
# while True:
#     counter += 1
#     if p2.cycle() == 100:
#         print(f"p2: {counter}")
#         break
























if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
