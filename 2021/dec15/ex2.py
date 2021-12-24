import sys
from collections import defaultdict
import heapq


def main():
    map = read_risk_map(sys.stdin)
    risk = map.find_least_risk()
    print(risk)


def read_risk_map(lines):
    map = Map()
    for y, line in enumerate(lines):
        line = line.strip()
        for x, risk in enumerate(line):
            map.add_risk((x, y), int(risk))
    return map

INF = float("inf")
def search(weights, start, target):
    frontier = [(0, start)]
    explored = set()
    cost = {start: 0}
    while True:
        nw, node = heapq.heappop(frontier)
        if node == target:
            return cost[node]
        explored.add(node)
        for n in neighbors(weights.keys(), node):
            w = nw + weights[n]
            if n not in explored and n not in cost:
                heapq.heappush(frontier, (w, n))
                cost[n] = w
            elif n in frontier and cost.get(n, INF) > w:
                cost[n] = w


def neighbors(available, coord):
    return available & set(adjacent(coord))


def adjacent(coord):
    x, y = coord
    yield x - 1,  y
    yield x + 1,  y
    yield x,  y - 1
    yield x,  y + 1


class Map:
    def __init__(self):
        self.risk = {}

    def add_risk(self, coord, risk):
        self.risk[coord] = risk

    def find_least_risk(self):
        x, y = max(self.risk)
        dx, dy = x + 1, y + 1
        weights = {}
        for i in range(5):
            for j in range(5):
                for x, y in self.risk:
                    risk = (self.risk[x, y] - 1 + i + j) % 9 + 1
                    weights[x + dx * i, y + dy * j] =  risk
        target = dx * 5 - 1, dy *  5 - 1
        return search(weights, (0, 0), target)


if __name__ == "__main__":
    main()
