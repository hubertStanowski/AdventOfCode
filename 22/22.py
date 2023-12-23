import os
import sys


def main():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        data = f.read().splitlines()

    part1 = 0
    part2 = 0

    bricks = get_bricks(data)
    dropped, _ = drop_bricks(bricks)

    for i in range(len(dropped)):
        without = dropped.copy()
        without.pop(i)
        _, count_fell = drop_bricks(without)
        if count_fell == 0:
            part1 += 1
        part2 += count_fell

    print(part1)
    print(part2)


def get_bricks(data):
    bricks = []
    for line in data:
        start, end = line.split("~")
        start = tuple(int(n) for n in start.split(","))
        end = tuple(int(n) for n in end.split(","))

        cubes = [start, end]
        for i in range(2):
            if start[i] != end[i]:
                for j in range(min(start[i], end[i]) + 1, max(start[i], end[i])):
                    to_add = list(start)
                    to_add[i] = j
                    cubes.append(tuple(to_add))
                break

        bricks.append(cubes)

    return sorted(bricks, key=lambda bricks: min(
        brick[2] for brick in bricks))


def drop_bricks(bricks):
    settled = set()
    final_bricks = []
    count_fell = 0
    for brick in bricks:
        moved = False
        while True:
            next = []
            for x, y, z in brick:
                next.append((x, y, z - 1))

            if any((current[2] == 0 or (current in settled)) for current in next):
                break
            else:
                brick = next
                moved = True

        for cube in brick:
            settled.add(cube)

        final_bricks.append(brick)

        if moved:
            count_fell += 1

    return final_bricks, count_fell


if __name__ == "__main__":
    main()
