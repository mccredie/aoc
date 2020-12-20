
import sys


def parse_tiles(lines):
    tile_id = ""
    tiles = {}
    tile_lines = []
    for line in lines:
        line = line.strip()
        if line.startswith("Tile"):
            tile_id = line
            tile_lines = []
        elif line:
            tile_lines.append(line)
        else:
            tiles[tile_id] = get_edges(tile_lines)
    tiles[tile_id] = get_edges(tile_lines)
    return tiles

def get_edges(tile_lines):
    edges = set()
    edges.add(frozenset([tile_lines[0], "".join(reversed(tile_lines[0]))]))
    right_edge = "".join(line[-1] for line in tile_lines)
    edges.add(frozenset([right_edge, "".join(reversed(right_edge))]))
    edges.add(frozenset([tile_lines[-1], "".join(reversed(tile_lines[-1]))]))
    left_edge = "".join(line[0] for line in tile_lines)
    edges.add(frozenset([left_edge, "".join(reversed(left_edge))]))
    return edges

def find_adjacent(the_tile_id, tiles):
    the_tile = tiles[the_tile_id]
    adjacent = []
    for tile_id, edges in tiles.items():
        if tile_id == the_tile_id:
            continue
        elif any(edge in the_tile for edge in edges):
            adjacent.append(tile_id)
    return adjacent

def main():
    tiles = parse_tiles(sys.stdin)
    corners = []
    for tile_id in tiles:
        adjacent = find_adjacent(tile_id, tiles)
        if len(adjacent) == 2:
            corners.append(tile_id)
    prod = 1
    for corner_id in corners:
        prod *= int(corner_id[5:-1])
    print(prod)


if __name__ == "__main__":
    main()
