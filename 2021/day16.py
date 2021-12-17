#! /usr/bin/env python3.10

YEAR = '2021'
AOC_DAY = '16'

import itertools as it
import math
import sys
from collections import Counter, defaultdict, deque, namedtuple
from dataclasses import dataclass
from enum import Enum

if not (YEAR and AOC_DAY):
    print("!!! Set YEAR/AOC_DAY")
    sys.exit(1)

def fail():
    print("!!! Need to define -p for production or -t for test")
    sys.exit(1)

if len(sys.argv) != 2:
    fail()

match sys.argv[1].lower():
    case '-t':
        test = True
    case '-p':
        test = False
    case _:
        fail()

if test:
    # filename = f"{AOC_DAY}.test"
    pass
else:
    filename = f"{AOC_DAY}.in"

title = f"Advent of Code {YEAR} - Day {AOC_DAY} - {'Test' if test else 'Production'}"

print(f"=" * len(title))
print(title)
print(f"=" * len(title))

def load_file(filename: str) -> str:
    """Loads an AOC file, returns a string"""

    with open(filename) as f:
        return f.read().rstrip("\n")


Packet = namedtuple("Packet", ["version", "type_id", "otype", "value", "packet_length"])
OPacket = namedtuple("OPacket", ["operator", "otype", "value", "packet_length"])
LPacket = namedtuple("LPacket", ["value", "packet_length"])


TOTAL_LENGTH = 0
SUBPACKETS = 1
PACKET_LITERAL = 4


def hex_to_bin(s: str):
    bit_length = len(s) * 4
    s = str(bin(int(s, 16)))[2:]
    s = '0' * (bit_length - len(s)) + s

    return s


def bint(s: str):
    '''binary string to int'''
    return int(s, 2)


def literal(s: str):
    _value = ''
    for i in it.count(1):
    # while True:
        part = s[0:5]
        s = s[5:]
        _value += part[1:5]
        if part[0] == '0':
            break

    packet_length = 5 * i
    
    return s, bint(_value), packet_length


def operator(s: str):
    op_type = bint(s[0])
    s = s[1:]

    if op_type == 0:         # 0
        value = bint(s[0:15])
        s = s[15:]
        packet_length = 15 + 1
    elif op_type == 1:         # 1
        value = bint(s[0:11])
        s = s[11:]
        packet_length = 11 + 1
    else:
        raise ValueError("op_type was wrong?")

    return s, value, op_type, packet_length


def decode_packet(s: str):
    # Check for 1s and 0s and convert our string from hex to bin
    if not all(c in '01' for c in s):
        s = hex_to_bin(s)

    if len(s) < 11:
        return '', Packet(None, None, None, s, len(s))

    version = bint(s[0:3])
    type_id = bint(s[3:6])

    s = s[6:]

    if type_id == PACKET_LITERAL:
        s, value, packet_length = literal(s)
        otype = None
    else:
        s, value, otype, packet_length = operator(s)

    packet_length += 6

    return s, Packet(version, type_id, otype, value, packet_length)


def decode(s: str):
    if not all(c in '01' for c in s):
        s = hex_to_bin(s)

    packets = []
    while s:
        s, packet = decode_packet(s)
        packets.append(packet)

    return packets


def print_packets(packets: list[Packet]):
    for packet in packets:
        print(packet)


def sum_version(packets):

    total = 0
    for packet in packets:
        if isinstance(packet, tuple) and packet.version is not None:
            total += packet.version
    
    return total


def test_code():
    test = decode('8A004A801A8002F478')
    print_packets(test)
    print(sum_version(test))
    print()

    test = decode('620080001611562C8802118E34')
    print_packets(test)
    print(sum_version(test))
    print()

    test = decode('C0015000016115A2E0802F182340')
    print_packets(test)
    print(sum_version(test))
    print()

    test = decode('A0016C880162017C3686B18A3D4780')
    print_packets(test)
    print(sum_version(test))
    print()


if not test:
    ll = hex_to_bin(load_file(filename))

    def part_one():
        packets = decode(ll)

        total = sum_version(packets)
        print(len(packets))

        print(f"p1: {total}")

    part_one()


def build_stack(packets: list[Packet]):

    ptypes = {
        0: '+',
        1: '*',
        2: 'min',
        3: 'max',
        5: '>',
        6: '<',
        7: '==',
    }

    packet_stack = []
    for packet in packets:
        if packet.type_id is None:
            break
        elif packet.type_id == 4:
            packet_stack.append(LPacket(packet.value, packet.packet_length))
        else:
            if packet.otype == 0:
                otype = 'length'
            elif packet.otype == 1:
                otype = 'num_subpackets'
            else:
                raise ValueError(f"unknown {packet.type_id=}")

            packet_stack.append(OPacket(ptypes[packet.type_id], otype, packet.value, packet.packet_length))

    return packet_stack


def compute(opacket: Packet, packets: list[Packet]):
    otypes = {
        0: '+',
        1: '*',
        2: 'min',
        3: 'max',
        5: '>',
        6: '<',
        7: '==',
    }

    print(otypes[opacket.type_id])
    print(opacket)
    for p in packets:
        print(p)
    print()

    match opacket.type_id:
        case 0: # sum
            value = sum(p.value for p in packets)
        case 1: # mult
            value = math.prod(p.value for p in packets)
        case 2: # min
            value = min(p.value for p in packets)
        case 3: # max
            value = max(p.value for p in packets)
        
        # for the equality packets, we compare 1 - 0 because everything is swapped
        # ... or maybe not? 
        case 5: # >
            value = 1 if packets[0].value > packets[1].value else 0
        case 6: # <
            value = 1 if packets[0].value < packets[1].value else 0
        case 7: # ==
            value = 1 if packets[0].value == packets[1].value else 0

    new_packet_length = sum(p.packet_length for p in packets)
    new_packet_length += opacket.packet_length

    return Packet(-1, 4, None, value, new_packet_length)


def run(packets: list[Packet]):

    # Get rid of a bad last packet
    if packets[-1].version is None:
        packets.pop()

    value = 0
    stack = []

    while packets:
        last = packets.pop()
        if last.type_id == 4:
            stack.append(last)

        if last.otype == SUBPACKETS:
            substack = []
            for _ in range(last.value):
                substack.append(stack.pop())

            new_packet = compute(last, substack)
            stack.append(new_packet)

        elif last.otype == TOTAL_LENGTH:
            subtotal = last.value
            substack = []
            while subtotal:
                subpacket = stack.pop()
                subtotal -= subpacket.packet_length
                substack.append(subpacket)

                if subtotal < 0:
                    raise ValueError(f"Should not be negative: {subtotal=}")
                
            new_packet = compute(last, substack)
            stack.append(new_packet)

        print(stack)
        # input()
            

if test:
    run(decode('C200B40A82'))
else:
    packets = decode(ll)
    run(packets)

if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
