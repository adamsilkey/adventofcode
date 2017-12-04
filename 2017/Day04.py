import itertools
import sys
from collections import Counter

def part_one():
    with open('input.txt') as f:
        total = 0
        for line in f:
            list_ = line.split()
            set_ = list(set(line.split()))
            print(sorted(set_))
            print(sorted(list_))
            if sorted(set_) == sorted(list_):
                total += 1

        print(total)

def part_two():
    print('part two')
    with open('input.txt') as f:
        total = 0
        for line in f:
            list_ = line.split()
            set_ = list(set(line.split()))
            if sorted(set_) == sorted(list_):
                new_list = []
                for item in list_:
                    new_list.append(''.join(sorted(item)))
                if [k for k,v in Counter(new_list).items() if v>1]:
                    print('found dup')
                else:
                    print('found no dup')
                    total += 1

        print(total)

if __name__ == '__main__':
    part_one()
    part_two()
