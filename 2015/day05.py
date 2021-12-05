#! /usr/bin/env python3.10
# Advent of Code 2015 - Day 05
#

with open('input/05.in') as f:
    santa_strings = [l.strip() for l in f.readlines()]

# print(santa_strings)


def has_three_vowels(s: str):
    VOWELS = 'aeiou'
    count = 0
    for c in s:
        if c in VOWELS:
            count += 1
    
    return count > 2


def has_double_letters(s: str):

    for idx, c in enumerate(s[:-1]):
        if c == s[idx+1]:
            return True
    else: #no break
        return False


def no_naughty_substrings(s: str):
    NAUGHTY = ('ab', 'cd', 'pq', 'xy')

    if any(bad in s for bad in NAUGHTY):
        return False
    else:
        return True


def naughty_or_nice(s: str):

    return has_three_vowels(s) and has_double_letters(s) and no_naughty_substrings(s)


def test_part1():
    test_cases = [
        'ugknbfddgicrmopn',
        'aaa',
        'jchzalrnumimnmhp',
        'haegwjzuvuyypxyu',
        'dvszwmarrgswjxmb',
    ]

    for test in test_cases:
        print(naughty_or_nice(test))


count = 0
for s in santa_strings:
    if naughty_or_nice(s):
        count += 1

print(f"Part 1: {count}")


# Part 2

def has_letter_sandwich(s: str):
    for idx, c in enumerate(s[:-2]):
        if c == s[idx+2]:
            return True
    else:   # no break
        return False


def has_two_letter_pair(s: str):
    while len(s) > 3:
        sub = s[0:2]
        if sub in s[2:]:
            return True
        else:
            s = s[1:]
    
    return False


def santas_second_try(s: str):
    return has_letter_sandwich(s) and has_two_letter_pair(s)


def test_part2():
    test_cases = [
        'qjhvhtzxzqqjkmpb',
        'xxyxx',
        'uurcxstgmygtbstg',
        'ieodomkazucvgmuy',
    ]

    for test in test_cases:
        print(santas_second_try(test))


count = 0
for s in santa_strings:
    if santas_second_try(s):
        count += 1

print(f"Part 2: {count}")
