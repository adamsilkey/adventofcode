#! /usr/bin/env python3.10
# Advent of Code 2015 - Day 04
#

from hashlib import md5
from itertools import count

test_key = 'abcdef'
my_key = 'bgvyzdsv'

# test = bytearray(f"{key}609043", "utf-8")

# print(md5(test).hexdigest())

def advent_coin_mine(key: str, num: int):
    return md5(bytearray(f"{key}{num}", "utf-8")).hexdigest()


key = my_key

def run(key, zeroes):
    for i in count(1):
        hash = advent_coin_mine(key, i)
        if hash.startswith(zeroes):
            print(f"{i}: {hash}")
            break


# part 1
run(key, '00000')

# part 2
run(key, '000000')