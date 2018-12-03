#! python3

frequency = 0

with open("Day01Input.txt") as f:
    for line in f:
        frequency += int(line.strip())

print(f"Frequency is {frequency}")


