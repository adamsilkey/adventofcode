with open("Day01Input.txt") as f:
    day_one = sum([(int(num.strip()) // 3 - 2) for num in f])

print(day_one)
