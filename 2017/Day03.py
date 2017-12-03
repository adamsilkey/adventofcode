import sys

puzzle_input = 277678

# a = [1,1,2,4,5,10,11,23,25,26,54,57,59,122,133,142,147,304,330,351,362,747,806,880,931]

# print(a[0:1])
# print(a[1:9])   # 8 elements
# print(a[9:25])  # 16 elements


sample_array = [[0, 0,   0,  0, 0],
                [0, 5,   4,  2, 0],
                [0, 10,  1,  1, 0],
                [0, 11, 23,  0, 0],
                [0, 0,   0,  0, 0]]


N, S, E, W = (0, -1), (0, 1), (1, 0), (-1, 0) #directions
turn_left = {N: W, W: S, S: E, E: N} # old: new direction

def add_surround(array, x, y):
    # doesn't handle out of bounds... even though it used to, I DELETED THE CODE
    sum_ = 0

    #North 
    sum_ += array[y][x-1]
    #NorthEast
    sum_ += array[y+1][x-1]
    #East
    sum_ += array[y+1][x]
    #SouthEast
    sum_ += array[y+1][x+1]
    #South
    sum_ += array[y][x+1]
    #SouthWest
    sum_ += array[y-1][x+1]
    #West
    sum_ += array[y-1][x]
    #NorthWest
    sum_ += array[y-1][x-1]
    
    return sum_

assert(add_surround(sample_array, 3, 3) == 25)

def go(limit, initial_direction):
    array = [[0, 0, 0],
             [0, 1, 0],
             [0, 0, 0]]
    x, y = 1, 1
    dx, dy = initial_direction
    num = array[y][x]

    while num < limit:
        try:
            array[y][x+2]   #See if we need to add another block of padding zeros
        except IndexError:
            # With an index error, we pad our matrix with 0s
            for row in array:
                row.insert(0,0)
                row.append(0)
            length = len(array[0])
            array.insert(0, [0] * length)
            array.append([0] * length)
            x += 1
            y += 1

        # see if we need to rotate
        new_dx, new_dy = turn_left[dx,dy]
        if array[y+new_dy][x+new_dx] == 0:
            dx, dy = new_dx, new_dy
            print('you need to rotate')

        x += dx
        y += dy
        print(x, y)
        print(array[y][x])
        print(add_surround(array, x, y))
        array[y][x] = add_surround(array, x, y)

        num = array[y][x]

    #while block ended
    for row in array:
        print(row)

    print(x,y)
    print(array[y][x])


go(puzzle_input+1, S)

#go(2, E)

