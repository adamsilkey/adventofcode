import sys

puzzle_inp = '14,58,0,116,179,16,1,104,2,254,167,86,255,55,122,244'

puzzle_lis = [int(x) for x in range(256)]
puzzle_lengths = [int(x) for x in puzzle_inp.split(',')]

def _convert_to_ascii(string):
    return [ord(char) for char in string]

assert(_convert_to_ascii('1,2,3') == [49,44,50,44,51])

def sequence(string):
    return _convert_to_ascii(string) + [17,31,73,47,23]

assert(sequence('1,2,3') == [49,44,50,44,51,17,31,73,47,23])

def sparse_hash(lengths, rounds = 64):
    pos = 0
    skip_size = 0
    lis = [x for x in range(256)]
    lis_length = len(lis)
    for _ in range(rounds):
        for length in lengths:
            #original list
            #fast forward
            for i in range(pos):
                val = lis.pop(0)
                lis.append(val)
            #reverse
            sublist = lis[:length]
            sublist.reverse()
            #return new list
            lis = sublist + lis[length:]
            #return list to original state
            for i in range(pos):
                val = lis.pop()
                lis.insert(0, val)
            #position increase
            pos += skip_size + length
            pos = pos % lis_length
            #skip size increase
            skip_size += 1
            #print(lis)

    return lis

def dense_hash(sparse_hash):
    dense = []
    sparse_hash.reverse()
    while sparse_hash:
        xor = sparse_hash.pop()
        for i in range(15):
            xor = xor ^ sparse_hash.pop()
        dense.append(xor)

    return dense

assert(dense_hash([65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]) == [64])

def make_hex(dense_hash):
    hex_string = ''
    for i in dense_hash:
        _, hex_val = hex(i).split('x')
        if len(hex_val) == 1:
            hex_val = '0' + hex_val
        hex_string += hex_val

    return hex_string

assert(make_hex([64, 7, 255]) == '4007ff')

def knot_hash(string):
    hash_ = make_hex(dense_hash(sparse_hash(sequence(string))))

    return hash_

assert(knot_hash('') == 'a2582a3a0e66e6e86e3812dcb672a272')

assert(knot_hash('AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd')

print(knot_hash(puzzle_inp))

print(knot_hash('Michael Wenzinger is a DOO DOO HEAD!1!!11'))

#assert(knot_hash([0,1,2,3,4], [3,4,1,5]) == 12)

