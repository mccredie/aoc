
import sys
from collections import defaultdict

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

def add_tiles(a, b):
    return tuple(x + y for x, y in zip(a, b))

def adjacent(tile):
    for direction in DIRECTIONS.values():
        yield add_tiles(tile, direction)

class Floor:
    def __init__(self):
        self._tiles = defaultdict(int)

    def flip(self, directions):
        tile = 0, 0, 0
        for direction in directions:
            tile = add_tiles(tile, direction)
        self._tiles[tile] += 1

    def is_black(self, tile):
        return self._tiles[tile] % 2 == 1

    def interesting_tiles(self):
        interesting_tiles = set()
        for tile in self.black_tiles:
            for adj in adjacent(tile):
                interesting_tiles.add(adj)
            interesting_tiles.add(tile)
        return interesting_tiles

    def adjacent_black(self, tile):
        return sum(self.is_black(adj) for adj in adjacent(tile))

    def day(self):
        new_tiles = defaultdict(int, self._tiles)
        interesting_tiles = self.interesting_tiles()
        for tile in interesting_tiles:
            black_adj = self.adjacent_black(tile)
            if self.is_black(tile):
                if 0 == black_adj or black_adj  > 2:
                    new_tiles[tile] = self._tiles[tile] + 1
            else:
                if black_adj == 2:
                    new_tiles[tile] = self._tiles[tile] + 1
        self._tiles = new_tiles


    @property
    def black_tiles(self):
        for tile in self._tiles:
            if self.is_black(tile):
                yield tile

    def count_blacks(self):
        count = 0
        for tile in self.black_tiles:
            count += 1
        return count

def main():
    floor = Floor()
    for dirs in read_input(sys.stdin):
        floor.flip(dirs)

    for day in range(100):
        floor.day()
    print(floor.count_blacks())

if __name__ == "__main__":
    main()
