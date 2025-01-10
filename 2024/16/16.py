import os
from collections import deque
from collections import defaultdict
import math


def load_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(current_dir, 'input.txt')

    data = []
    with open(input_path) as f:
        for line in f.read().split('\n'):
            data.append(list(line))

        # print(data)

    return data


directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]


def turn_right(curr_dir):
    return directions[(directions.index(curr_dir) + 1 + len(directions)) % len(directions)]


def turn_left(curr_dir):
    return directions[(directions.index(curr_dir) - 1 + len(directions)) % len(directions)]


def bfs(grid):
    queue = deque()
    start = (len(grid) - 2, 1, (0, 1), 0)
    grid[len(grid) - 2][1] = 0
    queue.append(start)

    while queue:
        curr_r, curr_c, curr_dir, curr_score = queue.popleft()

        possible = [
            (curr_dir, curr_score + 1),
            (turn_left(curr_dir), curr_score + 1001),
            (turn_right(curr_dir), curr_score + 1001)
        ]

        for new_dir, new_score in possible:
            new_x, new_y = curr_r + new_dir[0], curr_c + new_dir[1]
            if grid[new_x][new_y] == "#":
                continue

            if grid[new_x][new_y] in [".", "E"] or (isinstance(grid[new_x][new_y], int) and grid[new_x][new_y] > new_score):
                grid[new_x][new_y] = new_score
                queue.append((new_x, new_y, new_dir, new_score))

    return grid[1][len(grid[1]) - 2]


def reversed_bfs(grid):
    queue = deque()
    result = 1
    start_1 = (1, len(grid[1]) - 2, (1, 0), grid[1][len(grid[1]) - 2])
    start_2 = (1, len(grid[1]) - 2, (0, -1), grid[1][len(grid[1]) - 2])
    queue.append(start_1)
    queue.append(start_2)
    visited = set()

    while queue:
        curr_r, curr_c, curr_dir, curr_score = queue.popleft()

        allowed_directions_n_score = [
            (curr_dir, curr_score - 1),
            (turn_left(curr_dir), curr_score - 1001),
            (turn_right(curr_dir), curr_score - 1001)
        ]

        for new_dir, new_score in allowed_directions_n_score:
            new_x, new_y = curr_r + new_dir[0], curr_c + new_dir[1]
            if isinstance(grid[new_x][new_y], int) and (grid[new_x][new_y] in [new_score, new_score - 1000]) and (new_x, new_y) not in visited:
                result += 1
                queue.append((new_x, new_y, new_dir, new_score))
                visited.add((new_x, new_y))

    return result


def part1(data):
    return bfs(data)


def part2(data):
    return reversed_bfs(data)


if __name__ == "__main__":
    data = load_data()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
