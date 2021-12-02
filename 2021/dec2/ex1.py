import sys


def main():
    depth = 0
    horiz = 0

    for line in sys.stdin:
        command, dist = line.split(' ')
        dist = int(dist)

        if command == 'forward':
            horiz += dist
        elif command == 'down':
            depth += dist
        elif command == 'up':
            depth -= dist

    print(depth * horiz)

if __name__ == "__main__":
    main()
