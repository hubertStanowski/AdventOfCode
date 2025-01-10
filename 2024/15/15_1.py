import os
from collections import deque
from collections import defaultdict

dirs = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}


def load_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(current_dir, 'input.txt')

    grid, moves = [], ""
    with open(input_path) as f:
        grid_data, move_data = f.read().split('\n\n')
        for line in grid_data.split("\n"):
            grid.append(list(line))

        moves = "".join(move_data).replace("\n", "")

    return grid, moves


def get_start(grid):
    for r, row in enumerate(grid):
        for c, curr in enumerate(row):
            if curr == '@':
                return (r, c)


def move_to(current, direction, grid):
    new_x, new_y = current[0] + direction[0], current[1] + direction[1]
    grid[new_x][new_y] = grid[current[0]][current[1]]
    grid[current[0]][current[1]] = "."


def update_current(current, direction):
    return current[0] + direction[0], current[1] + direction[1]


def evaluate_map(grid, move_data, start):
    current = start
    for move in move_data:
        direction = dirs[move]
        new_x, new_y = current[0] + direction[0], current[1] + direction[1]
        if grid[new_x][new_y] == "#":
            continue
        if grid[new_x][new_y] == ".":
            move_to(current, direction, grid)
            current = update_current(current, direction)
        if grid[new_x][new_y] == "O":
            while grid[new_x][new_y] == "O":
                new_x, new_y = new_x + direction[0], new_y + direction[1]
            if grid[new_x][new_y] == "#":
                continue
            while (new_x, new_y) != current:
                new_x, new_y = new_x - direction[0], new_y - direction[1]
                move_to((new_x, new_y), direction, grid)
            current = update_current(current, direction)


def part1(data):
    grid, move_data = data
    start = get_start(grid)
    evaluate_map(grid, move_data, start)

    result = 0
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            if grid[i][j] == "O":
                result += 100*i + j

    return result


if __name__ == "__main__":
    data = load_data()
    print("Part 1:", part1(data))
