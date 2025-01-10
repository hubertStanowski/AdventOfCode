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

    new_grid = []
    current_row = 0
    for i in range(len(grid)):
        new_grid.append([])
        for j in range(len(grid[0])):
            if grid[i][j] in ["#", "."]:
                new_grid[current_row] += [grid[i][j], grid[i][j]]
            if grid[i][j] == "O":
                new_grid[current_row] += ["[", "]"]
            if grid[i][j] == "@":
                new_grid[current_row] += ["@", "."]
        current_row += 1

    return new_grid, moves


def get_start(grid):
    for r, row in enumerate(grid):
        for c, curr in enumerate(row):
            if curr == '@':
                return (r, c)


def move_to(current, direction, grid, symbol):
    new_x, new_y = current[0] + direction[0], current[1] + direction[1]
    grid[new_x][new_y] = symbol
    grid[current[0]][current[1]] = "."


def update_current(current, direction):
    return current[0] + direction[0], current[1] + direction[1]


def cords_of_next_containers(current, direction, grid):
    current_x, current_y = current[0], current[1]
    if grid[current_x + direction[0]][current_y] == "[":
        return (current_x + direction[0], current_y), (current_x + direction[0], current_y + 1)
    return (current_x + direction[0], current_y - 1), (current_x + direction[0], current_y)


def interact_with_container(current, direction, grid):
    if direction[0] == 0:
        new_x, new_y = current[0] + direction[0], current[1] + direction[1]
        while grid[new_x][new_y] in ["[", "]"]:
            new_x, new_y = new_x + direction[0], new_y + direction[1]
        if grid[new_x][new_y] == "#":
            return current
        while (new_x, new_y) != current:
            new_x, new_y = new_x - direction[0], new_y - direction[1]
            move_to((new_x, new_y), direction, grid, grid[new_x][new_y])
        return update_current(current, direction)

    linked_containers = [cords_of_next_containers(current, direction, grid)]
    index = 0

    while index < len(linked_containers):
        container = linked_containers[index]
        left_bracket, right_bracket = container[0], container[1]
        new_x_left_bracket, new_y_left_bracket = update_current(
            left_bracket, direction)
        new_x_right_bracket, new_y_right_bracket = update_current(
            right_bracket, direction)
        if (grid[new_x_left_bracket][new_y_left_bracket] == "#"
                or grid[new_x_right_bracket][new_y_right_bracket] == "#"):
            return current
        if grid[new_x_left_bracket][new_y_left_bracket] in ["[", "]"]:
            linked_containers.append(cords_of_next_containers(
                left_bracket, direction, grid))

        if grid[new_x_right_bracket][new_y_right_bracket] == "[":
            linked_containers.append(cords_of_next_containers(
                right_bracket, direction, grid))

        index += 1

    index -= 1
    while index >= 0:
        container = linked_containers[index]
        left_bracket, right_bracket = container[0], container[1]
        move_to(left_bracket, direction, grid, symbol="[")
        move_to(right_bracket, direction, grid, symbol="]")
        index -= 1
    move_to(current, direction, grid, "@")

    return update_current(current, direction)


def evaluate_map(grid, moves, start):
    current = start
    for move in moves:
        direction = dirs[move]
        new_x, new_y = current[0] + direction[0], current[1] + direction[1]
        if grid[new_x][new_y] == "#":
            continue
        if grid[new_x][new_y] == ".":
            move_to(current, direction, grid, "@")
            current = update_current(current, direction)
        if grid[new_x][new_y] in ["[", "]"]:
            current = interact_with_container(current, direction, grid)


def part2(data):
    grid, move_data = data
    start = get_start(grid)
    evaluate_map(grid, move_data, start)

    result = 0
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            if grid[i][j] == "[":
                result += 100 * i + j
    return result


if __name__ == "__main__":
    data = load_data()
    print("Part 2:", part2(data))
