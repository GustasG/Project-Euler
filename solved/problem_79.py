from typing import Optional
from collections import defaultdict, deque

from shared.paths import RESOURCE_DIR


def read_file(path) -> list[str]:
    with open(path, 'r') as f:
        return [line.strip()
                for line in f]


def create_graph(keylog: list[str]) -> dict[str, set[str]]:
    graph = defaultdict(set)

    for attempt in keylog:
        for i, j in zip(attempt[:-1], attempt[1:]):
            graph[i].add(j)

    return graph


def unique_digits(keylog: list[str]) -> set[str]:
    digits = set()

    for attempt in keylog:
        digits.update(list(attempt))

    return digits


def guess_passcode(start: str, graph: dict[str, set[str]], digits: set[str]) -> Optional[str]:
    queue = deque([(start, [start])])

    while queue:
        curr, path = queue.popleft()
        neighbours = graph.get(curr, [])

        for neighbour in neighbours:
            new_path = path + [neighbour]

            if set(new_path) == digits:
                return ''.join(new_path)

            queue.append((neighbour, new_path))


def main() -> None:
    keylog = read_file(RESOURCE_DIR / 'problem_79_keylog.txt')
    graph = create_graph(keylog)
    digits = unique_digits(keylog)

    for vertex in graph:
        if guess := guess_passcode(vertex, graph, digits):
            print(guess)


if __name__ == '__main__':
    main()
