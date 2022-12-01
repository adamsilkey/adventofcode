import sys
from collections import defaultdict, deque

def parse_input(filename):
    with open(filename) as f:
        return f.readline()


def solve(inp, file_ = True):
    if file_:
        inp = parse_input(inp)

    groups = 0
    group_count = 0
    count = 0
    garbage = False
    ignore = False
    in_group = False
    garbage_count = 0
    for idx, char in enumerate(inp):
        #print(f'before groups {groups}')
        #print(char)
        if not garbage:
            if groups < 0:
                print(idx)
                sys.exit()
            if char == '{':
                groups += 1
                count += groups
                in_group = True
            elif char == '}':
                groups -= 1
            elif char == '<':
                garbage = True
                #print('entering garbage')

            if groups == 0 and in_group:
                #print(f'new count: {count}')
                in_group = False
        if garbage:
            garbage_count += 1
            print(char, garbage_count)
            if not ignore:
                if char == '!':
                    ignore = True
                    garbage_count -= 1
                if char == '>':
                    garbage = False
                    garbage_count -= 2
                    print(garbage_count)
                    print('exiting garbage')
            else:
                ignore = False
                garbage_count -= 1

        #print(f'after groups {groups}')
        #print()
        #input()


    print(count)
    print(garbage_count)
    print()
    return count

solve('<!!>', False)
solve('<<<<>', False)
solve('<{!>}>', False)
solve('<{o"i!a,<{i<a>', False)
solve('<random characters>', False)


assert(solve('{{<a!>},{<a!>},{<a!>},{<ab>}}', False) == 3)


solve('test_input.txt')
solve('input.txt')


