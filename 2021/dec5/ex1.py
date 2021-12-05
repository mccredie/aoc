import sys
from collections import Counter


def main():
    grid = Grid()
    lines = (line for line in parse_input(sys.stdin) if orthogonal(line))

    for line in lines:
        grid.mark(line)

    print(grid.dangerous_count)

def parse_input(lines):
    for line in lines:
        yield tuple(parse_point(p) for p in line.split(" -> "))

def parse_point(point):
    return tuple(int(x) for x in point.split(","))

def orthogonal(line):
    return any(a == b for a, b in zip(*line))

class Grid:
    def __init__(self):
        self.counts = Counter()

    def mark(self, line):
        for point in points(line):
            self.counts[point] += 1

    @property
    def dangerous_count(self):
        count = 0
        for _, c in self.counts.most_common():
            if c > 1:
                count += 1
        return count

def points(line):
    frm, to = sorted(line)
    for x in range(frm[0], to[0] + 1):
        for y in range(frm[1], to[1] + 1):
            yield x, y


if __name__ == "__main__":
    main()
