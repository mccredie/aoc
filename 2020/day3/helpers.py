class TreeMap:
    def __init__(self, size):
        self._size = Point(size)
        self._trees = set()

    def add_tree(self, location):
        self._trees.add(location)

    def __contains__(self, location):
        x, y = location
        x %= self.width
        return Point(x, y) in self._trees

    @property
    def height(self):
        return self._size.y

    @property
    def width(self):
        return self._size.x

    @staticmethod
    def from_lines(lines):
        """ Create an instance of TreeMap from a sequence of strings. Leading
            and trailing whitespace is removed. Can accept a file object.
        """
        lines = [line.strip() for line in lines]
        the_map = TreeMap((len(lines[0]), len(lines)))
        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                if char == '#':
                    the_map.add_tree(Point(j, i))
        return the_map


class Point(tuple):
    def __new__(cls, *args):
        if len(args) == 1:
            args = args[0]
        return super(Point, cls).__new__(cls, args)

    @property
    def x(self):
        return self[0]

    @property
    def y(self):
        return self[1]

    def __add__(self, other):
        return Point(sum(points) for points in zip(self, other))


def traverse(trees, direction):
    location = Point(0, 0)
    trees_hit = 0

    while location.y < trees.height:
        trees_hit += location in trees
        location += direction

    return trees_hit
