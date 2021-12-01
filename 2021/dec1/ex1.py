
import sys

def main():
    current, *depths = [int(depth) for depth in sys.stdin]

    increases = 0;
    for depth in depths:
        increases += depth > current
        current = depth

    print(increases)


if __name__ == "__main__":
    main()
