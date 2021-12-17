#! /usr/bin/env python3.10

YEAR = '2021'
AOC_DAY = '17'

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

Point = namedtuple("Point", ["x", "y"])

if test:
    _test = 'target area: x=20..30, y=-10..-5'
    _t1 = Point(20, -10)
    _t2 = Point(30, -5)
else:
    _prod = 'target area: x=119..176, y=-141..-84'
    _t1 = Point(119, -141)
    _t2 = Point(176, -84)


def in_target_area(pt: Point, t1: Point, t2: Point):
    return t1.x <= pt.x <= t2.x and t1.y <= pt.y <= t2.y


def beyond_target_area(pt: Point, t1: Point, t2: Point):
    # return pt.y < t2.y  WHOOPS
    return pt.y < t1.y


def before_target_area(pt: Point, t1: Point, t2: Point):
    return pt.y < t2.y and pt.x < t1.x


def triangle_number(n):
    return (n * (n+1))/ 2

START = (0,0)


def step(pt: Point, velocity: Point):
    pt = Point(pt.x + velocity.x, pt.y + velocity.y)
    if velocity.x > 0:
        dx = velocity.x - 1
    else:
        dx = velocity.x
    velocity = Point(dx, velocity.y - 1)

    return pt, velocity



def shoot(velocity: Point, t1: Point, t2: Point):
    original_velocity = velocity
    pt = Point(0,0)
    highest = -math.inf
    for i in it.count(1):
        pt, velocity = step(pt, velocity)
        if pt.y > highest:
            highest = pt.y

        if in_target_area(pt, t1, t2):
            print(f"Successful. Ending Point: ({pt.x},{pt.y}) -- Starting Velocity: ({original_velocity.x},{original_velocity.y}) {highest=}")
            return highest
        if beyond_target_area(pt, t1, t2):
            # print(f"Beyond {original_velocity=}")
            return -math.inf # Sentinel stop value


# shoot(Point(6,9), _t1, _t2)


def find_highest(t1: Point, t2: Point):

    # determine minimum x velocity - triangle number
    for i in it.count(1):
        if triangle_number(i) >= t1.x:
            minimum_x_velocity = i
            break

    minimum_y_velocity = t1.y  # whoops. You had these backwards
    # minimum_y_velocity = t2.y
    
    maximum_x_velocity = t2.x
    print(f"{minimum_x_velocity=} {maximum_x_velocity=}")
    # input()

    velocities = []

    highest = -math.inf
    for x in range(minimum_x_velocity, maximum_x_velocity + 1):
    # for x in range(-999, 999):
        print(f"Starting new {x=}")
        for y in range(minimum_y_velocity, abs(t1.y)):
        # for y in range(-999, 999):
            height = shoot(Point(x,y), t1, t2)
            if height != -math.inf:
                velocities.append(Point(x,y))
            
            if height > highest:
                print(f"New Highest: {height=} old {highest=}")
                highest = height
            
            # we've shot past
            # if height == -math.inf and hit:
            #     break
            # input()

    print(highest)
    print(f"{len(velocities)=}")

find_highest(_t1, _t2)


# because the x velocity constantly decreases, there's a minimum x value that is needed


























if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
