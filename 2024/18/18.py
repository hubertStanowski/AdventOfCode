import heapq
import os
import math
from collections import deque
from collections import defaultdict


def load_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(current_dir, 'input.txt')

    data = []
    with open(input_path) as f:
        for line in f.read().split('\n'):
            data.append(list(map(int, line.split(","))))

    return data


def a_star_search(grid, start, end):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    close_set = set()
    came_from = {}
    gscore = {start: 0}
    fscore = {start: heuristic(start, end)}
    oheap = []

    heapq.heappush(oheap, (fscore[start], start))

    while oheap:
        current = heapq.heappop(oheap)[1]

        if current == end:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data[::-1]

        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            tentative_g_score = gscore[current] + 1

            if 0 <= neighbor[0] < len(grid):
                if 0 <= neighbor[1] < len(grid[0]):
                    if grid[neighbor[0]][neighbor[1]] == "#":
                        continue
                else:
                    continue
            else:
                continue

            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue

            if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, end)
                heapq.heappush(oheap, (fscore[neighbor], neighbor))

    return [-1]


def simulate(sim_size):
    size = 71
    grid = [['.' for _ in range(size)] for _ in range(size)]
    for i in range(sim_size):
        x, y = data[i]
        grid[y][x] = "#"
    result = a_star_search(grid, (0, 0), (size-1, size-1))
    if result[0] != -1:
        return len(result)
    else:
        return False


def part1(data):
    result = simulate(1024)

    return result


def part2(data):
    result = 0
    left, right = 0, len(data)
    while left < right:
        mid = (left + right) // 2
        if simulate(mid) == False:
            right = mid
        else:
            left = mid + 1
    return str(data[left-1][0]) + "," + str(data[left-1][1])


if __name__ == "__main__":
    data = load_data()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
