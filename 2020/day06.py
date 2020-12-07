#! /usr/bin/env python3

print("day 6")

with open("input/2020-06.in") as f:
    day6 = [line.strip() for line in f]

i = 0
questions = []
for q in day6:
    if i == len(questions):
        questions.append([])
    if q.strip() == "":
        i += 1
        continue
    questions[i].append(q)

# part one
part_one = 0
for group in questions:
    answers = list(set("".join(group)))
    part_one += len(answers)

print(f"part one: {part_one}")


pos_ans = "abcdefghijklmnopqrstuvwxyz"
part_two = 0
for group in questions:
    target = len(group)
    answers = list("".join(group))
    answers.sort()
    answers = "".join(answers)
    for c in pos_ans:
        if c * target in answers:
            part_two += 1

print(f"part_two: {part_two}")
