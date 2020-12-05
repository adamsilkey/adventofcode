#! /usr/bin/env python3

print("day 5")

with open("input/2020-05.in") as f:
    day5 = [line.strip() for line in f]

ROWS = 128
COLUMNS = 8

def get_row(seat_id):
    upper = 127
    lower = 0
    rows = seat_id[0:7]
    print(rows)

    for idx, c in enumerate(rows):
        if idx < 6:

            tmp = (upper - lower) // 2
            if c == "F":
                upper = lower + tmp
            elif c == "B":
                lower = lower + tmp + 1
            # print(f"{c} {lower} - {upper} || {tmp}")
        else:
            if c == "F":
                return lower
            else:
                return upper


def get_column(seat_id):
    left = 0
    right = 7
    for idx, c in enumerate(seat_id[7:]):
        if idx < 2:
            tmp = (right - left) // 2
            if c == "L":
                right = left + tmp
            elif c == "R":
                left = left + tmp + 1
            # print(f"{c} {left} - {right} || {tmp}")
        else:
            if c == "L":
                return left
            else:
                return right


highest = 0

all_seats = []

for seat in day5:
    row = get_row(seat)
    col = get_column(seat)

    id_ = (row * 8) + col
    all_seats.append(id_)
    if id_ > highest:
        highest = id_

print(f"part_one {highest}")
print(sorted(all_seats))

for i in range(46, 992):
    if i not in all_seats:
        print(i)
        break



