#! /usr/bin/env python3.10
# Advent of Code 2015 - Day 06
#

import re

class LightGrid:
    def __init__(self):
        self.grid = [[0 for _ in range(1000)] for i in range(1000)]
        self.instructions = []

    def turn_on(self, x, y, dx, dy):
        for i in range(x, dx+1):
            for j in range(y, dy+1):
                self.grid[i][j] = 1

    def toggle(self, x, y, dx, dy):
        for i in range(x, dx+1):
            for j in range(y, dy+1):
                if self.grid[i][j]:
                    self.grid[i][j] = 0
                else:
                    self.grid[i][j] = 1

    def turn_off(self, x, y, dx, dy):
        for i in range(x, dx+1):
            for j in range(y, dy+1):
                self.grid[i][j] = 0

    def run_instruction(self, inst):
        match inst[0]:
            case 'turn on':
                self.turn_on(*inst[1:])
            case 'toggle':
                self.toggle(*inst[1:])
            case 'turn off':
                self.turn_off(*inst[1:])

    @staticmethod
    def parse_instruction(s: str):
        pattern = re.compile(r'([a-z ]+) (\d+),(\d+) [a-z ]+ (\d+),(\d+)\s*')

        if res := pattern.match(s):
            return (
                res.group(1),
                int(res.group(2)),
                int(res.group(3)),
                int(res.group(4)),
                int(res.group(5)),
            )
            # return res.groups()
        else:
            raise ValueError(f"string {s} not matched")

    def load(self, filename: str):
        with open(filename) as f:
            self.instructions = [self.parse_instruction(line) for line in f.readlines()]

    def run(self):
        for inst in self.instructions:
            self.run_instruction(inst)
        
        print(f"Part 1: {self.on}")


    @property
    def on(self):
        return sum(sum(row) for row in self.grid)


def test_light_grid():
    test = LightGrid()

    test.turn_on(0,0,999,999)
    print(test.on)
    test.toggle(0,0,999,0)
    print(test.on)
    test.turn_off(499,499,500,500)
    print(test.on)


p1 = LightGrid()
p1.load('input/06.in')
p1.run()


# Part 2

class LightGrid2(LightGrid):

    def turn_on(self, x, y, dx, dy):
        for i in range(x, dx+1):
            for j in range(y, dy+1):
                self.grid[i][j] += 1

    def toggle(self, x, y, dx, dy):
        for i in range(x, dx+1):
            for j in range(y, dy+1):
                self.grid[i][j] += 2

    def turn_off(self, x, y, dx, dy):
        for i in range(x, dx+1):
            for j in range(y, dy+1):
                self.grid[i][j] -= 1
                if self.grid[i][j] < 0:
                    self.grid[i][j] = 0

p2 = LightGrid2()
p2.load('input/06.in')
p2.run()