import sys

from collections import deque

with open('input.txt') as f:
    inp = deque()
    for line in f:
        inp.append(deque(line.split()))

with open('test_input.txt') as f:
    test_inp = deque()
    for line in f:
        test_inp.append(deque(line.split()))

class Instruction:
    def __init__(self, line):
        self.register = line.popleft()
        self.modify = line.popleft()
        self.amount = int(line.popleft())
        line.popleft()
        self.condition = line

    def print(self):
        print(f"register: {self.register}")
        print(f"modify: {self.modify}")
        print(f"amount: {self.amount}")
        print(f"condition: {self.condition}")
        print()


def condition_check(register_value, condition, value):
    value = int(value)
    check = False
    if condition == '==':
        if register_value == value:
            check = True
    elif condition == '!=':
        if register_value != value:
            check = True
    elif condition == '<':
        if register_value < value:
            check = True
    elif condition == '>':
        if register_value > value:
            check = True
    elif condition == '<=':
        if register_value <= value:
            check = True
    elif condition == '>=':
        if register_value >= value:
            check = True
    #print(f'{register_value} {condition} {value}: {check}')
    return check

assert(condition_check(1, '>', 1) == False)

def solve(inp):
    cpu = {}
    instructions = [Instruction(line) for line in inp]
    highest_result = 0
    for instruction in instructions:
        if instruction.register not in cpu.keys():
            cpu[instruction.register] = 0
            #print(f'register {instruction.register} not found')
        new_reg = instruction.condition[0]
        if new_reg not in cpu.keys():
            cpu[new_reg] = 0
            #print(f'register {new_reg} not found')
        #print(instruction.condition)
        result = condition_check(cpu[instruction.condition[0]],
                                 instruction.condition[1],
                                 instruction.condition[2])

        if result == True:
            if instruction.modify == 'inc':
                cpu[instruction.register] += int(instruction.amount)
                #print(f'inc: {instruction.amount}')
            elif instruction.modify == 'dec':
                cpu[instruction.register] -= int(instruction.amount)
                #print(f'dec: {instruction.amount}')
            if cpu[instruction.register] > highest_result:
                highest_result = cpu[instruction.register]

    reg_values = []
    for key, val in cpu.items():
        #print(key, val)
        reg_values.append(val)

    reg_values.sort()

    print(f'max value: {highest_result}')

    #print(reg_values)
    return max(reg_values)

test_solution = 1

assert(solve(test_inp) == test_solution)


print(solve(inp))
