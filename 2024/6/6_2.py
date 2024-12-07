import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(current_dir, 'input.txt')

grid = []
with open(input_path) as f:
    grid = f.read().split()
    for i in range(len(grid)):
        grid[i] = list(grid[i])  # for printing


def get_starting_pos(grid):
    for r, row in enumerate(grid):
        if '^' in row:
            return r, row.index('^')


def print_grid(grid):
    for row in grid:
        print("".join(row))
    print()


def valid_pos(grid, pos):
    return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])


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


def get_obstacles(grid):
    obstacles = set()
    for i, row in enumerate(grid):
        for j, curr in enumerate(row):
            if curr == '#':
                obstacles.add((i, j))

    return obstacles


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


def detect_loop(obstacles, start):
    seen = {(start, 0)}
    pos = start
    d = (-1, 0)
    while True:
        new_pos = (pos[0] + d[0], pos[1] + d[1])
        if new_pos in obstacles:
            d = turn(d)
            continue
        if not valid_pos(grid, new_pos):
            return False
        if (new_pos, d) in seen:
            return True
        seen.add((new_pos, d))
        pos = new_pos


starting_pos = get_starting_pos(grid)
obstacles = get_obstacles(grid)
visited = get_visited(grid)

part2 = 0
for p in visited:
    if p in obstacles or p == starting_pos:
        continue
    if detect_loop(obstacles | {p}, starting_pos):
        part2 += 1

print("PART 2: ", part2)
