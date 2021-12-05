import sys
from collections import Counter


def main():
    grid = Grid()

    for line in parse_input(sys.stdin):
        grid.mark(line)

    print(grid.dangerous_count)

def parse_input(lines):
    for line in lines:
        yield tuple(parse_point(p) for p in line.split(" -> "))

def parse_point(point):
    return tuple(int(x) for x in point.split(","))

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

def direction(f, t):
    if f == t:
        return 0
    elif f < t:
        return 1
    else:
        return -1

def points(line):
    frm, to = line
    x, y = frm
    ex, ey = to

    dx = direction(x, ex)
    dy = direction(y, ey)

    while x != ex or y != ey:
        yield x, y
        x += dx
        y += dy
    yield x, y

if __name__ == "__main__":
    main()
