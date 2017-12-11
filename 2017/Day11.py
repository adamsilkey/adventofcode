import sys
from collections import namedtuple

def parse_input(inp):
    with open(inp) as f:
        return f.readline().strip()




class Hex:
    def __init__(self, x, y, z):
        self.pos = (x, y, z)
        self.x = x
        self.y = y
        self.z = z
        self.nw = (x - 1, y + 1, z + 0)
        self.n = (x - 0, y + 1, z - 1)
        self.ne = (x + 1, y + 0, z - 1)
        self.sw = (x - 1, y + 0, z + 1)
        self.s = (x - 0, y - 1, z + 1)
        self.se = (x + 1, y - 1, z + 0)

hex_dirs = {'nw': (-1,  1,  0),
            'n':  ( 0,  1, -1),
            'ne': ( 1,  0, -1),
            'sw': (-1,  0,  1),
            's':  ( 0, -1,  1),
            'se': ( 1, -1,  0)}


class HexGrid:
    def __init__(self, instructions, x = 0, y = 0, z = 0):
        self.instructions = [instruction for instruction in instructions.split(',')]
        self.grid = {(x,y,z): Hex(x,y,z)}
        self.pos = (x,y,z)

    def generate_grid(self):
        for ins in self.instructions:
            new_pos = (self.pos[0] + hex_dirs[ins][0],
                       self.pos[1] + hex_dirs[ins][1],
                       self.pos[2] + hex_dirs[ins][2])
            print(new_pos)
            if new_pos not in self.grid:
                self.grid[new_pos] = Hex(new_pos[0], new_pos[1], new_pos[2])
            self.pos = new_pos

    def p(self):
        for instruction in self.instructions:
            print(instruction)
        for key, val in self.grid:
            print(key, val)

def solve(inp):
    h = HexGrid(inp, 0, 0, 0)
    h.generate_grid()
    print()
    return inp

solve('ne,ne,ne')           #3 steps
solve('ne,ne,sw,sw')        #0 steps - back to where you started
solve('ne,ne,s,s')          #2 steps - se, se
solve('se,sw,se,sw,sw')     #3 steps - s, s, sw


solve(parse_input('input.txt'))



