def part_one():
    checksum = 0
    with open('input.txt', 'r') as f:
        for line in f:
            checksum_line = list(map(int, line.split()))
            checksum_line.sort()
            print(checksum_line)
            result = (int(checksum_line[-1]) - int(checksum_line[0]))
            print(result)
            checksum += result

    print(checksum)

def find_divisor(checksum_line):
    checksum_line_copy = checksum_line[:]

checksum = 0
with open('input.txt', 'r') as f:
    for line in f:
        found_divisor = False
        checksum_line = list(map(int, line.split()))
        checksum_line.sort()
        while not found_divisor:
            checksum_line_copy = checksum_line[:]
            checksum_line_copy.pop()
            for j in checksum_line_copy:
                if checksum_line[-1] % j == 0:
                    print('FOUND IT!')
                    print(checksum_line[-1], j)
                    result = checksum_line[-1] // j
                    print(result)
                    checksum += result
                    found_divisor = True
                    break
            else:
                checksum_line_copy.pop(0)
            checksum_line.pop()

print(checksum)


