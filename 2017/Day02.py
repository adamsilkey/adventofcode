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
