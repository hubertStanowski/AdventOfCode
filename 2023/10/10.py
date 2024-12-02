import os
import sys
from queue import Queue


def main():
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        data = f.read().split("\n")

        distances = get_distances(data)
        part1 = max(distances.values())
        loop = distances.keys()
        part2 = get_enclosed_titles(data, loop)

        print(part1)
        print(part2)


def find_start(data):
    # assuming start exists
    start_x, start_y = -1, -1
    for y, line in enumerate(data):
        for x, value in enumerate(line):
            if value == "S":
                start_x, start_y = x, y
                return start_x, start_y


def get_distances(data):
    connections = {
        "|": [(0, -1), (0, 1)],
        "-": [(-1, 0), (1, 0)],
        "L": [(0, -1), (1, 0)],
        "J": [(0, -1), (-1, 0)],
        "7": [(-1, 0), (0, 1)],
        "F": [(1, 0), (0, 1)],
    }
    possible_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    start_x, start_y = find_start(data)
    loop = Queue()
    distances = {(start_x, start_y): 1}
    for x, y in possible_directions:
        current = data[start_y+y][start_x+x]

        if current in connections:
            for xc, yc in connections[current]:
                if (start_x + x + xc) == start_x and (start_y + y + yc) == start_y:
                    loop.put((start_x + x, start_y + y, 1))

    while not loop.empty():
        x, y, dist = loop.get()
        if (x, y) not in distances:
            distances[(x, y)] = dist
            for xc, yc in connections[data[y][x]]:
                loop.put((x + xc, y + yc, dist + 1))

    return distances


# Part 2 is refactored code of https://www.reddit.com/user/hi_im_new_to_this/
def get_crosses(data, loop, x, y):
    width = len(data[0])
    height = len(data)
    crosses = 0
    while x < width and y < height:
        value = data[y][x]
        if (x, y) in loop and value != "L" and value != "7":
            crosses += 1
        x += 1
        y += 1

    return crosses


def get_enclosed_titles(data, loop):
    count = 0
    for y, line in enumerate(data):
        for x, _ in enumerate(line):
            if (x, y) not in loop:
                crosses = get_crosses(data, loop, x, y)
                if crosses % 2 == 1:
                    count += 1

    return count


if __name__ == "__main__":
    main()
