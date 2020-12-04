#! /usr/bin/env python3

print("day 4")

with open("input/2020-04.in") as f:
    day4 = [line.strip() for line in f]

passports = []

keys = ["byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
        ]

i = 0

for line in day4:
    if i == len(passports):
        passports.append({})

    if line.strip() == "":
        i += 1
        continue

    line = line.split()
    for pair in line:
        k, v = pair.split(":")
        passports[i][k] = v


def main():
    invalid = 0
    valid = 0
    for passport in passports:
        # part one
        for key in keys:
            if key not in passport.keys():
                invalid += 1
                break
        else:
            # part two
            if valid_passport(passport):
                valid += 1

    print(f"part one: {len(passports) - invalid}")
    print(f"part two: {valid}")


def valid_passport(passport):

    # for k, v in passport.items():
    #     print(f"{k} -> {v}")


    if not year_check(passport, "byr", 1920, 2002):
        # print("invalid\n")
        return False
    if not year_check(passport, "iyr", 2010, 2020):
        # print("invalid\n")
        return False
    if not year_check(passport, "eyr", 2020, 2030):
        # print("invalid\n")
        return False

    if hgt(passport) and hcl(passport) and ecl(passport) and pid(passport):
        # print("Valid!!\n")
        return True
    else:
        # print("invalid\n")
        return False



def year_check(passport, key, lo, hi):
    byr = int(passport[key])
    if lo <= byr <= hi:
        return True
    return False


def hgt(passport):
    try:
        hgt_type = passport["hgt"][-2:]
        height = int(passport["hgt"][:-2])
        if hgt_type == "cm":
            if 150 <= height <= 193:
                return True
        elif hgt_type == "in":
            if 59 <= height <= 76:
                return True
    except ValueError:
        pass

    return False


def hcl(passport):
    hcl = passport["hcl"]
    if len(hcl) != 7:
        return False
    if hcl[0] != "#":
        return False
    for c in hcl[1:]:
        if c not in "0123456789abcdef":
            return False

    return True


def ecl(passport):

    if passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return True
    else:
        return False


def pid(passport):
    pid = passport["pid"]
    if len(pid) == 9 and pid.isnumeric():
        return True
    return False


main()
