
import sys

from helpers import TreeMap, traverse, Point

directions = [
    Point(1, 1),
    Point(3, 1),
    Point(5, 1),
    Point(7, 1),
    Point(1, 2),
]


def main():
    product = 1
    trees = TreeMap.from_lines(sys.stdin)
    for direction in directions:
        product *= traverse(trees, direction)
    print(product)


if __name__ == "__main__":
    main()
