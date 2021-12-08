import sys


def main():
    print(sum(parse_input(sys.stdin)))

def parse_input(lines):
    for line in lines:
        for c in line:
            if c == '(':
                yield 1
            elif c == ')':
                yield -1

if __name__ == "__main__":
    main()
