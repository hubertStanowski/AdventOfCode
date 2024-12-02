import os
import sys


def main():
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        data = [list(row) for row in f.read().splitlines()]
        tilt(data)
        load = calculate_load(data)

        # data = ["".join(row) for row in data]
        # for row in data:
        #     print(row)
        print(load)


def tilt(data):
    for y, row in enumerate(data):
        for x, ch in enumerate(row):
            if ch == "O":
                roll(data, x, y)


def roll(data, x, y):
    while y-1 >= 0:
        if data[y-1][x] == ".":
            data[y][x] = "."
            data[y-1][x] = "O"
            y -= 1
        else:
            return


def calculate_load(data):
    result = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "O":
                result += len(data) - i

    return result


if __name__ == "__main__":
    main()
