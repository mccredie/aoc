
import sys

from ex1 import TreeMap, traverse


directions = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]


def main():
    product = 1
    trees = TreeMap.from_lines(line.strip() for line in sys.stdin)
    for direction in directions:
        product *= traverse(trees, direction)
    print(product)

if __name__ == "__main__":
    main()



