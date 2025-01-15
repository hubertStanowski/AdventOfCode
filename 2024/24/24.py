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
        initial, gates = {}, []
        for line in data[0].split('\n'):
            id, val = line.split(": ")
            initial[id] = int(val)
        for line in data[1].split('\n'):
            line = line.strip().replace("->", "").split()
            gates.append(line)

    data = [initial, gates]

    return data


def part1(data):
    def calc(gate):
        if gate[1] == "OR":
            return values[gate[0]] or values[gate[2]]
        elif gate[1] == "AND":
            return values[gate[0]] and values[gate[2]]
        else:
            return values[gate[0]] ^ values[gate[2]]
    result = 0
    values, gates = data
    done = False
    while not done:
        done = True
        for gate in gates:
            if gate[3] not in values:
                if gate[0] in values and gate[2] in values:
                    values[gate[3]] = calc(gate)
                else:
                    done = False

    z_keys = sorted([key for key in values.keys()
                    if key.startswith('z')], reverse=True)
    result = ''.join(map(str, [values[key] for key in z_keys]))
    # print(result)

    return int(result, 2)


def part2(data):
    result = 0
    # Couldn't do part 2
    return result


if __name__ == "__main__":
    data = load_data()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
