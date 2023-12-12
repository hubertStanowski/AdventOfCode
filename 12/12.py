import os
import sys
from functools import cache


def main():
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        data = f.read().splitlines()
        for i, row in enumerate(data):
            data[i] = row.split(" ")
            data[i][1] = tuple(map(int, data[i][1].split(",")))
        combinations_1 = [is_valid(spring, counts) for spring, counts in data]
        part1 = sum(combinations_1)

        for i, row in enumerate(data):
            data[i][0] += ("?" + data[i][0]) * 4
            data[i][1] *= 5
        combinations_2 = [is_valid(spring, counts) for spring, counts in data]
        part2 = sum(combinations_2)

        print(part1)
        print(part2)


@cache
def is_valid(spring, counts):
    spring = spring.lstrip('.')
    if len(spring) == 0:
        return int(counts == ())
    if len(counts) == 0:
        return int(spring.find("#") == -1)

    if spring[0] == "#":
        if len(spring) < counts[0] or "." in spring[:counts[0]]:
            return int(False)
        elif len(spring) == counts[0]:
            return int(len(counts) == 1)
        elif spring[counts[0]] == "#":
            return int(False)
        else:
            return is_valid(spring[counts[0] + 1:], counts[1:])

    return is_valid("#"+spring[1:], counts) + is_valid(spring[1:], counts)


if __name__ == "__main__":
    main()
