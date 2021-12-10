
import sys

def main():
    points = 0
    for p in parse_program(sys.stdin):
        points += p
    print(points)


def parse_program(lines):
    for line in lines:
        yield parse_statement(line.strip())

OPEN = set("({[<")

CLOSE = {
 ')': '(',
 '}': '{',
 ']': '[',
 '>': '<',
}
POINTS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

def parse_statement(line):
    stack = []
    for c in line:
        if c in OPEN:
            stack.append(c)
        elif CLOSE[c] == stack[-1]:
            stack.pop()
        else:
            return POINTS[c]
    return 0


if __name__ == "__main__":
    main()
