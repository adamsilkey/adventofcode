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

test_data = [line.split() for line in test_data]

part_two_test_data = """
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
""".strip().split("\n")

part_two_test_data = [line.split() for line in part_two_test_data]


DATASET = day7


def generate_bag_rules(raw_data):
    bag_rules = {}
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

        bag_rules[bag] = contents

    return bag_rules


def get_bag_contents(bag_rules: dict, outer_bag: str, contents=None, factor=1):
    if contents is None:
        contents = {}

    for bag in bag_rules[outer_bag]:
        qty = bag_rules[outer_bag][bag]
        if bag not in contents:
            contents[bag] = 0
        contents[bag] += qty * factor

        if bag_rules[bag]:
            get_bag_contents(bag_rules, bag, contents, qty * factor)

    return contents


def solve(dataset):
    bag_rules = generate_bag_rules(dataset)
    bags = {bag: get_bag_contents(bag_rules, bag) for bag in bag_rules}

    shinygold = 0
    for contents in bags.values():
        if "shinygold" in contents:
            shinygold += 1

    print(f"part one: {shinygold}")
    print(f"part two: {sum(bags['shinygold'].values())}")


if __name__ == "__main__":
    solve(DATASET)
