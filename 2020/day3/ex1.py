
import sys
from helpers import traverse, TreeMap, Point


def main():
    print(traverse(TreeMap.from_lines(sys.stdin), Point(3, 1)))


if __name__ == "__main__":
    main()
