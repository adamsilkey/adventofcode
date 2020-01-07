from collections import deque, namedtuple



Instruction = namedtuple('Instruction', [
                                        'opcode',
                                        'parameter_1_mode',
                                        'parameter_2_mode',
                                        'parameter_3_mode',
                                        ])


class IntcodeComputer:
    def __init__(self, intcode_list=None, intcode_input=None):
        #TODO: Rename intcode_list to intcode_program
        self.intcode_list = intcode_list
        #self.intcodes = {index: val for index, val in enumerate(self.intcode_list)}
        self.intcodes = self.intcode_list[:]
        self.intcode_intput = intcode_input
        self.intcode_output = None

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
                pos += 4
            elif opcode == 2:
                self.multiply(pos)
                pos += 4
            elif opcode == 3:
                self.intcode_input(pos)
                pos += 2
            elif opcode == 4:
                self.intcode_output(pos)
                pos += 2

        return self.intcodes


        opcode = None
        parameter_1_mode = 0
        parameter_2_mode = 0
        parameter_3_mode = 0

        opcode = instruction % 100
        instruction = instruction // 100

        parameter_1_mode = instruction % 10
        instruction = instruction // 10

        parameter_2_mode = instruction % 10
        instruction = instruction // 10

        parameter_3_mode = instruction % 10
        instruction = instruction // 10

        return Instruction(
                opcode, 
                parameter_1_mode,
                parameter_2_mode,
                parameter_3_mode
                )


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


    def intcode_input(self, pos, intcodes=None):
        if intcodes is None:
            intcodes = self.intcodes


    def intcode_output(self, pos, intcodes=None):
        if intocodes is None:
            intcodes = self.intcodes





def tests():
    cpu = IntcodeComputer([1,0,0,0,99])
    print(cpu.run())

    cpu = IntcodeComputer([2,3,0,3,99])
    print(cpu.run())

    cpu = IntcodeComputer([1,9,10,3,2,3,11,0,99,30,40,50])
    print(cpu.run())

    cpu = IntcodeComputer([0])
    print(cpu.parse_instruction(12345))
    print(cpu.parse_instruction(3))
    print(cpu.parse_instruction(1003))
    print(cpu.parse_instruction(99))

    import sys; sys.exit()


tests()


def p1solver():
    intcode_program[1] = 12
    intcode_program[2] = 2

    cpu = IntcodeComputer(intcode_program)
    cpu.run()
    print(cpu.intcodes[0])


def p2solver(noun, verb):
    intcode_program[1] = noun
    intcode_program[2] = verb
    cpu = IntcodeComputer(intcode_program)
    cpu.run()
    return cpu.intcodes[0]


def p2finder(target):
    for noun in range(100):
        for verb in range(100):
            val = p2solver(noun,verb)
            print(noun, verb, val)
            if val == target:
                print("FOUND IT!!!!")
                checksum = 100 * noun + verb
                print(f"checksum: {checksum}")
                return noun, verb, val, checksum


target = 19690720
print(p2finder(target))
with open("Day05Input.txt") as f:
    intcode_program = list(map(int, f.readline().strip().split(',')))
