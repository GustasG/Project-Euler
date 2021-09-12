from typing import List
from dataclasses import dataclass

from shared.paths import RESOURCE_DIR


@dataclass(frozen=True)
class Edge:
    src: int
    dest: int
    weight: int


def find(parent: List[int], x: int) -> int:
    while x != parent[x]:
        x = parent[x]
    return x


def union(parent: List[int], rank: List[int], edge: Edge) -> None:
    rx = find(parent, edge.src)
    ry = find(parent, edge.dest)

    if rx == ry:
        return

    if rank[rx] > rank[ry]:
        parent[ry] = rx
    else:
        parent[rx] = ry

        if rank[rx] == rank[ry]:
            rank[ry] += 1


def kruskal(graph: List[Edge], vertices: int) -> List[Edge]:
    graph = sorted(graph, key=lambda item: item.weight)

    parent = [i for i in range(vertices + 1)]
    rank = [0 for _ in range(vertices + 1)]

    a = []

    for edge in graph:
        if find(parent, edge.src) != find(parent, edge.dest):
            a.append(edge)
            union(parent, rank, edge)
    return a


def read_file(path: str) -> List[Edge]:
    with open(path, 'r') as f:
        return [Edge(i, j, int(weight))
                for i, line in enumerate(f)
                for j, weight in enumerate(line.rstrip().split(','))
                if weight.isnumeric()]


def find_max_saving(graph: List[Edge], vertices: int) -> int:
    tree = kruskal(graph, vertices)

    start_weight = sum(edge.weight for edge in graph) // 2
    final_weight = sum(edge.weight for edge in tree)

    return start_weight - final_weight


def main():
    graph = read_file(RESOURCE_DIR / 'problem_107_network.txt')
    vertices = 40
    savings = find_max_saving(graph, vertices)

    print(savings)


if __name__ == "__main__":
    main()
