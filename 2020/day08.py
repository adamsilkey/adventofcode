#! /usr/bin/env python3

from collections import namedtuple
from typing import List

print("day 8")

with open("input/2020-08.in") as f:
    day8 = [line.strip() for line in f]

Instruction = namedtuple('Instruction', 'line ins value')


def generate_instructions(data):
    instructions = []
    for idx, line in enumerate(data):
        move, value = line.split()
        if value.startswith("+"):
            value = value[1:]
        value = int(value)
        instructions.append(Instruction(idx, move, value))

    return instructions


def runner(instructions: List[Instruction]):
    acc = 0
    line = 0
    seen = {}
    while True:
        # Have we run out of instructions? If so, we break
        if line >= len(instructions):
            valid = True
            break

        # Get instruction based on our current line number
        ins = instructions[line]

        # Have we seen this instruction before? If so, we break
        if ins not in seen:
            seen[ins] = 1
        else:
            valid = False
            break

        # Handle instructions
        if ins.ins == "nop":
            line += 1
        elif ins.ins == "jmp":
            line += ins.value
        elif ins.ins == "acc":
            acc += ins.value
            line += 1
        else:
            raise ValueError(f"Invalid instruction in set {ins.ins}")

    Result = namedtuple("Result", "acc valid")

    return Result(acc, valid)


def part_two(instructions: List[Instruction]):
    for ins in instructions:
        tmp_instructions = instructions[:]
        if ins.ins == "nop":
            tmp = Instruction(ins.line, "jmp", ins.value)
        elif ins.ins == "jmp":
            tmp = Instruction(ins.line, "nop", ins.value)
        elif ins.ins == "acc":
            continue
        tmp_instructions[ins.line] = tmp

        acc, valid = runner(tmp_instructions)
        if valid is True:
            return acc


day8 = generate_instructions(day8)
print(f"part one: {runner(day8).acc}")
print(f"part two: {part_two(day8)}")


part_one_test = """
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
""".strip().split("\n")

part_two_test = """
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
nop -4
acc +6
""".strip().split("\n")
test1 = generate_instructions(part_one_test)
test2 = generate_instructions(part_two_test)

