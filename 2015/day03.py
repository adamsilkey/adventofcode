#! /usr/bin/env python3.10
# Advent of Code 2015 - Day 03
#

from collections import Counter

with open('input/03.in') as f:
    moves = [c for c in f.read().strip()]


# Part 1

def do_move(x, y, move):
    match move:
        case '^':
            y += 1
        case 'v':
            y -= 1
        case '<':
            x -= 1
        case '>':
            x += 1
    return x, y

houses = set()
houses.add((0,0))

x, y = 0, 0

for move in moves:
    x, y = do_move(x, y, move)
    houses.add((x,y))

print(f"Part 1: {len(houses)}")


# Part 2

santa_x, santa_y, robot_x, robot_y = 0, 0, 0, 0

houses = set()
houses.add((0,0))
moves = iter(moves)

for santa, robot in zip(moves, moves):
    santa_x, santa_y = do_move(santa_x, santa_y, santa)
    robot_x, robot_y = do_move(robot_x, robot_y, robot)

    houses.add((santa_x, santa_y))
    houses.add((robot_x, robot_y))

print(f"Part 2: {len(houses)}")