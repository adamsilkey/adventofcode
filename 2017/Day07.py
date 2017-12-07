import sys

test_inp = None
test_solution = 'tknk'

with open('test_input2.txt') as f:
    test_inp = f.readlines()

with open('input.txt') as f:
    inp = f.readlines()

class Disk:
    def __init__(self, inp):
        inp = inp.split()
        self.name = inp.pop(0)
        self.weight = int(inp.pop(0)[1:-1])
        if inp:
            inp.pop(0)
            self.other_disks = inp[:]
            for idx, disk in enumerate(self.other_disks):
                if disk[-1] == ',':
                    self.other_disks[idx] = disk[:-1]
        else:
            self.other_disks = []
        self.tree = {self.name: self.other_disks}
        self.parent = None
        self.level = None
        self.total_weight = None
        self.balanced = None

    def print(self):
        print(f"name: {self.name}")
        #print(f"weight: {self.weight}")
        print(f"other_disks: {self.other_disks}")
        #print(f"tree: {self.tree}")
        print(f"parent: {self.parent}")
        print(f"level: {self.level}")
        print(f"total_weight: {self.total_weight}")
        print(f"balanced: {self.balanced}")
        print()

def test_disk():
    test_disk = Disk('ugml (68) -> gyxo, ebii, jptl')
    test_disk.print()
    print(test_disk.name)
    print(test_disk.weight)
    print(test_disk.other_disks)
    sys.exit()

def get_unsorted_tower(inp):
    tower = {}
    for line in inp:
        disk = Disk(line)
        tower[disk.name] = disk

    return tower

def sort_tower(unsorted_tower):
    tower = {}
    # makes copy of tower
    for name, disk in unsorted_tower.items():
        tower[name] = disk
    # gets everyone's parent
    for name, disk in tower.items():
        if disk.other_disks:
            for other_disk in disk.other_disks:
                tower[other_disk].parent = disk.name

    return tower

def generate_total_weight(tower, disk):
    #print(f'inside {disk.name}')
    if disk.total_weight is None:
        for child_disk in disk.other_disks:
            if tower[child_disk].total_weight is None:
                #print(f'walking -> {child_disk}')
                generate_total_weight(tower, tower[child_disk])
        else:
            #print(f'calculating weight for {disk.name}')
            disk.total_weight = disk.weight
            for child_disk in disk.other_disks:
                disk.total_weight += tower[child_disk].total_weight


def solve(inp):
    tower = sort_tower(get_unsorted_tower(inp))

    found_disk = None
    for name, disk in tower.items():
        if disk.parent is None:
            found_disk = name
            print(found_disk)
    return found_disk


assert(solve(test_inp) == test_solution)

solve(inp)
