#! python3

frequency = 0

with open("Day01Input.txt") as f:
    for line in f:
        frequency += int(line.strip())

print(f"Frequency is {frequency}")

print("Part 2")
frequency = 0
seen_frequencies = set()
repeated = False

with open("Day01Input.txt") as f:
    frequency_input = [int(line.strip()) for line in f]

while repeated is False:
    for i in frequency_input:
        frequency += i
        if frequency not in seen_frequencies:
            seen_frequencies.add(frequency)
        else:
            print(f"Repeated frequency: {frequency}")
            repeated = True
            break


