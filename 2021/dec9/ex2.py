import sys


def main():
    map = Map()
    for pos, depth in parse_map(sys.stdin):
        if depth != 9:
            map.add_point(pos)

    basins = list(len(c) for c in map.basins)
    basins.sort()
    a, b, c = basins[-3:]

    print(a*b*c)


class Map:
    def __init__(self):
        self.positions = set()

    def add_point(self, point):
        self.positions.add(point)

    @property
    def basins(self):
        while self.positions:
            p = self.positions.pop()
            yield self.cluster(p)

    def cluster(self, p):
        cluster = set()
        stack = [p]
        while stack:
            p = stack.pop()
            cluster.add(p)
            self.positions.discard(p)
            for a in self._adjacent_exists(p):
                stack.append(a)

        return cluster

    def _adjacent_exists(self, pos):
        for point in self._adjacent_points(pos):
            if point in self.positions:
                yield point

    def _adjacent_points(self, pos):
        x, y = pos
        yield x - 1, y
        yield x + 1, y
        yield x, y - 1
        yield x, y + 1


def parse_map(lines):
    for i, line in enumerate(lines):
        for j, x in enumerate (parse_row(line.strip())):
            yield (i, j), x


def parse_row(line):
    for n in line:
        yield int(n)


if __name__ == "__main__":
    main()
