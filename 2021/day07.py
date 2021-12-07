#! /usr/bin/env python3.10

TEST = False
# TEST = True

AOC_DAY = '07'

from statistics import median

def load_file(filename: str) -> str:
    """Loads an AOC file, returns a string"""

    with open(filename) as f:
        return f.read().rstrip("\n")


if TEST:
    filename = f"{AOC_DAY}.test"
else:
    filename = f"{AOC_DAY}.in"

ll = [int(i) for i in load_file(filename).split(',')]

total = 0
for i in ll:
    total += abs(median(ll) - i)

print(f"Part 1: {total}")

average = sum(ll)/len(ll)
average = round(average)
# print(average)
options = [average, average + 1, average - 1]

# average = 458 #92439832
# average = 457

potentials = []
for ave in options:
    total = 0
    for i in ll:
        difference = abs(ave - i)
        for i in range(difference + 1):
            total += i
    
    potentials.append(total)
    
print(f"Part 2: {min(potentials)}")