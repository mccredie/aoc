import sys

def read_input(input_str):
    for digit in input_str:
        yield int(digit)

class CupGame:
    def __init__(self, digits):
        self._digits = list(digits)

    def iterate(self):
        removed = self._remove()
        dest = self._find_destination()
        self._insert(dest, removed)

    def _remove(self):
        removed = self._digits[1:4]
        del self._digits[1:4]
        return removed

    def _find_destination(self):
        start = self._digits[0] - 1
        for dest in range(start, -1, -1):
            try:
                return self._digits.index(dest)
            except ValueError:
                pass
        for dest in range(max(self._digits), self._digits[0], -1):
            try:
                return self._digits.index(dest)
            except ValueError:
                pass

    def _insert(self, dest, removed):
        current = self._digits[0]
        before = self._digits[1:dest + 1]
        after = self._digits[dest + 1:]
        self._digits = before + removed + after + [current]

    def result(self):
        start = self._digits.index(1)
        return "".join(str(d) for d in self._digits[start + 1:]) + "".join(str(d) for
                d in self._digits[:start])

def main():
    digits = read_input(sys.argv[1])
    game = CupGame(digits)
    for _ in range(100):
        game.iterate()

    print(game.result())


if __name__ == "__main__":
    main()
