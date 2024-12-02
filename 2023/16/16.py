import os
import sys


def main():
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        data = f.read().splitlines()

        part1 = get_energized(((0, -1), "E"), data)
        part2 = part1

        for row in range(len(data)):
            part2 = max(part2, get_energized(((row, -1), 'E'), data))
            part2 = max(part2, get_energized(((row, len(data[0])), 'W'), data))
        for col in range(len(data[0])):
            part2 = max(part2, get_energized(((-1, col), 'S'), data))
            part2 = max(part2, get_energized(((len(data), col), 'N'), data))

        print(part1)
        print(part2)


def get_energized(start, data):
    DIRECTIONS = {'E': (0, 1), 'W': (0, -1), 'N': (-1, 0), 'S': (1, 0)}
    energized = set()
    visited = set()
    stack = [start]

    while stack:
        current = stack.pop()
        if current not in visited:
            energized.add(current[0])
            direction = current[1]
            visited.add(current)
            next_coords = (current[0][0]+DIRECTIONS[direction][0],
                           current[0][1]+DIRECTIONS[direction][1])
            if next_coords[0] in range(len(data)) and next_coords[1] in range(len(data)):
                next = data[next_coords[0]][next_coords[1]]
                if next == '\\':
                    if direction in 'EN':
                        direction = 'WS'[direction == 'E']
                    elif direction in 'WS':
                        direction = 'EN'[direction == 'W']
                    stack.append((next_coords, direction))
                elif next == '/':
                    if direction in 'ES':
                        direction = 'WN'[direction == 'E']
                    elif direction in 'WN':
                        direction = 'ES'[direction == 'W']
                    stack.append((next_coords, direction))
                elif next == '|' and direction in 'EW':
                    stack.append((next_coords, 'N'))
                    stack.append((next_coords, 'S'))
                elif next == '-' and direction in 'NS':
                    stack.append((next_coords, 'E'))
                    stack.append((next_coords, 'W'))
                else:
                    stack.append((next_coords, direction))

    return len(energized)-1


if __name__ == "__main__":
    main()
