#! /usr/bin/env python3

print("day 7")

with open("input/2020-07.in") as f:
    day7 = [line.strip().split() for line in f]

test_data = """
dumb blue bags contain 4 dumb green bags, 1 dumb red bag
dumb red bags contain 1 dotted black bag, 1 slime blue bag
dumb green bags contain 4 dotted black bags
slime blue bags contain 1 light red bag
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
""".strip().split("\n")

part_two_test_data = """
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
""".strip().split("\n")

test_data = [line.split() for line in test_data]
part_two_test_data = [line.split() for line in part_two_test_data]


def generate_bag_rules(raw_data):
    bag_types = {}
    for rule in raw_data:
        bag = "".join(rule[0:2])
        contents = {}
        rule = rule[4:]
        if len(rule) % 4 == 0:
            for _ in range(len(rule) // 4):
                name = "".join(rule[1:3])
                qty = int(rule[0])
                contents[name] = qty
                rule = rule[4:]

        bag_types[bag] = contents

    return bag_types


# bags = generate_bag_rules(test_data)

# bags = generate_bag_rules(part_two_test_data)
#
bags = generate_bag_rules(day7)


def get_bag_contents(bag_list: dict, outer_bag: str, contents: dict, factor=1):
    for bag in bag_list[outer_bag]:
        qty = bag_list[outer_bag][bag]
        if bag not in contents:
            contents[bag] = 0
        contents[bag] += qty * factor

        if bag_list[bag]:
            get_bag_contents(bag_list, bag, contents, qty * factor)


        # if bag_list[bag]:
        #     for _ in range(bag_list[outer_bag][bag]):
        #         get_bag_contents(bag_list, bag, contents)

    return contents


all_bags = []

for bag in bags:
    bag_contents = {}
    # print(bag, get_bag_contents(bags, bag, bag_contents))
    all_bags.append(get_bag_contents(bags, bag, bag_contents))


shinygold = 0
for bag in all_bags:
    if "shinygold" in bag:
        shinygold += 1

print(f"part one: {shinygold}")

shiny_contents = get_bag_contents(bags, "shinygold", {})

sum = 0
for q in shiny_contents.values():
    sum += q


print(f"part two: {sum}")


'''
"""def part_one(bag: str, bag_list: dict, bag_target: str):
    print(f"Checking {bag}")
    print(f"Searching through {bag_list[bag]}")
    for b in bag_list[bag]:
        print(f"  - checking {b}")
        if b == bag_target:
            print("found our target!")
            return True
        elif not bag_list[b]:
            print("found an empty bag")
            continue
        else:
            return part_one(b, bag_list, bag_target)
    print("End of the line")
    print()
    # return False
"""


def get_bag_contents(bag: str, bag_list: dict, contents=None):
    if contents is None:
        contents = set()
    for sub_bag in bag_list[bag]:
        contents.add(sub_bag)
        if bag_list[sub_bag]:
            get_bag_contents(sub_bag, bag_list, contents)

    return contents


def part_one(bag_list, target):
    target_count = 0
    for i, bag in enumerate(bag_list):
        if target in get_bag_contents(bag, bag_list):
            target_count += 1
        print(f"Processed {i + 1} / {len(bag_list)} bags.")

    return target_count




def test():
    test_data = """
    dumb red bags contain 1 dotted black bag, 1 slime blue bag
    slime blue bags contain 1 light red bag
    light red bags contain 1 bright white bag, 2 muted yellow bags.
    dark orange bags contain 3 bright white bags, 4 muted yellow bags.
    bright white bags contain 1 shiny gold bag.
    muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
    shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
    dark olive bags contain 3 faded blue bags, 4 dotted black bags.
    vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
    faded blue bags contain no other bags.
    dotted black bags contain no other bags.
    """.strip().split("\n")

    test_data = [line.split() for line in test_data]

    bags = generate_bag_rules(test_data)
    print(f"part_one {part_one(bags, 'shinygold')}")




def main():
    bags = generate_bag_rules(day7)

    print(f"part_one {part_one(bags, 'shinygold')}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("specifcy debug or prod")
        sys.exit()
    debug = sys.argv[1]
    if debug == "debug":
        test()
    else:
        main()
        '''