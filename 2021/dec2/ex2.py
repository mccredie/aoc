import sys


def main():
    depth = 0
    horiz = 0
    aim = 0

    for line in sys.stdin:
        command, dist = line.split(' ')
        dist = int(dist)

        if command == 'forward':
            horiz += dist
            depth += dist * aim
        elif command == 'down':
            aim += dist
        elif command == 'up':
            aim -= dist

    print(depth * horiz)

if __name__ == "__main__":
    main()
