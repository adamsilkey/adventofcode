with open('input.txt') as f:
    lines = f.readlines()

lis = []

for line in lines:
    lis.append(int(line))

def jump(lis):
    i = 0
    total = 0
    while i < len(lis):
        total +=1
        jump = lis[i]
        lis[i] += 1
        i += jump

    return lis, total

def jump_two(lis):
    i = 0
    total = 0
    while i < len(lis):
        total +=1
        jump = lis[i]
        if lis[i] > 2:
            lis[i] -= 1
        else:
            lis[i] +=1
        i += jump

    return lis, total

print(jump_two([0,3,0,1,-3]))
print(jump_two(lis))
