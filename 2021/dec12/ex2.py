import sys
from collections import defaultdict

def main():
    cave = Cave()
    for edge in load_edges(sys.stdin):
        cave.add_edge(edge)

    for i, _ in enumerate(cave.traversals()):
        pass

    print(i + 1)

class Cave:
    def __init__(self):
        self.map = defaultdict(set)

    def add_edge(self, edge):
        frm, to = edge
        if to != "start" and frm != "end":
            self.map[frm].add(to)
        if frm != "start" and to != "end":
            self.map[to].add(frm)

    def traversals(self):
        traversals = [Traversal(self.map, set(), ["start"])]
        while traversals:
            traversal = traversals.pop()
            for next in traversal.advances():
                if next.finished:
                    yield next
                elif not next.alive:
                    pass
                else:
                    traversals.append(next)

class Traversal:
    def __init__(self, map, visited, path, twice=False):
        self.map = map
        self.visited = visited
        self.path = path
        self.twice = twice

    def advances(self):
        node = self.path[-1]
        to_visit = self.map[node]
        if self.twice:
            to_visit = to_visit - self.visited
        for next in to_visit:
            twice = self.twice
            visited = set(self.visited)
            if next.islower():
                twice = twice or next in visited
                visited.add(next)
            yield Traversal(self.map, visited, self.path + [next], twice)

    @property
    def alive(self):
        next = set(self.map[self.path[-1]])
        if self.twice:
            next -= self.visited
        return bool(next)

    @property
    def finished(self):
        return "end" in self.visited

    def __str__(self):
        return ",".join(self.path)


def load_edges(lines):
    for line in lines:
        yield line.strip().split("-")


if __name__ == "__main__":
    main()
