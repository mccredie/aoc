import sys
from itertools import tee
from collections import Counter


def main():
    polymer, template = read_input(sys.stdin)

    for _ in range(10):
        polymer = template.apply(polymer)

    counts = Counter(polymer).most_common()

    _, most = counts[0]
    _, least = counts[-1]
    print(most - least)


def read_input(lines):
    lines = iter(lines)

    polymer = next(lines).strip()

    # skip a line
    next(lines, None)

    template = Template()
    for line in lines:
        pair, insert = line.strip().split(" -> ")
        template.add_rule(pair, insert)

    return polymer, template

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

class Template:
    def __init__(self):
        self._rules = {}

    def add_rule(self, pair, insert):
        a, b = pair
        self._rules[a, b] = insert


    def apply(self, polymer):
        return "".join(self._apply(polymer))

    def _apply(self, polymer):
        for a, b in pairwise(polymer):
            yield a
            yield self._rules.get((a, b), '')
        yield b



if __name__ == "__main__":
    main()
