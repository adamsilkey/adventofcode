#! /usr/bin/env python3

def part_one(year):
    for idx, num in enumerate(nums):
        for num2 in nums[idx+1:]:
            if year == num + num2:
                print(num, num2)
                print(num * num2)
                return


def part_two(year):
    for idx, num in enumerate(nums):
        for num2 in nums[idx+1:]:
            for num3 in nums[idx+2:]:
                if year == num + num2 + num3:
                    print(num, num2, num3)
                    print(num * num2 * num3)
                    return


if __name__ == "__main__":

    with open("input/2020-01.in") as f:
        nums = [int(line.strip()) for line in f]

    part_one(2020)
    part_two(2020)
