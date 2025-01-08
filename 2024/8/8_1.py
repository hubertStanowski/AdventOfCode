import os
from collections import defaultdict

current_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(current_dir, 'input.txt')


def valid(node):
    r, c = node
    return 0 <= r < len(data) and 0 <= c < len(data[0])


def get_antinodes(node1, node2):
    x1, y1 = node1
    x2, y2 = node2

    option1 = (x2 * 2 - x1, y2*2 - y1)
    option2 = (x1 * 2 - x2, y1*2 - y2)

    return option1, option2


data = []
with open(input_path) as f:
    for line in f.read().split('\n'):
        data.append(line)

antenas = defaultdict(list)
for r in range(len(data)):
    for c in range(len(data[0])):
        curr = data[r][c]
        if curr == '.':
            continue
        antenas[curr].append((r, c))

part1 = set()
for antena_type, positions in antenas.items():
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            node1 = positions[i]
            node2 = positions[j]
            antinodes = get_antinodes(node1, node2)
            for antinode in antinodes:
                if valid(antinode) and antinode not in part1:
                    part1.add(antinode)

print("PART 1: ", len(part1))
