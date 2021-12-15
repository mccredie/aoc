import sys
from itertools import tee
from collections import Counter


def main():
    template = read_input(sys.stdin)

    for _ in range(40):
        template.step()

    print(template.count)

def read_input(lines):
    lines = iter(lines)

    polymer = next(lines).strip()

    # skip a line
    next(lines, None)

    template = Template(polymer)
    for line in lines:
        pair, insert = line.strip().split(" -> ")
        template.add_rule(pair, insert)

    return template

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

class Template:
    def __init__(self, polymer):
        self._pairs = Counter(pairwise(polymer))
        self._counts = Counter(polymer)
        self._rules = {}

    def add_rule(self, pair, rule):
        a, b = pair
        self._rules[a, b] = rule

    def step(self):
        updates = Counter()
        for pair, count in self._pairs.items():
            try:
                center = self._rules[pair]
            except KeyError:
                pass
            else:
                updates[pair] -= count
                updates[pair[0], center] += count
                updates[center, pair[1]] += count
                self._counts[center] += count
        self._pairs.update(updates)

    @property
    def count(self):
        common = self._counts.most_common()
        return common[0][1] - common[-1][1]


if __name__ == "__main__":
    main()
