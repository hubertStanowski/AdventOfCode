import os
import sys


def main():
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        data = f.read().split("\n\n")
        data = [pattern.split("\n") for pattern in data]

        part1 = (sum([get_value(pattern, 0) for pattern in data]))
        part2 = (sum([get_value(pattern, 1) for pattern in data]))

        print(part1)
        print(part2)


def get_distance(left, right):
    return sum([ch1 != ch2 for (ch1, ch2) in zip(left, right)])


def transpose(matrix):
    return ["".join(x) for x in zip(*matrix)]


def get_horizontal_value(pattern, distance):
    result = 0
    for i in range(len(pattern) - 1):
        total = 0
        for row1, row2 in zip(pattern[i + 1:], pattern[i::-1]):
            total += get_distance(row1, row2)
        if total == distance:
            result += i + 1
    return result


def get_value(pattern, distance):
    rows = get_horizontal_value(pattern, distance) * 100
    columns = get_horizontal_value(transpose(pattern), distance)

    return rows + columns


if __name__ == "__main__":
    main()
