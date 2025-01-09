import os
from collections import deque


current_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(current_dir, 'input.txt')


def valid(r, c):
    return 0 <= r < len(data) and 0 <= c < len(data[0])


def get_neighbors(r, c):
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    neighbors = []
    for dr, dc in dirs:
        new_r, new_c = r+dr, c+dc
        if valid(new_r, new_c):
            neighbors.append((new_r, new_c))

    return neighbors


def border_count(r, c, neighbors):
    count = 4
    for nr, nc in neighbors:
        if data[nr][nc] == data[r][c]:
            count -= 1

    return count


data = []
with open(input_path) as f:
    for line in f.read().split('\n'):
        data.append(line)


visited = set()


def bfs(start):
    queue = deque([start])
    area = 0
    perimeter = 0
    while queue:
        r, c = queue.popleft()
        visited.add((r, c))
        neighbors = get_neighbors(r, c)
        area += 1
        perimeter += border_count(r, c, neighbors)
        for nr, nc in neighbors:
            if not (nr, nc) in visited and data[nr][nc] == data[r][c]:
                queue.append((nr, nc))
                visited.add((nr, nc))

    return area, perimeter


part1 = 0

for r, row in enumerate(data):
    for c, curr in enumerate(row):
        if (r, c) not in visited:
            area, perimeter = bfs((r, c))
            # print(curr, area, perimeter)
            part1 += area * perimeter

print("PART 1: ", part1)
