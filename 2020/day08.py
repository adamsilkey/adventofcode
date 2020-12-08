#! /usr/bin/env python3

print("day 8")

with open("input/2020-08.in") as f:
    day8 = [line.strip() for line in f]

part_two_test = """
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
""".strip()

test = part_two_test.strip().split("\n")

instructions = []

for idx, line in enumerate(day8):
# for idx, line in enumerate(test):
    move, value = line.split()
    if value.startswith("+"):
        value = value[1:]
    value = int(value)
    visits = 0
    line_number = idx
    check = False
    instructions.append([move, value, visits])


def part_one():
    acc = 0
    line = 0
    while True:
        ins = instructions[line]
        ins[2] += 1
        if ins[2] == 2:
            break

        if ins[0] == "nop":
            line += 1
        elif ins[0] == "acc":
            line += 1
            acc += ins[1]
        else:       # jmp
            line += ins[1]

    print(f"part one: {acc}")


part_one()
