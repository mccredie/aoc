import sys

def read_input():
    for line in sys.stdin:
        yield line.strip()

def get_actions(lines):
    for line in lines:
        yield line[0], int(line[1:])

class Waypoint:
    def __init__(self, position):
        self.position = position

    def move(self, vector):
        x, y = self.position
        vx, vy = vector
        self.position = x + vx, y + vy

    def rotate(self, amount):
        amount %= 360
        for _ in range(amount // 90):
            x, y = self.position
            self.position = y, -x

class Ship:
    position = 0, 0
    def __init__(self):
        self.waypoint = Waypoint((10, 1))

    def update(self, command):
        action, amount = command
        f = getattr(self, f'update_{action}')
        f(amount)

    def update_N(self, amount):
        self.waypoint.move((0, amount))

    def update_S(self, amount):
        self.waypoint.move((0, -amount))

    def update_E(self, amount):
        self.waypoint.move((amount, 0))

    def update_W(self, amount):
        self.waypoint.move((-amount, 0))

    def update_R(self, amount):
        self.waypoint.rotate(amount)

    def update_L(self, amount):
        self.waypoint.rotate(-amount)

    def update_F(self, amount):
        ux, uy = self.waypoint.position
        x, y = self.position
        vx = ux * amount
        vy = uy * amount
        self.position = x + vx, y + vy

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

