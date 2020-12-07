#! /usr/bin/env python3

print("day 5")

with open("input/2020-05.in") as f:
    day5 = [line.strip() for line in f]

# ROWS = 128
# COLUMNS = 8


def get_row(boarding_pass):
    upper = 127
    lower = 0
    for idx, c in enumerate(boarding_pass[:7]):
        if idx < 6:
            tmp = (upper - lower) // 2
            if c == "F":
                upper = lower + tmp
            elif c == "B":
                lower = lower + tmp + 1
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

print(f"part_one {max(all_seats)}")

for i in range(min(all_seats), max(all_seats) + 1):
    if i not in all_seats:
        print(f"part_two {i}")
        break
