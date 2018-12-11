#! python3

from collections import Counter, deque

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

print(f"Part 1: Checksum is {two_checksum * three_checksum}")
# Correct answer is 4980

print("Part 2")

for first_id in box_ids:
    for second_id in box_ids:
        if first_id == second_id:
            pass
        else:
            differences = 0
            common_characters = []
            dfirst_id = deque(first_id)
            dsecond_id = deque(second_id)
            while dfirst_id and differences < 2:
                a = dfirst_id.popleft()
                if a != dsecond_id.popleft():
                    differences += 1
                else:
                    common_characters.append(a)
            if differences == 1:
                print(f"IDs found: {first_id}, {second_id}")
                print(f"Common characters: {''.join(common_characters)}")
            else:
                pass
                #print(f"{first_id} and {second_id}")
