
import sys
from itertools import tee

def triplewise(iterable):
    "Return overlapping triplets from an iterable"
    # triplewise('ABCDEFG') -> ABC BCD CDE DEF EFG
    a, b = tee(iterable)
    next(b, None)
    b, c = tee(b)
    next(c, None)

    return zip(a, b, c)

def main():
    current, *depths = [sum(trip) for trip in triplewise(int(depth) for depth in sys.stdin)]

    increases = 0;
    for depth in depths:
        increases += depth > current
        current = depth

    print(increases)


if __name__ == "__main__":
    main()
