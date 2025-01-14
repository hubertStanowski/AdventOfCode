from functools import cache
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
            data.append(line)

    return data


NUMPAD = {
    '7': (0, 0), '8': (0, 1), '9': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '1': (2, 0), '2': (2, 1), '3': (2, 2),
    '0': (3, 1), 'A': (3, 2),
}


DIRPAD = {
    '^': (0, 1), 'A': (0, 2),
    '<': (1, 0), 'v': (1, 1), '>': (1, 2),
}


def create_graph(keypad, invalid_coords):
    graph = {}
    for a, (x1, y1) in keypad.items():
        for b, (x2, y2) in keypad.items():
            path = '<' * (y1 - y2) + 'v' * (x2 - x1) + \
                '^' * (x1 - x2) + '>' * (y2 - y1)
            if invalid_coords == (x1, y2) or invalid_coords == (x2, y1):
                path = path[::-1]
            graph[(a, b)] = path + 'A'
    return graph


def part1(data):
    def convert(sequence, graph):
        conversion = ''
        prev = 'A'
        for char in sequence:
            conversion += graph[(prev, char)]
            prev = char
        return conversion

    result = 0
    numpad_graph = create_graph(NUMPAD, (3, 0))
    dirpad_graph = create_graph(DIRPAD, (0, 0))

    for button_presses in data:
        conversion = convert(button_presses, numpad_graph)
        conversion = convert(conversion, dirpad_graph)
        conversion = convert(conversion, dirpad_graph)
        result += int(button_presses[:-1]) * len(conversion)

    return result


def part2(data):
    @cache
    def get_length(sequence, iterations, first_iter=False) -> int:
        if iterations == 0:
            return len(sequence)
        prev = 'A'
        total_length = 0
        graph = numpad_graph if first_iter else dirpad_graph
        for char in sequence:
            total_length += get_length(graph[(prev, char)], iterations - 1)
            prev = char
        return total_length

    result = 0
    numpad_graph = create_graph(NUMPAD, (3, 0))
    dirpad_graph = create_graph(DIRPAD, (0, 0))

    for button_presses in data:
        result += int(button_presses[:-1]) * \
            get_length(button_presses, 26, True)

    return result


if __name__ == "__main__":
    data = load_data()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
