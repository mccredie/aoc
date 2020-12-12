import sys

def read_input():
    for line in sys.stdin:
        yield line.strip()

def get_actions(lines):
    for line in lines:
        yield line[0], int(line[1:])

class Ship:
    position = 0, 0
    direction = 0
    directions = (1, 0), (0, -1), (-1, 0), (0, 1)

    def update(self, command):
        action, amount = command
        f = getattr(self, f'update_{action}')
        f(amount)

    def update_N(self, amount):
        self.move((0, amount))

    def update_S(self, amount):
        self.move((0, -amount))

    def update_E(self, amount):
        self.move((amount, 0))

    def update_W(self, amount):
        self.move((-amount, 0))

    def update_R(self, amount):
        self.rotate(amount)

    def update_L(self, amount):
        self.rotate(-amount)

    def update_F(self, amount):
        ux, uy = self.directions[self.direction]
        self.move((ux * amount, uy * amount))

    def move(self, vector):
        x, y = self.position
        vx, vy = vector
        self.position = x + vx, y + vy

    def rotate(self, amount):
        self.direction = (self.direction + amount // 90) % len(self.directions)

    @property
    def manhattan(self):
        x, y = self.position
        return abs(x) + abs(y)

def main():
    actions = get_actions(read_input())
    ship = Ship()
    for action in actions:
        ship.update(action)

    print(ship.manhattan)


if __name__ == "__main__":
    main()

