#! /usr/bin/env python3.10
# Advent of Code 2015 - Day 02
#
# formula - 2*l*w + 2*w*h + 2*h*l

# Part 1

from collections import namedtuple

Box = namedtuple('Box', ['l', 'w', 'h'])

with open('input/02.in') as f:
    boxes = []
    for line in f.readlines():
        l, w, h = line.strip().split('x')
        boxes.append(Box(int(l), int(w), int(h)))

wrapping_paper = 0

for box in boxes:
    paper_needed = (box.l * box.w, box.l * box.h, box.w * box.h)
    wrapping_paper += sum(paper_needed) * 2 + min(paper_needed)

print(print(f"Part 1: {wrapping_paper}")