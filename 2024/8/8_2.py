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

    offset = (x1 - option1[0], y1 - option1[1])
    # offset2 = (x2 - option2[0], y2 - option2[1])

    antinodes = set()

    curr = list(node1)
    while valid(curr):
        antinodes.add(tuple(curr))
        curr[0] += offset[0]
        curr[1] += offset[1]

    curr = list(node1)
    while valid(curr):
        antinodes.add(tuple(curr))
        curr[0] -= offset[0]
        curr[1] -= offset[1]

    curr = list(node2)
    while valid(curr):
        antinodes.add(tuple(curr))
        curr[0] += offset[0]
        curr[1] += offset[1]

    curr = list(node2)
    while valid(curr):
        antinodes.add(tuple(curr))
        curr[0] -= offset[0]
        curr[1] -= offset[1]

    return antinodes


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

print("PART 2: ", len(part1))
