import os
import math
from collections import deque
from collections import defaultdict


def load_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(current_dir, 'input.txt')

    data = []
    with open(input_path) as f:
        for line in f.read().split('\n'):
            data.append(line.split('-'))

    return data


def convert(data):
    graph = defaultdict(set)
    for a, b in data:
        graph[a].add(b)
        graph[b].add(a)

    return graph


def part1(data):
    graph = convert(data)
    possible = [c for c in graph if c.startswith('t')]
    result = set()

    for t in possible:
        for a in graph[t]:
            for b in graph[a]:
                if b in graph[t]:
                    result.add(tuple(sorted([t, a, b])))

    return len(result)


def part2(data):
    def bron_kerbosch(selected, possible, excluded):
        if not possible and not excluded:
            return selected

        max_clique = set()
        for v in possible.copy():
            clique = bron_kerbosch(
                selected.union({v}),
                possible.intersection(graph[v]),
                excluded.intersection(graph[v])
            )
            max_clique = max(max_clique, clique, key=len)
            possible.remove(v)
            excluded.add(v)

        return max_clique

    graph = convert(data)
    max_clique = bron_kerbosch(set(), set(graph), set())

    return ','.join(sorted(max_clique))


if __name__ == "__main__":
    data = load_data()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
