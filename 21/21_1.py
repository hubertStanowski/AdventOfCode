import os
import sys
from queue import deque


def main():
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        grid = list(map(list, f.read().splitlines()))

    for r, row in enumerate(grid):
        if "S" in row:
            start = (r, row.index("S"))

    part1 = len(bfs(grid, start))
    print(part1)


def bfs(grid, start, limit=64):
    width = len(grid[0])
    height = len(grid)

    queue = deque()
    queue.append((*start, 0))

    valid = set()
    visited = set()

    while queue:
        x, y, steps = queue.popleft()
        if (x, y, steps) not in visited:
            visited.add((x, y, steps))
            if steps == limit:
                valid.add((x, y))
            else:
                if x >= 0:
                    if grid[y][x - 1] != "#":
                        queue.append((x - 1, y, steps + 1))
                if x < width - 1:
                    if grid[y][x + 1] != "#":
                        queue.append((x + 1, y, steps + 1))
                if y >= 0:
                    if grid[y - 1][x] != "#":
                        queue.append((x, y - 1, steps + 1))
                if y < height - 1:
                    if grid[y + 1][x] != "#":
                        queue.append((x, y + 1, steps + 1))

    return valid


if __name__ == "__main__":
    main()
