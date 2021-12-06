#! /usr/bin/env python3.10

TEST = False
from collections import Counter

def load_file(filename: str) -> str:
    """Loads an AOC file, returns a string"""

    with open(filename) as f:
        return f.read().rstrip("\n")


if TEST:
    ll = load_file("06.test").strip()
else:
    ll = '4,1,1,4,1,2,1,4,1,3,4,4,1,5,5,1,3,1,1,1,4,4,3,1,5,3,1,2,5,1,1,5,1,1,4,1,1,1,1,2,1,5,3,4,4,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,5,1,1,1,4,1,2,3,5,1,2,2,4,1,4,4,4,1,2,5,1,2,1,1,1,1,1,1,4,1,1,4,3,4,2,1,3,1,1,1,3,5,5,4,3,4,1,5,1,1,1,2,2,1,3,1,2,4,1,1,3,3,1,3,3,1,1,3,1,5,1,1,3,1,1,1,5,4,1,1,1,1,4,1,1,3,5,4,3,1,1,5,4,1,1,2,5,4,2,1,4,1,1,1,1,3,1,1,1,1,4,1,1,1,1,2,4,1,1,1,1,3,1,1,5,1,1,1,1,1,1,4,2,1,3,1,1,1,2,4,2,3,1,4,1,2,1,4,2,1,4,4,1,5,1,1,4,4,1,2,2,1,1,1,1,1,1,1,1,1,1,1,4,5,4,1,3,1,3,1,1,1,5,3,5,5,2,2,1,4,1,4,2,1,4,1,2,1,1,2,1,1,5,4,2,1,1,1,2,4,1,1,1,1,2,1,1,5,1,1,2,2,5,1,1,1,1,1,2,4,2,3,1,2,1,5,4,5,1,4'
    # ll = load_file("06.in").strip()


ll = [int(i) for i in ll.split(',')]

# c = Counter(ll)

# print(c)

# 6
# 5
# 4
# 3
# 2
# 1
# 0, 8
# 6, 7
# 5, 6
# 4, 5
# 3, 4


def make_many_fish(school: list[int], days: int):

    school = Counter(school)
    school[6] = 0
    school[7] = 0
    school[8] = 0

    for i in range(1, days+1):

        swap = Counter({0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0})

        # Swap everything down

        swap[7] = school[8]
        swap[6] = school[7]
        swap[5] = school[6]
        swap[4] = school[5]
        swap[3] = school[4]
        swap[2] = school[3]
        swap[1] = school[2]
        swap[0] = school[1]

        happy_fish = school[0]
        swap[8] = happy_fish
        swap[6] += happy_fish

        school = swap

        # print(f"Day {i} | School: {school}")
        # input()

    print(f"Final school total: {school[0] + school[1] + school[2] + school[3] + school[4] + school[5] + school[6] + school[7] + school[8]}")

# make_many_fish([5], 80)

# make_many_fish([3,4,3,1,2], 80)
make_many_fish(ll, 256)
make_many_fish(ll, 1024)

import sys;sys.exit()

def make_a_fish(start: int, days: int):
    school = [start]

    print(f"School: {school}")
    # school = [3,4,3,1,2]
    for i in range(1, days + 1):
        for idx, days in enumerate(school):
            school[idx] -= 1
            if school[idx] == -1:
                school.append(9)
                school[idx] = 6
        # print(f"School: {school}")
        print(f"Original Fish Days Remaining: {start} | Day: {i} | Total Fish: {len(school)}")
        # input()

make_a_fish(5,80)
# # import sys;sys.exit()
# make_a_fish(5, 256)
# make_a_fish(4, 256)
# make_a_fish(3, 256)
# make_a_fish(2, 256)
# make_a_fish(1, 256)