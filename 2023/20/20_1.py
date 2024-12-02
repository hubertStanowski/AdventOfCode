import os
import sys
from collections import defaultdict


def main():
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        data = {}

        for line in f.read().splitlines():
            label, destinations = line.split(' -> ')
            destinations = destinations.split(', ')

            if label == 'broadcaster':
                _type = None
            else:
                _type = label[0]
                label = label[1:]

            data[label] = (_type, destinations)

        count_low = 0
        count_high = 0

        input_map = process_destinations(data)
        memory = process_types(data, input_map)

        for _ in range(1000):
            current_counts = press_button(data, memory)
            count_low += current_counts[0]
            count_high += current_counts[1]

        part1 = count_low * count_high

        print(part1)


def process_destinations(data):
    input_map = defaultdict(list)

    for node, (_, destinations) in data.items():
        for d in destinations:
            input_map[d].append(node)

    return input_map


def process_types(data, input_map):
    memory = {}
    for node, (_type, _) in data.items():
        if _type == '%':
            memory[node] = False
        elif _type == '&':
            memory[node] = {d: False
                            for d in input_map[node]}

    return memory


def press_button(data, memory):
    todo = [(None, 'broadcaster', False)]
    count_low = count_high = 0

    while todo:
        new_todo = []

        for src, node, is_high_pulse in todo:
            if is_high_pulse:
                count_high += 1
            else:
                count_low += 1

            info = data.get(node)
            if info is None:
                continue

            _type, destinations = info
            if _type == '%':
                if is_high_pulse:
                    continue
                state = memory[node]
                memory[node] = not state
                for d in destinations:
                    new_todo.append((node, d, not state))
                continue

            if _type == '&':
                state = memory[node]
                state[src] = is_high_pulse

                if sum(state.values()) == len(state):
                    to_send = False
                else:
                    to_send = True

                for d in destinations:
                    new_todo.append((node, d, to_send))
                continue

            if _type is None:
                for d in destinations:
                    new_todo.append((node, d, is_high_pulse))
                continue

        todo = new_todo

    return count_low, count_high


if __name__ == "__main__":
    main()
