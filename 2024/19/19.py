import os
import math
from collections import deque
from collections import defaultdict


def load_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(current_dir, 'input.txt')

    data = []
    with open(input_path) as f:
        data = f.read().split("\n\n")
        data[0] = data[0].split(", ")
        data[1] = data[1].split("\n")
    return data


def match(current, available, target):
    if current == target:
        return True
    if current != target[:len(current)]:
        return False
    for option in available:
        if match(current+option, available, target):
            return True
    return False


def part1(data):
    result = 0
    available, targets = data
    for target in targets:
        result += match("", available, target)
    return result


def part2(data):
    result = 0
    available, targets = data
    for target in targets:
        dp = [0] * (len(target) + 1)
        for i in range(1, len(target) + 1):
            for j in range(i):
                for option in available:
                    if j + len(option) == i and option == target[j:i]:
                        if j == 0:
                            dp[i] += 1
                        else:
                            dp[i] += dp[j]
        result += dp[-1]
    return result


if __name__ == "__main__":
    data = load_data()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
