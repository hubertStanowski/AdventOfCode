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
            data.append(int(line))

    return data


PRUNE_MASK = (1 << 24) - 1


def generate(num):
    num ^= (num << 6) & PRUNE_MASK
    num ^= (num >> 5)
    num ^= (num << 11) & PRUNE_MASK
    return num


def part1(data):
    result = 0
    steps = 2000
    for num in data:
        for _ in range(steps):
            num = generate(num)
        result += num

    return result


def part2(data):
    result = defaultdict(int)
    steps = 2000
    for num in data:
        seen = set()
        diffs = []
        for i in range(steps):
            next_num = generate(num)
            diffs.append((next_num % 10) - (num % 10))
            num = next_num
            if i >= 3:
                if (sequence := tuple(diffs)) not in seen:
                    result[sequence] += num % 10
                    seen.add(sequence)
                diffs.pop(0)

    return max(result.values())


if __name__ == "__main__":
    data = load_data()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
