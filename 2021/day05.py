#! /usr/bin/env python3.10

TEST = False

import re

class Line:
    pattern = re.compile(r"(\d*),(\d*) -> (\d*),(\d*)")

    def __init__(self, x1, y1, x2, y2):
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.x2 = int(x2)
        self.y2 = int(y2)

    @classmethod
    def from_string(cls, s: str):
        match = cls.pattern.match(s.strip())
        x1 = match.group(1)
        y1 = match.group(2)
        x2 = match.group(3)
        y2 = match.group(4)

        return cls(x1, y1, x2, y2)


class VentMap:
    DIMENSION = 1000
    def __init__(self):
        self.vents = []
        self.lines = []

    def make_line(self, line: Line, allow_diagonal):
        line_length = abs(line.x1 - line.x2) or abs(line.y1 - line.y2)
        is_diagonal = False if (line.x1 == line.x2 or line.y1 == line.y2) else True
        dx = 1 if line.x1 < line.x2 else -1 if line.x1 > line.x2 else 0
        dy = 1 if line.y1 < line.y2 else -1 if line.y1 > line.y2 else 0

        if not allow_diagonal and is_diagonal:
            return
        
        for i in range(line_length + 1):
            self.vents[line.y1 + (i * dy)][line.x1 + (i * dx)] += 1

    def load(self, filename: str):
        with open(filename) as f:
            self.lines = [Line.from_string(line.strip()) for line in f.readlines()]
    
    def run(self, allow_diagonal=False):

        self.vents = [[0 for _ in range(self.DIMENSION)] for i in range(self.DIMENSION)]
        
        for line in self.lines:
            self.make_line(line, allow_diagonal=allow_diagonal)

        return self.total

    @property
    def total(self):
        total = 0
        for row in self.vents:
            for vent in row:
                if vent > 1:
                    total += 1
        
        return total


vents = VentMap()
vents.load("05.in")
print(f"Part 1: {vents.run()}")
print(f"Part 2: {vents.run(allow_diagonal=True)}")