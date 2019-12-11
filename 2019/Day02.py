from collections import deque

with open("Day02Input.txt") as f:
    intcode_program = list(map(int, f.readline().strip().split(',')))


class IntcodeComputer:
    def __init__(self, intcode_list=None):
        self.intcode_list = intcode_list
        #self.intcodes = {index: val for index, val in enumerate(self.intcode_list)}
        self.intcodes = self.intcode_list[:]

    def run(self, intcodes=None):
        if intcodes is None:
            intcodes = self.intcodes
        halt = False
        pos = 0
        while not halt:
            opcode = intcodes[pos]
            if opcode == 99:
                halt = True
            elif opcode == 1:
                self.add(pos)
            elif opcode == 2:
                self.multiply(pos)
            #Intcode instructions are stored in sets of 4
            pos += 4
        #print("Execution finished")
        #print(self.intcodes)
        return self.intcodes

    def add(self, pos, intcodes=None):
        if intcodes is None:
            intcodes = self.intcodes
        a_position = intcodes[pos+1]
        b_position = intcodes[pos+2]
        result_position = intcodes[pos+3]
        intcodes[result_position] = intcodes[a_position] + intcodes[b_position]

    def multiply(self, pos, intcodes=None):
        if intcodes is None:
            intcodes = self.intcodes
        a_position = intcodes[pos+1]
        b_position = intcodes[pos+2]
        result_position = intcodes[pos+3]
        intcodes[result_position] = intcodes[a_position] * intcodes[b_position]


def tests():
    cpu = IntcodeComputer([1,0,0,0,99])
    print(cpu.run())

    cpu = IntcodeComputer([2,3,0,3,99])
    print(cpu.run())

    cpu = IntcodeComputer([1,9,10,3,2,3,11,0,99,30,40,50])
    print(cpu.run())

    import sys; sys.exit()


def daytwo_partone():
    intcode_program[1] = 12
    intcode_program[2] = 2

    cpu = IntcodeComputer(intcode_program)
    cpu.run()
    print(cpu.intcodes[0])

daytwo_partone()

