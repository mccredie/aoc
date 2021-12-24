import sys
from collections import defaultdict


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


class Dijkstra:
    def __init__(self):
        self.weight = {}

    def add_vertex(self, coord, weight):
        self.weight[coord] = weight

    def find_path(self, source, target):
        unreached = set(self.weight)
        dist = {source: 0}
        prev = {}
        while unreached:
            u = min(dist.keys() & unreached, key=dist.get)
            unreached.remove(u)

            for v in neighbors(unreached, u):
               alt = dist[u] + self.weight[v]
               if alt < dist.get(v, float("inf")):
                   dist[v] = alt
                   prev[v] = u
            if target in dist:
                break
        return dist, prev


def neighbors(available, coord):
    return available & set(adjacent(coord))


def adjacent(coord):
    x, y = coord
    yield x - 1,  y
    yield x + 1,  y
    yield x,  y - 1
    yield x,  y + 1


class Map:
    target = 0, 0
    def __init__(self):
        self.graph = Dijkstra()

    def add_risk(self, coord, risk):
        self.graph.add_vertex(coord, risk)
        self.target = max(coord, self.target)

    def find_least_risk(self):
        dist, _ = self.graph.find_path((0, 0), self.target)
        return dist[self.target]


if __name__ == "__main__":
    main()
