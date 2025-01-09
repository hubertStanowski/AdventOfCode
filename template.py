import os
from collections import deque
from collections import defaultdict


def load_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(current_dir, 'input.txt')

    data = []
    with open(input_path) as f:
        for line in f.read().split('\n'):
            data.append(line)

    return data


def part1(data):
    result = 0
    return result


def part2(data):
    result = 0
    return result


if __name__ == "__main__":
    data = load_data()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
