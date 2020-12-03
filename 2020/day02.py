#! /usr/bin/env python3

print("day 2")

with open("input/2020-02.in") as f:
    passwords = [line.strip() for line in f]

part_one = 0
part_two = 0

for group in passwords:
    count, letter, password = group.split()
    letter = letter[:1]
    low, high = count.split("-")
    #print(low, high, letter[:1], password)

    low = int(low)
    high = int(high)

    count = password.count(letter)
    if count >= low and count <= high:
        part_one += 1

    low -= 1
    high -= 1

    try:    
        if password[low] == letter and password[high] != letter:
            part_two += 1
            #print(password, low, high, letter)
        elif password[low] != letter and password[high] == letter:
            part_two += 1
            #print(password, low, high, letter)
        else:
            #print(password, low, high, letter)
            pass
    except IndexError:
        pass


print(part_one)
print(part_two)

