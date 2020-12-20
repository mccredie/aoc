
import sys
from pprint import pprint as pp
from collections import Counter

def parse_tiles(lines):
    tile_id = ""
    tiles = []
    tile_lines = []
    for line in lines:
        line = line.strip()
        if line.startswith("Tile"):
            tile_id = line
            tile_lines = []
        elif line:
            tile_lines.append(line)
        else:
            tiles.append(Tile(tile_lines))
            tile_lines = []
    if tile_lines:
        tiles.append(Tile(tile_lines))
    return tiles

class Tile:
    def __init__(self, lines):
        self.lines = list(lines)

    def shared_edge(self, other):
        for edge in self.edges:
            if edge in other.edges:
                return edge

    def find_match_right(self, tiles):
        right = self.right
        for tile in tiles:
            for edge in tile.edges:
                if right in edge:
                    return tile

    def find_match_bottom(self, tiles):
        for tile in tiles:
            if any(self.bottom in edge for edge in tile.edges):
                return tile

    @property
    def edges(self):
        return [
                edge_set(self.top),
                edge_set(self.right),
                edge_set(self.bottom),
                edge_set(self.left),
        ]

    @property
    def top(self):
        return self.lines[0]

    @property
    def right(self):
        return "".join(line[-1] for line in self.lines)
    @property
    def bottom(self):
        return self.lines[-1]

    @property
    def left(self):
        return "".join(line[0] for line in self.lines)

    def find_adjacent(self, tiles):
        adjacent = []
        for tile in tiles:
            if tile is not self and tile.shared_edge(self):
                adjacent.append(tile)
        return adjacent

    def rotate_right(self):
        return Tile("".join(x) for x in zip(*reversed(self.lines)))

    def flip(self):
        return Tile(reversed(self.lines))

    def iter_orientations(self):
        tile = self
        for _ in range(4):
            yield tile
            tile = tile.rotate_right()
        tile = tile.flip()
        for _ in range(3):
            yield tile
            tile = tile.rotate_right()
        yield tile

    def strip_edges(self):
        out = []
        for line in self.lines[1:-1]:
            out.append(line[1:-1])
        return out

    def shape_at(self, shape, x, y):
        return all(
            self.lines[py][px] == '#'
            for px, py in shape.points(x, y))

    def find_shapes(self, shape):
        for y in range(len(self.lines) - shape.height):
            for x in range(len(self.lines[0]) - shape.width):
                if self.shape_at(shape, x, y):
                    yield x, y


    def __str__(self):
        return "\n".join(self.lines)

class Shape:
    def __init__(self, lines):
        self.lines = list(lines)

    @property
    def width(self):
        return max(len(line) for line in self.lines)

    @property
    def height(self):
        return len(self.lines)

    def points(self, offsetx, offsety):
        for y, line in enumerate(self.lines):
            for x, c in enumerate(line):
                if c == '#':
                    yield x + offsetx, y + offsety

def edge_set(edge):
    return frozenset([edge, "".join(reversed(edge))])

def find_corner(tiles):
    for tile in tiles:
        adjacent = tile.find_adjacent(tiles)
        if len(adjacent) == 2:
            return tile, adjacent

def find_all_adjacent(tiles):
    all_adjacent = []
    for tile in tiles:
        adjacent = tile.find_adjacent(tiles)
        all_adjacent.append(adjacent)
    return all_adjacent

def build_grid(tiles):
    tiles = list(tiles)
    # find a corner
    corner, adjacent = find_corner(tiles)
    # remove corner from tiles
    tiles.remove(corner)
    grid = {}
    x, y = 0, 0
    for o in corner.iter_orientations():
        # orient corner so that it has blanks on top and left (top left corner)
        if o.find_match_right(adjacent) and o.find_match_bottom(adjacent):
            # set corner as base tile
            base = o
            break
    grid[x,y] = base
    # while tiles to match:
    while tiles:
        #  find a tile that matches with the right edge of base tile
        if match := base.find_match_right(tiles):
            x += 1
            #  if found
            #   remove it from tiles
            tiles.remove(match)
            for o in match.iter_orientations():
                if o.left == base.right:
                    #   orient it to mate with base tile
                    #   set found tile as base tile
                    grid[x, y] = o
                    base = o
                    break
            else:
                raise Exception("left/right orientation not found")
        else:
            #  else:
            base = grid[0, y]
            #   find a tile that matches with the bottom edge of the left most tile in
            #   the previous row
            if match := base.find_match_bottom(tiles):
                x, y = 0, y + 1
                #   remove the tile from tiles
                tiles.remove(match)

                #   orient the tile to mate
                for o in match.iter_orientations():
                    if o.top == base.bottom:
                        #   set tile as base tile
                        grid[x, y] = o
                        base = o
                        break
                else:
                    raise Exception("top/bottom orientation not found")
            else:
                raise Exception("Shouldn't happen")

    return grid

def combine_grid(grid):
    lines = []
    maxx, maxy = max(grid)
    for y in range(maxy + 1):
        for row in zip(*[grid[x, y].strip_edges() for x in range(maxx + 1)]):
            lines.append("".join(row))
    return Tile(lines)

def main():
    tiles = parse_tiles(sys.stdin)
    grid = build_grid(tiles)
    tile = combine_grid(grid)
    sea_monster = Shape([
        "                  # ",
        "#    ##    ##    ###",
        " #  #  #  #  #  #   ",
    ])
    found = False
    for o in tile.iter_orientations():
        for location in o.find_shapes(sea_monster):
            found = True
            break
        if found:
            tile = o
            break
    sea_monster_tiles = set()
    seas = Shape(tile.lines)
    roughness = set(seas.points(0, 0))
    for location in tile.find_shapes(sea_monster):
        for point in sea_monster.points(*location):
            roughness.discard(point)
    print(len(roughness))


if __name__ == "__main__":
    main()
