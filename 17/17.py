import os
import sys
from heapq import heappush, heappop


def main():
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        grid = [list(map(int, line)) for line in f.read().splitlines()]

        part1 = dijkstra(grid, ultra=False)
        part2 = dijkstra(grid, ultra=True)

        print(part1)
        print(part2)


def neighbours(grid, current, ultra=False):
    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    if ultra:
        MAX_MOVES = 10
    else:
        MAX_MOVES = 3

    if ultra:
        MIN_MOVES = 4
    else:
        MIN_MOVES = None

    height = len(grid)
    width = len(grid[0])
    y, x, direction, direction_moves = current

    result = []

    for new_direction in DIRECTIONS:
        new_y, new_x = y + new_direction[0], x + new_direction[1]

        if not (new_y >= 0 and new_x >= 0 and new_y < height and new_x < width):
            continue

        if direction == new_direction:
            new_direction_moves = direction_moves + 1
        else:
            new_direction_moves = 1

        if new_direction_moves > MAX_MOVES:
            continue

        if MIN_MOVES and direction != new_direction and direction_moves < MIN_MOVES:
            continue

        if (new_direction[0] * -1, new_direction[1] * -1) == direction:
            continue

        result.append((new_y, new_x, new_direction, new_direction_moves))

    return result


def dijkstra(maze, ultra=False):
    height = len(maze)
    width = len(maze[0])
    START = (0, 0)
    END = (height - 1, width - 1)

    distances = {}
    heap = []

    for direction in [(0, 1), (1, 0)]:
        heappush(heap, (0, (*START, direction, 0)))

    while heap:
        cost, curr = heappop(heap)
        if curr in distances:
            continue

        distances[curr] = cost

        for neighbour in neighbours(maze, curr, ultra):
            if neighbour not in distances or new_cost < distances[curr]:
                new_cost = cost + maze[neighbour[0]][neighbour[1]]
                heappush(heap, (new_cost, neighbour))

    valid = []
    for (y, x, direction, direction_moves), cost in distances.items():
        if (y, x) == END and (not ultra or direction_moves >= 4):
            valid.append(cost)

    return min(valid)


if __name__ == "__main__":
    main()
