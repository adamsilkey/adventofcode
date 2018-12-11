#! python3

from dataclasses import dataclass

def main_test():
    fabric_claims = [ 
        FabricClaim.from_claimstring('#1 @ 1,3: 4x4'),
        FabricClaim.from_claimstring('#2 @ 3,1: 4x4'),
        FabricClaim.from_claimstring('#3 @ 5,5: 2x2'),
    ]

    overlapped_inches, master_fabric, overlapping_claims = find_overlapped_inches(fabric_claims, 8, 8)
    print(overlapped_inches)
    for line in master_fabric:
        print(line)
    print(sorted(overlapping_claims))


def main():
    fabric_claims = []
    biggest_x = 0
    biggest_y = 0
    with open("Day03Input.txt") as f:
        for line in f:
            claim = FabricClaim.from_claimstring(line)
            fabric_claims.append(claim)
            if claim.x2 > biggest_x:
                biggest_x = claim.x2
            if claim.y2 > biggest_y:
                biggest_y = claim.y2

    print(f"x: {biggest_x}, y: {biggest_y}")

    overlapped_inches, master_fabric, overlapping_claims = find_overlapped_inches(fabric_claims, biggest_x, biggest_y)

    print(f"overlapped inches: {overlapped_inches}")
    claims = set([claim.cid for claim in fabric_claims])
    print(claims - overlapping_claims)

def find_overlapped_inches(fabric_claims, x, y):
    master_fabric = [[[] for x in range(x)] for i in range(y)]
    overlapped_inches = 0
    overlapping_claims = set()
    for claim in fabric_claims:
        # Remember that it's masterfabric[row/y][column/x]
        for x in range(claim.width):
            for y in range(claim.height):
                x_coord = claim.left_edge + x
                y_coord = claim.top_edge + y
                master_fabric[y_coord][x_coord].append(claim.cid)
                # if this is > 2, it will double count, so we only care about the first time that the fabric overlaps
                if len(master_fabric[y_coord][x_coord]) == 2:
                    overlapped_inches += 1
                if len(master_fabric[y_coord][x_coord]) > 1:
                    for cid in master_fabric[y_coord][x_coord]:
                        overlapping_claims.add(cid)

    return overlapped_inches, master_fabric, overlapping_claims


@dataclass
class FabricClaim:
    cid: int
    left_edge: int
    top_edge: int
    width: int
    height: int

    @property
    def x1(self):
        return self.left_edge

    @property
    def x2(self):
        return self.left_edge + self.width

    @property
    def y1(self):
        return self.top_edge

    @property
    def y2(self):
        return self.top_edge + self.height

    @classmethod
    def from_claimstring(cls, claimstring):
        claim = claimstring.split()
        cid = claim[0][1:]
        left_edge, top_edge = claim[2][:-1].split(',')
        width, height = claim[3].split('x')
        return cls(int(cid), int(left_edge), int(top_edge), int(width), int(height))

    @staticmethod
    def claim_intersection(claim1, claim2):
        x_intersection = FabricClaim._calculate_intersection(
                claim1.x1, claim1.x2, claim2.x1, claim2.x2)
        y_intersection = FabricClaim._calculate_intersection(
                claim1.y1, claim1.y2, claim2.y1, claim2.y2)

        return x_intersection or y_intersection

    @staticmethod
    def _calculate_intersection(a0, a1, b0, b1):
        if a0 >= b0 and a1 <= b1: #b contains a
            intersection = a1 - a0
        elif a0 < b0 and a1 > b1: #a contains b
            intersection = b1 - b0
        elif a0 < b0 and a1 > b0: #intersects right
            intersection = a1 - b0
        elif a1 > b1 and a0 < b1: #intersects left
            intersection = b1 - a0
        else: #no intersection
            intersection = 0

        return intersection

if __name__ == '__main__':
    # main_test()
    main()
