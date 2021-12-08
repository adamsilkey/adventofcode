#! /usr/bin/env python3.10

YEAR = '2021'
AOC_DAY = '08'

import itertools as it
import sys
from collections import Counter, defaultdict, deque, namedtuple
from dataclasses import dataclass

if not (YEAR and AOC_DAY):
    print("!!! Set YEAR/AOC_DAY")
    sys.exit(1)

def fail():
    print("!!! Need to define -p for production or -t for test")
    sys.exit(1)

if len(sys.argv) != 2:
    fail()

match sys.argv[1].lower():
    case '-t':
        test = True
    case '-p':
        test = False
    case _:
        fail()

if test:
    filename = f"{AOC_DAY}.test"
else:
    filename = f"{AOC_DAY}.in"

title = f"Advent of Code {YEAR} - Day {AOC_DAY} - {'Test' if test else 'Production'}"

print(f"=" * len(title))
print(title)
print(f"=" * len(title))

def load_file(filename: str) -> str:
    """Loads an AOC file, returns a string"""

    with open(filename) as f:
        return f.read().rstrip("\n")


def load_lines(filename: str) -> list[str]:
    """Returns a list of lines"""

    return load_file(filename).split("\n")


def load_ints(filename: str) -> list[int]:
    """Returns a list of ints"""

    return [int(i) for i in load_lines(filename)]

def load_comma_separated_ints(filename: str) -> list[int]:
    """Returns a list of ints from a comma separated list of ints"""

    return [int(i) for i in load_file(filename).strip().split(",")]


# filename

# digit0 = {"a": 4, "b": 2, "c": 2, "e": 2, "f": 2, "g": 4}
# digit2 = {"a": 4, "c": 2, "d": 4, "e": 2, "g": 4}
# digit3 = {"a": 4, "c": 2, "d": 4, "e": 2, "f": 2, "g": 4}
# digit5 = {"a": 4, "b": 2, "d": 4, "f": 2, "g": 4}
# digit6 = {"a": 4, "b": 2, "d": 4, "e": 2, "f": 2, "g": 4}
# digit9 = {"a": 4, "b": 2, "c": 2, "d": 4, "f": 2, "g": 4}

# digit1 = {                "c": 2,         "f": 2}   # Len 2
# digit7 = {"a": 4,         "c": 2,         "f": 2} # Len 3
# digit4 = {        "b": 2, "c": 2, "d": 4, "f": 2} # Len 4
# digit8 = {"a": 4, "b": 2, "c": 2, "d": 4, "e": 2, "f": 2, "g": 4} # Len 7



# 10 unique signals | 4 digit output value
DisplayLine = namedtuple("DisplayLine", ["signal", "output"])

def parse_display_line(line: str):
    signal, _, output = line.partition("|")

    return DisplayLine(signal.strip().split(), output.strip().split())


#### Digit Mapping
##   1 -     c     f     - 2
##   7 - a   c     f     - 3
##   4 -   b c d   f     - 4

##   2 - a   c d e   g   - 5
##   3 - a   c d   f g   - 5
##   5 - a b   d   f g   - 5

##   0 - a b c   e f g   - 6
##   6 - a b   d e f g   - 6
##   9 - a b c d   f g   - 6

##   8 - a b c d e f g   - 8

def decode(line: DisplayLine):

    mixed_up = [signal for signal in line.signal]
    decode = {}
    # charmap = {}  # Encoded ---> Decoded
    charmap = {}  # Decoded ---> Encoded

    # Find 1,4,7,8
        # 1 - 2
        # 4 - 4
        # 7 - 3
        # 8 - 7
    for signal in mixed_up:
        match len(signal):
            case 2:
                decode[1] = signal
            case 4:
                decode[4] = signal
            case 3:
                decode[7] = signal
            case 7:
                decode[8] = signal

    # ====== FIND A
    # Whatever is in 7 that isn't in 4 is a
    for c in decode[7]:
        if c not in decode[4]:
            charmap['a'] = c

    # ====== FIND D and G
    two_three_five = [set(signal) for signal in mixed_up if len(signal) == 5]
    ## Find the intersection of all the fives
    potentials = two_three_five[0].intersection(two_three_five[1], two_three_five[2])
    ## Remove 'a' - we are left with two potentials for d and g
    potentials.remove(charmap['a'])
    ## Which potential is found in 4? That is d
    for c in potentials:
        if c in decode[4]:
            charmap['d'] = c
    ## What remains must be 'g'
    potentials.remove(charmap['d'])
    ## Pop the last remaining item
    charmap['g'] = potentials.pop()


    # ===== FIND B
    ## find difference between 1 and 4
    one = set(decode[1])
    four = set(decode[4])
    potentials = four.difference(one)
    ## Remove D
    potentials.remove(charmap['d'])
    ## What remains must be B
    charmap['b'] = potentials.pop()

    # ===== FIND F
    ## Look at 5
    two_three_five = [signal for signal in mixed_up if len(signal) == 5]
    found = set([v for v in charmap.values()])

    for potential in two_three_five:
        if len(set(potential).difference(found)) == 1:
            # we've found f and 5
            charmap['f'] = set(potential).difference(found).pop()
            decode[5] = potential

    # ===== FIND C
    for c in decode[1]:
        if c not in charmap.values():
            charmap['c'] = c

    # ===== FIND E
    for c in decode[8]:
        if c not in charmap.values():
            charmap['e'] = c

    # Decode 0,2,3,6,9
    ## Remove the values we know
    remaining = [item for item in mixed_up if item not in decode.values()]

    to_be_figured_out = {
        'abcefg': 0,
        'acdeg': 2,
        'acdfg': 3,
        'abdefg': 6,
        'abcdfg': 9,
    }

    reverse_charmap = {v: k for k,v in charmap.items()}

    for encoded_signal in remaining:

        decoded = ''
        for c in encoded_signal:
            decoded += reverse_charmap[c]
        
        decoded = ''.join(sorted(decoded))
        decode[to_be_figured_out[decoded]] = encoded_signal


    # for k, v in decode.items():
    #     print(f"{k}: {v}")  

    # for k, v in charmap.items():
    #     print(f"Decoded: {k} -- Encoded: {v}")

    # We want the reverse because we care about the key in the output dictionary
    return {v: k for k, v in decode.items()}



TEST_LINE = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
test_display_line = parse_display_line(TEST_LINE)
# print(display_line)

# print(decode(display_line))


def convert_output(output, decode_dict):
    # Sort our items. There's a better place to do this but we're just trying to get the solve
    # for this first run
    decode_dict = {''.join(sorted(k)): v for k,v in decode_dict.items()}
    output = [''.join(sorted(s)) for s in output]
    result = (
        decode_dict[output[0]] * 1000 +
        decode_dict[output[1]] * 100 +
        decode_dict[output[2]] * 10 +
        decode_dict[output[3]] * 1
    )

    return result


def process_line(line: DisplayLine):

    return convert_output(line.output, decode(line))

# print(process_line(test_display_line))




def parse_input(filename):
    ll = load_lines(filename)

    displays = []

    for line in ll:
        displays.append(parse_display_line(line))

    return(displays)
    

displays = parse_input(filename)

total = sum(process_line(display) for display in displays)

print(f"p2: {total}")















def part_one(displays):
    count = 0
    for disp in displays:
        for out in disp.output:
            if len(out) in [2,3,4,7]:
                count += 1
    
    print(f"p1: {count}")

# part_one(displays)