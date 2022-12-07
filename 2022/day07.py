#! /usr/bin/env python3.11

YEAR = '2022'
AOC_DAY = '07'

import itertools as it
import re
import sys
from collections import Counter, defaultdict, deque, namedtuple
from dataclasses import dataclass
from string import ascii_letters, ascii_lowercase, ascii_uppercase

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
    FILENAME = f"input/{AOC_DAY}.test"
else:
    FILENAME = f"input/{AOC_DAY}.in"

title = f"Advent of Code {YEAR} - Day {AOC_DAY} - {'Test' if test else 'Production'}"

print(f"=" * len(title))
print(title)
print(f"=" * len(title))

def load_file(filename: str = FILENAME) -> str:
    """Loads an AOC file, returns a string"""

    with open(filename) as f:
        return f.read().rstrip("\n")


def load_lines(filename: str = FILENAME) -> list[str]:
    """Returns a list of lines"""

    return load_file(filename).split("\n")


def load_ints(filename: str = FILENAME) -> list[int]:
    """Returns a list of ints"""

    return [int(i) for i in load_lines(filename)]


def load_comma_separated_ints(filename: str = FILENAME) -> list[int]:
    """Returns a list of ints from a comma separated list of ints"""

    return [int(i) for i in load_file(filename).strip().split(",")]



## Regex / list/map helpers
# number_of_stacks = max(map(int, stacks.pop().split()))
# qty, old, new = list(map(int, re.findall(r'\d+', move)))
#   - map(function, target)
#   - map needs to bec onverted to a list (or other object)

p = load_lines(FILENAME)


# for line in p:
#     if line.startswith("$"):
#         #process command
#         if ' cd ' in line:
#             _, _, cd = line.split()
#             print(cd)
#             if cd not in filesystem:
#                 filesystem[cd] = dict(
#                     size = 0,
#                     subdirs = {}
#                 )
#     else:
#         # if line
#         pass


## possible commands
## cd -- change directory
## ls -- run the get_sizes()
## possible entries
    ## dir a -- add this to a 


def get_sizes(directory, instructions):
    for line in instructions:
        if line.startswith("dir"):
            _, subdir = line.split()
            if subdir not in directory:
                directory[subdir] = dict (
                    size = 0,
                    subdirs = {},
                )
        # We have numbers!
        elif not line.startswith('$'):
            filesize, filename = line.split()
            directory['size'] += filesize
        
        else:
            return


def dispatch_command(line):
    line = line[2:]         # strip off the $
    if line.startswith('cd'):
        pass
    elif line.startswith('ls'):
        pass


## part 1
    # if gathering_instructions:
    #     if line.startswith('$'):
    #         get_sizes(filesystem[])
    #         pass
            
    #         # process
    #     else:
    #         instructions.append(line)
    #         continue

    # if line.startswith("$ cd"):
    #     cd = change_directory(line)
    # elif line.startswith("$ ls"):
    #     gathering_instructions = True









class File:
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)

    def __repr__(self):
        return f"File(name={self.name}, size={self.size})"

    def __hash__(self):
        return hash(self.name)


class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files = {}
        self.subdirs = []
    
    def __repr__(self):
        return f"Directory(name={self.name}, parent={self.parent}, files={self.files}, subdirectories={self.subdirs})"

    def __hash__(self):
        return hash(self.name)

    def get_size(self, filesystem, total=0):
        for file in self.files.values():
            # print(file)
            total += file.size
        for subdir in self.subdirs:
            # print(subdir)
            total = filesystem[subdir].get_size(filesystem, total)
        
        return total
        # print(f"{directory=} {total=}")
        # directory = self.directories[directory]
        # for file in directory.files.values():
        #     print(f"{file=}")
        #     total += file.size
        # for subdir in directory.subdirs:
        #     total = self.get_size(subdir, total)
        
        # return total


def change_directory(line):
    _, _, cd = line.split()
    return cd

def parse_filesystem(puzzle_input):
    # Initialize the root filesystem object
    current_path = [""]
    filesystem = {"/": Directory("/", None)}

    for line in puzzle_input[1:]:   # skip the / object
        if line.startswith('$ ls'):
            pass
        elif line.startswith("$ cd .."):
            current_path.pop()
        elif line.startswith("dir"):
            current = '/'.join(current_path) or '/'
            _, dirname = line.split()
            new_dir = '/'.join(current_path) + '/' + dirname
            filesystem[new_dir] = Directory(new_dir, current)
            filesystem[current].subdirs.append(new_dir)
            # print(new_dir, current)
        elif line.startswith("$ cd"):
            current_path.append(change_directory(line))
        else:
            size, name = line.split()
            current = '/'.join(current_path) or '/'
            f = filesystem[current].files[name] = File(name, size)
            # print(f, current)
            pass
    
    return filesystem
#             size, name = line.split()
#             # print(name)
#             self.directories[self.cd].files[name] = File(name, size, self.cd)
#             # self.files[name] = File(name, size, self.cd)



filesystem = parse_filesystem(p)

# for k, v in filesystem.items():
#     # print(k, v)
#     print(v.get_size(filesystem))






at_most = 100_000

total = 0
for d, v in filesystem.items():
    sz = v.get_size(filesystem)
    print(f"{d}: {sz}")
    if sz <= at_most:
        total += sz

print(f"p1: {total}")

# class Filesystem:
#     def __init__(self):
#         self.directories = {}
#         # self.files = {}
#         self.cd = ''
#         self.total_ls = 0
#         self.total_cd = 0

#     def parse_line(self, line):
#         if line.startswith("$ ls"):
#             self.total_ls += 1
#             pass
#         elif line.startswith("$ cd .."):
#             self.change_directory(self.directories[self.cd].parent)
#             pass
#             # get parent of current directory
#             # parent = self.directories
#             # change to that directory
#         elif line.startswith("$ cd"):
#             self.total_cd += 1
#             self.change_directory(line)
#             # Should only be the case for '/'
#             if self.cd not in self.directories:
#                 print("BOOM, you lookin for this? ", self.cd)
#                 self.directories[self.cd] = Directory(self.cd, None)
#         elif line.startswith("dir"):
#             _, dirname = line.split()
#             self.directories[dirname] = Directory(dirname, self.cd)
#             self.directories[self.cd].subdirs.append(dirname)
#         else:
#             size, name = line.split()
#             # print(name)
#             self.directories[self.cd].files[name] = File(name, size, self.cd)
#             # self.files[name] = File(name, size, self.cd)
    
#     def parse_input(self, puzzle_input):
#         for line in puzzle_input:
#             self.parse_line(line)
#         print(self.total_ls)
#         print(self.total_cd)


#     def get_size(self, directory, total=0):
#         print(f"{directory=} {total=}")
#         directory = self.directories[directory]
#         for file in directory.files.values():
#             print(f"{file=}")
#             total += file.size
#         for subdir in directory.subdirs:
#             total = self.get_size(subdir, total)
        
#         return total

#     # def get_dirsize(self, directory, total=0):
#     #     if total == 0:
#     #         print(f"Directory size for: {directory}")
#     #     for file in self.files:
#     #         total += file.size
#     #         print(f"-----------{file.name=} {file.size=}")
#     #     for subdir in self.subdirectories:
#     #         print(f"{self.name} : {self.subdirectories}")
#     #         total = self.filesystem[subdir].size(total)
        
#     #     return total






# for f, v in elfs.files.items():
#     print(f, v)




sys.exit()


class Directory:
    def __init__(self, name, parent, filesystem):
        self.name = name
        self.parent = parent
        self.filesystem = filesystem
        self.files = list()
        self.subdirectories = list()
    
    def __repr__(self):
        return f"{self.name} - {self.parent} - {self.files} - {self.subdirectories}"

    def __str__(self):
        return f"{self.name} - {self.parent} - {self.files} - {self.subdirectories}"
    
    def __hash__(self):
        return hash(self.name)

    def add_item(self, line):
        if line.startswith('dir'):
            _, subdir = line.split()
            if subdir not in self.subdirectories:
                self.subdirectories.append(subdir)
            if subdir not in self.filesystem:
                self.filesystem[new_cd] = Directory(name=new_cd, parent=cd, filesystem=self.filesystem)
        else:
            filesize, filename = line.split()
            self.files.append(File(filename, filesize))




# filesystem = {}
# cd = ''
# indentation_level = 0
# for idx, line in enumerate(p):
#     # print(f"{'  '*indentation_level} - {line}")
#     if line.startswith('$ cd ..'):
#         indentation_level -= 1
#         # print("going up!")
#         cd = filesystem[cd].parent
#         print(f"  {'  '*indentation_level} {cd}")
#     elif line.startswith('$ cd'):
#         print(f"{'  '*indentation_level} - {line}")
#         new_cd = change_directory(line)
#         if new_cd not in filesystem:
#             filesystem[new_cd] = Directory(name=new_cd, parent=cd, filesystem=filesystem)
#         cd = new_cd
#         indentation_level += 1
#     elif line.startswith('$ ls'):
#         pass
#     else:
#         print(f"adding {line}")
#         filesystem[cd].add_item(line)

# for k, v in filesystem.items():
#     print(v)
# import sys;sys.exit()
input()

# get files
sizes = []
total = 0
value_not_to_exceed = 100000
for directory in filesystem:
    sz = filesystem[directory].size()
    sizes.append(sz)
    print(f"{filesystem[directory].name=} : {filesystem[directory].size()}")

    if sz < value_not_to_exceed:
        total += sz

print(total)



print(sizes)


























if test:
    print()
    print("============ This was a test!!!! ============")
else:
    print()
    print("You just ran that production data. Nice work!")
