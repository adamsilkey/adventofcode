import sys

puzzle_inp = '14,58,0,116,179,16,1,104,2,254,167,86,255,55,122,244'

puzzle_lis = [int(x) for x in range(256)]
puzzle_lengths = [int(x) for x in puzzle_inp.split(',')]

def solve(lis, lengths):
    pos = 0
    skip_size = 0
    lis_length = len(lis)
    for length in lengths:
        #original list

        #fast forward
        for i in range(pos):
            val = lis.pop(0)
            lis.append(val)

        #reverse
        sublist = lis[:length]
        sublist.reverse()

        #return new list
        lis = sublist + lis[length:]

        #return list to original state
        for i in range(pos):
            val = lis.pop()
            lis.insert(0, val)

        #position increase
        pos += skip_size + length
        pos = pos % lis_length

        #skip size increase
        skip_size += 1

        print(lis)

    print(lis)

solve([0,1,2,3,4], [3,4,1,5])

solve(puzzle_lis, puzzle_lengths)
