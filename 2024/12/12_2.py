import os
from collections import deque


current_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(current_dir, 'input.txt')

data = []
with open(input_path) as f:
    for line in f.read().split('\n'):
        data.append(line)


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


def get_sides(row, col):
    d_r = [-1, 0, 1, 0]
    d_c = [0, 1, 0, -1]
    sides = 0
    curr = data[row][col]
    for i in range(4):
        nr = row + d_r[i]
        nc = col + d_c[i]
        if not valid(nr, nc) or data[nr][nc] != curr:
            nr_90 = row + d_r[(i - 1) % 4]
            nc_90 = col + d_c[(i - 1) % 4]
            begining = not valid(
                nr_90, nc_90) or data[nr_90][nc_90] != curr

            nr_corner = nr + d_r[(i - 1) % 4]
            nc_corner = nc + d_c[(i - 1) % 4]
            concave = valid(
                nr_corner, nc_corner) and data[nr_corner][nc_corner] == curr

            if begining or concave:
                sides += 1

    return sides


visited = set()


def bfs(start):
    queue = deque([start])
    area = 0
    sides = 0
    while queue:
        r, c = queue.popleft()
        visited.add((r, c))
        neighbors = get_neighbors(r, c)
        area += 1
        sides += get_sides(r, c)
        for nr, nc in neighbors:
            if not (nr, nc) in visited and data[nr][nc] == data[r][c]:
                queue.append((nr, nc))
                visited.add((nr, nc))

    return area, sides


part2 = 0

for r, row in enumerate(data):
    for c, curr in enumerate(row):
        if (r, c) not in visited:
            area, perimeter = bfs((r, c))
            # print(curr, area, perimeter)
            part2 += area * perimeter

print("PART 2: ", part2)
