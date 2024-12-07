import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(current_dir, 'input.txt')

grid = []
with open(input_path) as f:
    grid = f.read().split()
    for i in range(len(grid)):
        grid[i] = list(grid[i])  # for printing


# directions relative to observer
def turn(direction):
    # going down -> going left
    if direction == (1, 0):
        return (0, -1)
    # going up -> going right
    elif direction == (-1, 0):
        return (0, 1)
    # going right -> going down
    elif direction == (0, 1):
        return (1, 0)
    # going left -> going up
    elif direction == (0, -1):
        return (-1, 0)


def move(curr, direction, grid):
    dr, dc = direction
    try:
        if grid[curr[0]+dr][curr[1]+dc] == '#':
            direction = turn(direction)
            return curr, direction, 1
        else:
            curr = (curr[0]+dr, curr[1]+dc)
    except IndexError:
        return curr, direction, 4

    return curr, direction, 0


def get_starting_pos(grid):
    for r, row in enumerate(grid):
        if '^' in row:
            return r, row.index('^')


def print_grid(grid):
    for row in grid:
        print("".join(row))
    print()


def get_visited(grid):
    staleness = 0
    curr = get_starting_pos(grid)
    direction = (-1, 0)
    visited = set([curr])

    # if it gets surrounded from 3 sides by obstacles and can only go back the way it came -> return
    while staleness < 3:
        curr, direction, staleness_diff = move(curr, direction, grid)
        if staleness_diff == 0:
            staleness = 0
        staleness += staleness_diff
        visited.add(curr)

    return visited


visited = get_visited(grid)
part1 = len(visited)
print("PART 1: ", part1)
