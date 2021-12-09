import sys

def main():
    map = Map()
    for pos, depth in parse_map(sys.stdin):
        map.add_point(pos, depth)

    print(map.risk)

class Map:
    def __init__(self):
        self.map = {}
        self.dx = 0
        self.dy = 0

    def add_point(self, point, depth):
        x, y = point
        self.dx = max(x, self.dx)
        self.dy = max(y, self.dy)
        self.map[point] = depth

    @property
    def risk(self):
        risk = 0
        for pos, depth in self.map.items():
            if depth < min(self._adjacent(pos)):
                risk += 1 + depth
        return risk

    def _adjacent(self, pos):
        x, y = pos
        if x != 0:
            yield self.map[x - 1, y]
        if x != self.dx:
            yield self.map[x + 1, y]
        if y != 0:
            yield self.map[x, y - 1]
        if y != self.dy:
            yield self.map[x, y + 1]

def parse_map(lines):
    for i, line in enumerate(lines):
        for j, x in enumerate (parse_row(line.strip())):
            yield (i, j), x


def parse_row(line):
    for n in line:
        yield int(n)

if __name__ == "__main__":
    main()
