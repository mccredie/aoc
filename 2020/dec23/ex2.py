import sys
from dataclasses import dataclass

@dataclass
class Position:
    label: int
    destination: 'Position' = None
    p: 'Position' = None
    n: 'Position' = None

def read_input(input_str):
    for digit in input_str:
        yield int(digit)

def print_pos(pos):
    if pos:
        n = "none"
        if pos.n:
            n = pos.n.label
        p = "none"
        if pos.p:
            p = pos.p.label

        d = "none"
        if pos.destination:
            d = pos.destination.label
        print(pos.label, "n", n, "p", p, "d", d)
    else:
        print("none")

def print_10_pos(pos):
    for _ in range(10):
        print_pos(pos)
        pos = pos.n

def build_start_pos(digits):
    digits = list(digits)
    first = Position(label=digits[0])
    positions = {
        digits[0]: first,
    }
    last_pos = first
    for d in digits[1:]:
        p = Position(label=d)
        p.p = last_pos
        last_pos.n = p
        positions[d] = p
        last_pos = p
    last_input_pos = last_pos
    # Fix destinations
    for d, p in positions.items():
        if d - 1 in positions:
            p.destination = positions[d - 1]
    # Add ranged positions
    for d in range(max(digits) + 1, 1000001):
        p = Position(label=d)
        p.p = last_pos
        p.destination = last_pos
        last_pos.n = p
        last_pos = p
    first_range_input = last_input_pos.n
    first_range_input.destination = positions[first_range_input.label - 1]
    last_pos.n = first
    first.p = last_pos
    positions[1].destination = last_pos

    return first, positions[1]


class CupGame:
    def __init__(self, digits):
        self.current, self.one  = build_start_pos(digits)

    def iterate(self):
        removed = self._remove()
        dest = self._find_destination(removed)
        self._insert(dest, removed)
        self.current = self.current.n

    def _remove(self):
        r0 = self.current.n
        r1 = r0.n
        r2 = r0.n.n
        self.current.n = r2.n
        r2.n.p = self.current
        return r0, r1, r2

    def _find_destination(self, removed):
        d = self.current.destination
        while d in removed:
            d = d.destination
        return d

    def _insert(self, dest, removed):
        last = dest.n
        dest.n = removed[0]
        removed[0].p = dest
        last.p = removed[-1]
        removed[-1].n = last

    def result(self):
        return self.one.n.label * self.one.n.n.label

def main():
    digits = read_input(sys.argv[1])
    game = CupGame(digits)
    for _ in range(10000000):
        game.iterate()
    print(game.result())


if __name__ == "__main__":
    main()
