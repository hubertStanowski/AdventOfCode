import os
import math
from collections import deque
from collections import defaultdict


def load_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(current_dir, 'input.txt')

    data = []
    with open(input_path) as f:
        for curr in f.read().split("\n\n"):
            data.append(curr.split('\n'))

    return data


def process_data(data):
    def convert(curr):
        cols = list(map(list, zip(*curr[1:-1])))
        pins = []
        for i in range(len(cols)):
            pins.append(cols[i].count('#'))

        return pins

    keys = []
    locks = []
    for curr in data:
        pins = convert(curr)
        if curr[0] == "#####":
            locks.append(pins)
        else:
            keys.append(pins)

    return keys, locks


def match(key, lock):
    for i in range(len(key)):
        if key[i] + lock[i] > 5:
            return False

    return True


def part1(data):
    result = 0
    keys, locks = process_data(data)

    for lock in locks:
        for key in keys:
            if match(key, lock):
                result += 1

    return result


def part2(data):
    result = "NO PART 2"
    return result


if __name__ == "__main__":
    data = load_data()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
