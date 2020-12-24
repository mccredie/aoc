
import sys

def read_input(lines):
    for line in lines:
        yield list(directions(line.strip()))

DIRECTIONS = {
    'nw': (-1, 0, 1),
    'ne': (0, 1, 1),
    'e': (1, 1, 0),
    'se': (1, 0, -1),
    'sw': (0, -1, -1),
    'w': (-1, -1, 0),
}

def directions(line):
    chars = iter(line)
    try:
        while True:
            c = next(chars)
            if c in 'ns':
                yield DIRECTIONS[c+next(chars)]
            else:
                yield DIRECTIONS[c]
    except StopIteration:
        pass

class Floor:
    def __init__(self):
        self._tiles = {}

    def flip(self, directions):
        x, y, z = 0, 0, 0
        for dx, dy, dz in directions:
            x += dx
            y += dy
            z += dz

        color = self._tiles.get((x, y, z), 0)
        self._tiles[x, y, z] = color + 1

    def count_blacks(self):
        count = 0
        for color in self._tiles.values():
            count +=  color % 2
        return count

def main():
    floor = Floor()
    for dirs in read_input(sys.stdin):
        floor.flip(dirs)
    print(floor.count_blacks())

if __name__ == "__main__":
    main()
