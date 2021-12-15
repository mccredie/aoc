import re
import sys


def main():
    points, folds = parse_input(sys.stdin)
    page = Page()

    for point in points:
        page.add(point)

    for dir, coord in folds:
        if dir == 'y':
            page.fold_y(coord)
        elif dir == 'x':
            page.fold_x(coord)

    print(page)


FOLD = re.compile(r"^fold along (?P<dir>\w)=(?P<coord>[0-9]+)$")


class Page:
    def __init__(self):
        self.points = set()

    def add(self, coord):
        self.points.add(coord)

    def fold_x(self, coord):
        discard = set()
        points = set()
        for point in self.points:
            x, y = point
            if x >= coord:
                discard.add(point)
                new_x = 2 * coord - x
                points.add((new_x, y))
        self.points -= discard
        self.points |= points

    def fold_y(self, coord):
        discard = set()
        points = set()
        for point in self.points:
            x, y = point
            if y >= coord:
                discard.add(point)
                new_y = 2 * coord - y
                points.add((x, new_y))
        self.points -= discard
        self.points |= points

    @property
    def dx(self):
        return 1 + max(x for x, _ in self.points)

    @property
    def dy(self):
        return 1 + max(y for _, y in self.points)

    def __str__(self):
        out = []
        for y in range(self.dy):
            line = []
            for x in range(self.dx):
                point = x, y
                if point in self.points:
                    line.append("#")
                else:
                    line.append(" ")
            out.append("".join(line))
        return "\n".join(out)


def parse_input(lines):
    points = []
    for line in lines:
        line = line.strip()
        if not line:
            break
        point = parse_point(line)
        points.append(point)

    folds = []
    for line in lines:
        match = FOLD.match(line)
        d = match.group("dir")
        c = int(match.group("coord"))
        folds.append((d, c))

    return points, folds


def parse_point(line):
    return tuple(int(x) for x in line.split(","))


if __name__ == "__main__":
    main()

