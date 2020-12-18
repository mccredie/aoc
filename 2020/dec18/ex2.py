
import sys
from shlex import shlex
import operator


OPERATORS = {'+': 1, '*': 0}
OPERATOR_FUNCS = {
    '+': operator.add,
    '*': operator.mul,
}

def shunting_yard(input_str):
    output = []
    operators = []
    for tok in shlex(input_str):
        if tok.isdecimal():
            output.append(int(tok))
        elif tok in OPERATORS:
            while operators and operators[-1] != '(' and OPERATORS[tok] <= OPERATORS[operators[-1]]:
                output.append(operators.pop())
            operators.append(tok)
        elif tok == '(':
            operators.append(tok)
        elif tok == ')':
            while operators[-1] != '(':
                output.append(operators.pop())
            if operators[-1] == '(':
                operators.pop()
    while operators:
        output.append(operators.pop())
    return output

def evaluate(line):
    inputs = shunting_yard(line)
    stack = []
    for tok in inputs:
        if isinstance(tok, int):
            stack.append(tok)
        elif tok in OPERATOR_FUNCS:
            stack.append(OPERATOR_FUNCS[tok](stack.pop(), stack.pop()))
    return stack[0]

def main():
    total = 0
    for line in sys.stdin:
        value = evaluate(line)
        total += value
    print(total)

if __name__ == "__main__":
    main()


