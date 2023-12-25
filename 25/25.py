import os
import sys
from networkx import Graph, minimum_cut
import random


def main():
    graph = Graph()
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        for line in f.read().splitlines():
            x = line.split(':')[0]
            for y in line.split(':')[1].strip().split(' '):
                graph.add_edge(x, y, capacity=1)

        part1 = get_partitions(graph)
        print(part1)


def get_partitions(graph):
    while True:
        nodes = list(graph.nodes())
        x, y = random.choices(nodes, k=2)
        if x != y:
            cut, partition = minimum_cut(graph, x, y)
            if cut == 3:
                return len(partition[0]) * len(partition[1])


if __name__ == "__main__":
    main()
