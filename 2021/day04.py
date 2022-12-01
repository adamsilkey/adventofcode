#! /usr/bin/env python3.10

TEST = False

import itertools as it
from collections import deque
from dataclasses import dataclass


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


class BingoBoard:
    pass


@dataclass
class BingoSpot:
    num: int
    called: bool = False


# a = BingoSpot(1)
# print(a)

# import sys;sys.exit()

def bingo_load(filename:str):

    bingo = deque(load_lines(filename))
    bingo_order = [int(i) for i in bingo[0].split(",")]

    bingo.popleft()

    bingo_cards = []

    while bingo:
        card = []
        for i in range(6):
            if i == 0:
                bingo.popleft()
            else:
                card.append([BingoSpot(int(i)) for i in bingo.popleft().split()])
            
        bingo_cards.append(card)

    
    return(bingo_order, bingo_cards)


def call_number(num, card):
    for row in card:
        for spot in row:
            if spot.num == num:
                spot.called = True
                return
    else:
        pass
        # JK, there can be missin numbers from a bingo board
        # raise("Something broke with the card here")



def pprint_card(card):
    print("===============================")
    for row in card:
        for spot in row:
            print(spot, end=' ')
        print()
    print("===============================")


def print_all_cards(cards):
    for card in cards:
        pprint_card(card)
        print('\n')
        print('\n')


def check_for_victory(card):

    # Check Horizontals
    for row in card:
        for spot in row:
            if spot.called == False:
                break
        else: # no break for this row
            print("FOUND A HORIZONTAL VICTOR!!!")
            return True
    
    # Check verticals
    for col in range(5):
        for row in range(5):
            if card[row][col].called == False:
                break
        else: # no break for this column
            print("FOUND A VERTICAL VICTOR!!")
            return True
        
    
    return False


def sum_unmarked_numbers(card):
    sum_ = 0
    for row in card:
        for spot in row:
            if spot.called == False:
                sum_ += spot.num

    return sum_


def round(num, cards):
    # assign number to card
    for card in cards:
        call_number(num, card)

    # check for victory
    for card in cards:
        if check_for_victory(card):
            print(card)
            print(sum_unmarked_numbers(card))
            return sum_unmarked_numbers(card)



def let_the_squid_win(num, cards):
    last_sum = False
    for card in cards:
        call_number(num, card)
    
    for idx, card in enumerate(cards):
        if check_for_victory(card):
            print(card)
            print(sum_unmarked_numbers(card))
            last_sum = sum_unmarked_numbers(card)
            cards.pop(idx)
    
    return last_sum



if TEST:
    puzzle_input = bingo_load("04.test")
    # puzzle_input = bingo_load("04_vertical.test")
else:
    puzzle_input = bingo_load("04.in")


order, cards = puzzle_input

# # Part 1
# for num in order:
#     if sum_ := round(num, cards):
#         print(num, sum_)
#         print(num * sum_)
#         break

# print()
# print()
# print()
# print()

# Part 2

total_cards = len(cards)
print(total_cards)

wins = 0

cards_that_won = []

for num in order:
    if sum_ := let_the_squid_win(num, cards):
        print(num, sum_)
        print(num * sum_)
        # wins += 1
        print(f"{wins=}")

# print_all_cards(cards)
# print(len(cards))
# print(total_cards)
