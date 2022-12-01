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

    # print(otypes[opacket.type_id])
    # print(opacket)
    # for p in packets:
    #     print(p)
    # print()

    # print(f"{otypes[opacket.type_id]}: {[p.value for p in packets]}")

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

    return stack[0].value
            

if test:
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


        run(decode('C200B40A82'))

    print('p1')
    print(sum_version(decode('22008c513004610e80234006cc890c29600b25000d99251873e008c49890')))
    print('p2')
    print(run(decode('22008c513004610e80234006cc890c29600b25000d99251873e008c49890')))

    kiwi = '820D4100A1000085C6E8331F8401D8E106E1680021708630C50200A3BC01495B99CF6852726A88014DC9DBB30798409BBDF5A4D97F5326F050C02F9D2A971D9B539E0C93323004B4012960E9A5B98600005DA7F11AFBB55D96AFFBE1E20041A64A24D80C01E9D298AF0E22A98027800BD4EE3782C91399FA92901936E0060016B82007B0143C2005280146005300F7840385380146006900A72802469007B0001961801E60053002B2400564FFCE25FEFE40266CA79128037500042626C578CE00085C718BD1F08023396BA46001BF3C870C58039587F3DE52929DFD9F07C9731CC601D803779CCC882767E668DB255D154F553C804A0A00DD40010B87D0D6378002191BE11C6A914F1007C8010F8B1122239803B04A0946630062234308D44016CCEEA449600AC9844A733D3C700627EA391EE76F9B4B5DA649480357D005E622493112292D6F1DF60665EDADD212CF8E1003C29193E4E21C9CF507B910991E5A171D50092621B279D96F572A94911C1D200FA68024596EFA517696EFA51729C9FB6C64019250034F3F69DD165A8E33F7F919802FE009880331F215C4A1007A20C668712B685900804ABC00D50401C89715A3B00021516E164409CE39380272B0E14CB1D9004632E75C00834DB64DB4980292D3918D0034F3D90C958EECD8400414A11900403307534B524093EBCA00BCCD1B26AA52000FB4B6C62771CDF668E200CC20949D8AE2790051133B2ED005E2CC953FE1C3004EC0139ED46DBB9AC9C2655038C01399D59A3801F79EADAD878969D8318008491375003A324C5A59C7D68402E9B65994391A6BCC73A5F2FEABD8804322D90B25F3F4088F33E96D74C0139CF6006C0159BEF8EA6FBE3A9CEC337B859802B2AC9A0084C9DCC9ECD67DD793004E669FA2DE006EC00085C558C5134001088E308A20'
    print(f"kiwi p1: {sum_version(decode(kiwi))}")
    print(f"kiwi p2: {run(decode(kiwi))}")


    # test_code()
else:
    import time
    ll = hex_to_bin(load_file(filename))

    def part_one():
        packets = decode(ll)

        total = sum_version(packets)

        print(f"p1: {total}")

    def part_two():
        tic = time.perf_counter()

        ll = hex_to_bin(load_file(filename))
        packets = decode(ll)
        print(f"p2: {run(packets)}")

        toc = time.perf_counter()
        print(f"P2 time elapsed: {toc - tic:0.4f} seconds")

    part_one()
    part_two()

if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
