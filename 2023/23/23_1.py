import os
import sys

sys.setrecursionlimit(9999)
DIRECTIONS = {
    "^": [(-1, 0)],
    ">": [(0, 1)],
    "v": [(1, 0)],
    "<": [(0, -1)],
    ".": [(1, 0), (-1, 0), (0, 1), (0, -1)]
}
part1 = 0


def main():
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        grid = list(map(list, f.read().splitlines()))

        dfs((0, 1), [], set(), grid)

        print(part1)


def get_neighbours(current, grid):
    cx, cy = current
    length, width = len(grid), len(grid[0])

    neighbours = []
    for direction in DIRECTIONS[grid[cx][cy]]:
        dx, dy = direction
        nx, ny = cx + dx, cy + dy
        if nx in range(length) and ny in range(width) and grid[nx][ny] != "#":
            neighbours.append((nx, ny))

    return neighbours


def dfs(current, path, pathset, grid):
    global part1
    length, width = len(grid), len(grid[0])

    if current == (length - 1, width - 2):
        part1 = max(part1, len(path))
    for neighbour in get_neighbours(current, grid):
        if neighbour not in pathset:
            path.append(neighbour)
            pathset.add(neighbour)

            dfs(neighbour, path, pathset, grid)

            pathset.remove(neighbour)
            path.pop(-1)


if __name__ == "__main__":
    main()
