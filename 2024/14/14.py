import os
from math import prod
from collections import deque
from collections import defaultdict


def load_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(current_dir, 'input.txt')

    data = []
    with open(input_path) as f:
        for line in f.read().split("\n"):
            # curr = line.split(' ')
            # robot = {}
            # robot["p"] = list(map(int, curr[0].replace("p=", "").split(",")))
            # robot["v"] = list(map(int, curr[1].replace("v=", "").split(",")))
            # data.append(robot)
            # print(robot)
            data.append(line)

    return data


def full(data):
    def get_next_pos(x, y, dx, dy, w, h, seconds):
        x2 = (x + dx * seconds) % w
        y2 = (y + dy * seconds) % h
        x = x2 if x2 >= 0 else x2 + w
        y = y2 if y2 >= 0 else y2 + h
        return (x, y)

    def get_quadrant(x, y):
        qx = x // (w // 2)
        qy = y // (h // 2)
        quad = qx + 1 if qx < 2 else qx
        quad += 2 if qy > 0 else 0
        return quad

    w, h = 101, 103
    seconds = 100

    quad_counter = [0, 0, 0, 0]
    neighbors_counter = []
    for i in range(10000):
        neighbors = 0
        positions = set()
        for robot in data:
            pos, velocity = robot.split(" ")
            x, y = map(int, pos.replace("p=", "").split(","))
            dx, dy = map(int, velocity.replace("v=", "").split(","))
            new_x, new_y = get_next_pos(x, y, dx, dy, w, h, i + 1)
            positions.add((new_x, new_y))

            if i == seconds-1:
                if new_x == w // 2 or new_y == h // 2:
                    continue
                quad = get_quadrant(new_x, new_y)
                quad_counter[quad - 1] = quad_counter[quad - 1] + 1

        for x, y in positions:
            for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if (x2, y2) in positions:
                    neighbors += 1
        neighbors_counter.append(neighbors)

    print(f"Part 1: {prod(quad_counter)}")
    print(f"Part 2: {neighbors_counter.index(max(neighbors_counter)) + 1}")


if __name__ == "__main__":
    data = load_data()
    full(data)
