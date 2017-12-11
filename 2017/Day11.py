import sys

from collections import defaultdict, namedtuple

def parse_input(inp):
    with open(inp) as f:
        return f.readline().strip()

Hex = namedtuple('Hex', ['x', 'y', 'z'])

class HexGrid:
    def __init__(self, instructions, x = 0, y = 0, z = 0):
        self.instructions = [instruction for instruction in instructions.split(',')]
        self.grid = defaultdict(int)
        self.grid[Hex(x,y,z)] += 1
        self.pos = Hex(x,y,z)
        self._max = {'x': self.pos.x, 
                     'y': self.pos.y,
                     'z': self.pos.z}

    dirs = {'nw': Hex(-1,  1,  0),
            'n':  Hex( 0,  1, -1),
            'ne': Hex( 1,  0, -1),
            'sw': Hex(-1,  0,  1),
            's':  Hex( 0, -1,  1),
            'se': Hex( 1, -1,  0)}

    def generate_grid(self):
        for ins in self.instructions:
            new_pos = Hex(self.pos.x + self.__class__.dirs[ins].x,
                          self.pos.y + self.__class__.dirs[ins].y,
                          self.pos.z + self.__class__.dirs[ins].z)
            self.grid[new_pos] += 1
            self.pos = new_pos
            if abs(self.pos.x) > self._max['x']:
                self._max['x'] = abs(self.pos.x)
            if abs(self.pos.y) > self._max['y']:
                self._max['y'] = abs(self.pos.y)
            if abs(self.pos.z) > self._max['z']:
                self._max['z'] = abs(self.pos.z)
            print(self.pos, self.grid[self.pos])

    @property
    def timmydistance(self):
        return max(abs(self.pos.x), abs(self.pos.y), abs(self.pos.z))

    @property
    def max(self):
        return max(self._max.values())

def solve(inp):
    h = HexGrid(inp, 0, 0, 0)
    h.generate_grid()
    print(h.timmydistance)
    print(h.max)
    print()
    return inp

solve('ne,ne,ne')           #3 steps
solve('ne,ne,sw,sw')        #0 steps - back to where you started
solve('ne,ne,s,s')          #2 steps - se, se
solve('se,sw,se,sw,sw')     #3 steps - s, s, sw

solve(parse_input('input.txt'))
