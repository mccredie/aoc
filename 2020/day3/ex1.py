
import sys


class TreeMap:
    def __init__(self, size):
        self._size = tuple(size)
        self._trees = set()

    def add_tree(self, location):
        self._trees.add(location)

    def __contains__(self, location):
        return location in self._trees

    @property
    def height(self):
        return self._size[1]

    @property
    def width(self):
        return self._size[0]

    @staticmethod
    def from_lines(lines):
        lines = list(lines)
        the_map = TreeMap((len(lines[0]), len(lines)))
        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                if char == '#':
                    the_map.add_tree((j, i))
        return the_map


def add_points(*args):
    return tuple(sum(points) for points in zip(*args))


def traverse(trees, direction):
    location = (0, 0)
    trees_hit = 0

    while location[1] < trees.height:
        trees_hit += location in trees
        location = add_points(direction, location)
        location = location[0] % trees.width, location[1]

    return trees_hit


def main():
    trees = TreeMap.from_lines(line.strip() for line in sys.stdin)
    print(traverse(trees, (3, 1)))


if __name__ == "__main__":
    main()
