import sys


def main():
    numbers, game = parse_input(iter(sys.stdin))

    for number in numbers:
        game.play(number)
        if game.over:
            break;

    print(game.win_code)


def parse_input(lines):
    numbers = [int(x) for x in next(lines).split(',')]
    games = []

    while next(lines, None) is not None:
        games.append(parse_board(lines))

    return numbers, Game(games)

def parse_board(lines):
    board = Board()
    for i in range(5):
        row = [int(x) for x in next(lines).split()]
        for j, x in enumerate(row):
            board.put((j, i), x)
    return board


class Game:
    def __init__(self, boards):
        self.boards = boards
        self.last_number = None
        self.winner = None

    def play(self, number):
        for board in self.boards:
            self.last_number = number
            board.play(number)
            if board.wins:
                self.winner = board

    @property
    def over(self):
        return self.winner is not None

    @property
    def win_code(self):
        return sum(self.winner.unmarked) * self.last_number


class Board:
    def __init__(self):
        self.rows = [set(), set(), set(), set(), set()]
        self.cols = [set(), set(), set(), set(), set()]

    def put(self, coord, value):
        self.rows[coord[0]].add(value)
        self.cols[coord[1]].add(value)

    def play(self, number):
        for row in self.rows:
            row.discard(number)
        for col in self.cols:
            col.discard(number)

    @property
    def wins(self):
        return (
                any(len(row) == 0 for row in self.rows)
                or any(len(col) == 0 for col in self.cols))

    @property
    def unmarked(self):
        for row in self.rows:
            yield from row


if __name__ == "__main__":
    main()
