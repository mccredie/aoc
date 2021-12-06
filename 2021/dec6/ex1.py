import sys
from collections import Counter

def main():
    ocean = Ocean()
    days = 80
    for fish in parse_input(sys.stdin):
        ocean.add_fish(fish)

    for _ in range(days):
        ocean.elapse_day()

    print(ocean.fish_count)

def parse_input(lines):
    for line in lines:
        for value in line.split(","):
            yield int(value)

class Ocean:
    day = 0
    def __init__(self):
        self.fish_counts = Counter()

    def add_fish(self, fish):
        self.fish_counts[fish] += 1

    def elapse_day(self):
        c = self.fish_counts.pop(self.day, 0)
        self.day += 1
        self.fish_counts[self.day + 8] += c
        self.fish_counts[self.day + 6] += c

    @property
    def fish_count(self):
        return sum(self.fish_counts.values())


if __name__ == "__main__":
    main()
