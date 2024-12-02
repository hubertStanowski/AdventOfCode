import os
import sys


def main():
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        history = f.read().split("\n")
        part1 = 0
        part2 = 0
        for i in range(len(history)):
            history[i] = list((map(int, history[i].split())))
            part1 += get_next(history[i])
            part2 += get_prev(history[i])

    print(part1)
    print(part2)


def get_differences(sequence):
    differences = [0] * (len(sequence) - 1)
    for i in range(len(sequence) - 1):
        differences[i] = sequence[i+1] - sequence[i]

    return differences


def extrapolate(sequence):
    result = [sequence]
    while set(result[-1]) != set([0]):
        result.append(get_differences(result[-1]))

    return result


def get_next(sequence):
    data = extrapolate(sequence)
    result = 0
    for i in range(len(data)-1, -1, -1):
        result += data[i][-1]

    return result


def get_prev(sequence):
    data = extrapolate(sequence)
    current_diff = 0
    for i in range(len(data)-2, 0, -1):
        current_diff = data[i][0] - current_diff
    result = sequence[0] - current_diff

    return result


if __name__ == "__main__":
    main()
