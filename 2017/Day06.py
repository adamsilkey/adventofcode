with open('input.txt') as f:
    inp = f.readline()
    inp = inp.split()

inp = [int(item) for item in inp]
import sys

test = [0,2,7,0]

#print(max(test))

def day_06(inp):
    loop = 0
    unique = []
    memory = [item for item in inp]
    while True:
        print(f'memory: {memory}')
        #print(f'unique: {unique}')
        if memory in unique:
            print('memory is in unique!')
            for item in unique:
                print(item)
            print(len(unique))
            print(loop)
            break
        loop +=1
        temp_memory = [item for item in memory]
        unique.append(temp_memory)

        value = max(memory)
        index = 0
        for val in memory:
            if memory[index] == value:
                break
            else:
                index += 1

        memory[index] = 0
        pos = index + 1
        while value > 0:
            try:
                memory[pos] += 1
                value -= 1
                pos +=1
            except IndexError:
                pos = 0

    print(f'broken memory: {memory}')
    broke = [item for item in memory]

    return loop

assert(day_06([0,2,7,0])) == 5

day_06(inp)
print(str(day_06(inp)))
