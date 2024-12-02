import os
import sys
from itertools import combinations


def main():
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        universe = f.read().split('\n')
        universe = [list(x) for x in universe]
        # PART 1
        galaxies = get_galaxies(universe, part=1)
        distances = [get_distance(galaxy_1, galaxy_2)
                     for galaxy_1, galaxy_2 in combinations(galaxies.values(), 2)]
        part1 = sum(distances)

        # PART 2
        galaxies = get_galaxies(universe, part=2)
        distances = [get_distance(galaxy_1, galaxy_2)
                     for galaxy_1, galaxy_2 in combinations(galaxies.values(), 2)]
        part2 = sum(distances)

        print(part1)
        print(part2)


def get_distance(point_a, point_b):
    return (abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1]))


def get_galaxies(universe, part=1):
    empty_rows, empty_columns = [], []
    for y, row in enumerate(universe):
        if row.count("#") == 0:
            empty_rows.append(y)

    for x, column in enumerate(zip(*universe)):
        if column.count("#") == 0:
            empty_columns.append(x)

    galaxy_number = 1
    galaxies = {}
    ratio = 2 if part == 1 else 1000000
    for y, row in enumerate(universe):
        for x, current in enumerate(row):
            if current == "#":
                additional_y_space = sum(
                    [ratio-1 for r in empty_rows if r < y])
                additional_x_space = sum(
                    [ratio-1 for c in empty_columns if c < x])
                galaxies[galaxy_number] = (
                    y + additional_y_space, x + additional_x_space)
                galaxy_number += 1

    return galaxies


if __name__ == "__main__":
    main()
