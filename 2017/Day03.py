import sys
try:
    import numpy as np
except ImportError:
    np = None

# --- Constants ----------------------------------------------------------------

puzzle_input = 277678

#directions
N = (0, -1) 
W = (-1, 0)
S = (0, 1)
E = (1, 0)
turn_left = {N: W, W: S, S: E, E: N} # old: new direction

# --- Functions ----------------------------------------------------------------

def add_surround(array, x, y):
    '''Adds the surrounding nums per the problem'''
    sum_ = 0
    north = None if y-1 < 0 else y-1
    west = None if x-1 < 0 else x-1
    south = None if y+1==len(array) else y+1
    east = None if x+1==len(array[0]) else x+1

    try:
        sum_ += array[north][x]
    except TypeError:
        pass
    try:
        sum_ += array[north][east]
    except TypeError:
        pass
    try:
        sum_ += array[y][east]
    except TypeError:
        pass
    try:
        sum_ += array[south][east]
    except TypeError:
        pass
    try:
        sum_ += array[south][x]
    except TypeError:
        pass
    try:
        sum_ += array[south][west]
    except TypeError:
        pass
    try:
        sum_ += array[y][west]
    except TypeError:
        pass
    try:
        sum_ += array[north][west]
    except TypeError:
        pass
    
    return sum_

def pad_array(array, pad=0):
    '''Pads a rectangular array with the pad character'''
    for row in array:
        row.insert(0, pad)
        row.append(pad)
    length = len(array[0])
    array.insert(0, [pad] * length)
    array.append([pad] * length)

def spiral_move(array, x, y, dx, dy):
    '''Spiral moves in direction or rotates if it can. Pads zeroes as necessary'''
    x += dx
    y += dy
    if x < 0 or y < 0 or x == len(array[0]) or y == len(array):
        pad_array(array)
        x += 1
        y += 1
    new_dx, new_dy = turn_left[dx, dy]
    if array[y+new_dy][x+new_dx] == 0:
        dx, dy = new_dx, new_dy
    return x, y, dx, dy

def go(limit, initial_direction):
    array = [[1]]
    x, y = 0, 0
    dx, dy = initial_direction
    num = array[y][x]

    while num < limit:
        x, y, dx, dy = spiral_move(array, x, y, dx, dy)
        array[y][x] = add_surround(array, x, y)
        num = array[y][x]

    if np:
        print(np.matrix(array)) 
    else:
        for row in array:
            print(row)
    print()
    print(f"Last number found was: {array[y][x]}")

# --- Tests --------------------------------------------------------------------
def test_add_surround():
    sample_array = [[5,   4,  2], [10,  1,  1], [11, 23,  0]]
    assert(add_surround(sample_array, 2, 2) == 25)

def test_pad_array():
    pad_array_test = [[1]]
    pad_array(pad_array_test)
    assert(pad_array_test == [[0,0,0],[0,1,0],[0,0,0]])

# --- Main ---------------------------------------------------------------------
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Solve Advent of Code 2017 Day 3, Part 2')
    parser.add_argument('limit', metavar='N', type=int, nargs='?', default=puzzle_input, help='Puzzle input')
    args = parser.parse_args()
    go(args.limit, E)

