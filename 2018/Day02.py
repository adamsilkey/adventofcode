#! python3

from collections import Counter

with open("Day02Input.txt") as f:
    box_ids = [id_.strip() for id_ in f]

two_checksum = 0
three_checksum = 0

for id_ in box_ids:
    c = Counter(id_)
    if 2 in c.values():
        two_checksum += 1
    if 3 in c.values():
        three_checksum += 1

print(f"Checksum is {two_checksum * three_checksum}")
