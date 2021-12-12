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
        self.map[frm].add(to)
        self.map[to].add(frm)

    def traversals(self):
        nodes = set(self.map)
        nodes.discard("start")
        traversals = [Traversal(self.map, nodes, "start")]
        while traversals:
            traversal = traversals.pop()
            for next in traversal.advances():
                if next.finished:
                    yield next
                elif next.dead:
                    pass
                else:
                    traversals.append(next)

class Traversal:
    def __init__(self, map, nodes, node):
        self.map = map
        self.nodes = nodes
        self.node = node

    def advances(self):
        for next in self.map[self.node] & self.nodes:
            nodes = set(self.nodes)
            if next.islower():
                nodes.discard(next)
            yield Traversal(self.map, nodes, next)

    @property
    def dead(self):
        return not self.map[self.node] & self.nodes

    @property
    def finished(self):
        return self.node == "end"

def load_edges(lines):
    for line in lines:
        yield line.strip().split("-")

if __name__ == "__main__":
    main()
