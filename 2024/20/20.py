import os
import math
from collections import deque
from collections import defaultdict


DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def load_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(current_dir, 'input.txt')

    data = []
    with open(input_path) as f:
        for line in f.read().split('\n'):
            data.append(list(line))

    return data


def bfs(grid):
    def valid(r, c):
        return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and (r, c) not in visited and grid[r][c] != '#'
    grid = data
    m, n = len(grid), len(grid[0])
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'S':
                start = (row, col)
            elif grid[row][col] == 'E':
                end = (row, col)

    queue = deque([(*start, 0, dict())])
    while queue:
        r, c, time, visited = queue.popleft()
        visited[(r, c)] = time

        if (r, c) == end:
            break

        for dr, dc in DIRECTIONS:
            i = r + dr
            j = c + dc
            if valid(i, j):
                queue.append((i, j, time + 1, visited.copy()))

    return visited


def part1(data):
    visited = bfs(data)
    result = 0
    threshold = 102
    for (r, c), time in visited.items():
        for dr, dc in DIRECTIONS:
            i = r + 2*dr
            j = c + 2*dc
            if visited.get((i, j), 0) - time >= threshold:
                result += 1

    return result


def part2(data):
    visited = bfs(data)

    result = 0
    threshold = 100
    path = sorted(visited, key=visited.get)
    for t2 in range(threshold, len(path)):
        for t1 in range(t2 - threshold):
            x1, y1 = path[t1]
            x2, y2 = path[t2]
            distance = abs(x1-x2) + abs(y1-y2)
            if distance <= 20 and t2 - t1 - distance >= threshold:
                result += 1

    return result


if __name__ == "__main__":
    data = load_data()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
