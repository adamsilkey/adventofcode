def generate_wire_coordinates(wire_list):
    pass


class Wire:
    def __init__(self, wire_string):
        self.wire_string = wire_string
        self.instructions = self.generate_instructions(self.wire_string)

    def generate_instructions(self, wire_string):
        return [(instruction[0:1], int(instruction[1:]))
                for instruction in
                wire_string.split(',')]


my_wire = Wire('R8,U5,L5,D3')

my_wire_2 = Wire('R88888,U12345,L3,D200000000')

print(my_wire.instructions)
print(my_wire_2.instructions)
