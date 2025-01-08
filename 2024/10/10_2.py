import os
from collections import deque

current_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(current_dir, 'input.txt')


data = []
with open(input_path) as f:
    for line in f.read().split('\n'):
        data.append([int(digit) for digit in line])

starts = set()

for r, col in enumerate(data):
    for c, curr in enumerate(col):
        if curr == 0:
            starts.add((r, c))

# print(starts)


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


def bfs(start):
    queue = deque([start])
    # visited = set(start)
    result = 0
    while queue:
        curr_r, curr_c = queue.popleft()
        if data[curr_r][curr_c] == 9:
            result += 1
        neighbors = get_neighbors(curr_r, curr_c)
        for nr, nc in neighbors:
            if data[nr][nc] == data[curr_r][curr_c] + 1 and (nr, nc):
                queue.append((nr, nc))

    return result


part2 = 0
for start in starts:
    part2 += bfs(start)

print("PART 2: ", part2)
