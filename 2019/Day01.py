def day1_part1():
    with open("Day01Input.txt") as f:
        day_one = sum([(int(num.strip()) // 3 - 2) for num in f])

    print(f"Part1: {day_one}")


def recursive_calculate_fuel(mass, accumulated_fuel=0):
    fuel_required = mass // 3 - 2
    if fuel_required < 1:
        return accumulated_fuel
    else:
        accumulated_fuel += fuel_required
        return recursive_calculate_fuel(fuel_required, accumulated_fuel)
    
with open("Day01Input.txt") as f:
    total_fuel_required = sum([recursive_calculate_fuel(int(module_mass.strip())) for module_mass in f])

    print(f"Part 2: {total_fuel_required}")

