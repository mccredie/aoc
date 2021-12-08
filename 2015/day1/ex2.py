import sys


def main():
    floor = 0
    for i, d in enumerate(parse_input(sys.stdin), 1):
        floor += d
        if floor < 0:
            break
    print(i)

def parse_input(lines):
    for line in lines:
        for c in line:
            if c == '(':
                yield 1
            elif c == ')':
                yield -1

if __name__ == "__main__":
    main()
