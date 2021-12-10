
import sys

def main():
    scores = [score for score in parse_program(sys.stdin) if score]
    scores.sort()

    middle_index = len(scores) // 2

    print(scores[middle_index])

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
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}

def parse_statement(line):
    stack = []
    for c in line:
        if c in OPEN:
            stack.append(c)
        elif CLOSE[c] == stack[-1]:
            stack.pop()
        else:
            return 0
    points = 0
    for c in stack[-1::-1]:
        points *= 5
        points += POINTS[c]

    return points

if __name__ == "__main__":
    main()
