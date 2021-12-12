import sys

def main():
    map = Map()
    for coord, level in read_map(sys.stdin):
        map.add_level(coord, level)

    for _ in range(100):
        map.step()

    print(map.flashes)

def read_map(lines):
    for y, line in enumerate(lines):
        for x, level in enumerate(line.strip()):
            yield (x, y), int(level)

class Map:
    flashes = 0
    dx = 0
    dy = 0
    def __init__(self):
        self.map = {}

    def add_level(self, coord, level):
        x, y = coord
        self.dx = max(x + 1, self.dx)
        self.dy = max(y + 1, self.dy)
        self.map[coord] = level

    def step(self):
        flash_stack = []
        for coord in self.coords:
            self.map[coord] += 1
            if self.map[coord] > 9:
                flash_stack.append(coord)

        while flash_stack:
            flash = flash_stack.pop()
            if flash in self.map:
                self.flashes += 1
                del self.map[flash]
                for coord in self.adjacent(flash):
                    self.map[coord] += 1
                    if self.map[coord] > 9:
                        flash_stack.append(coord)

        for coord in self.coords:
            self.map.setdefault(coord, 0)

    def adjacent(self, coord):
        x, y = coord
        for dx in range(-1, 2):
            ax = x + dx
            for dy in range(-1, 2):
                acoord = ax, y + dy
                if acoord != coord and acoord in self.map:
                    yield acoord

    @property
    def coords(self):
        for x in range(self.dx):
            for y in range(self.dy):
                yield x, y

if __name__ == "__main__":
    main()

