import os
from collections import deque
from collections import defaultdict


def load_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(current_dir, 'input.txt')

    data = []
    with open(input_path) as f:
        for curr in f.read().split("\n\n"):
            curr = curr.split('\n')
            machine = {}
            machine["A"] = list(map(int, curr[0].replace(
                "Button A: X+", "").replace("Y+", "").split(", ")))
            machine["B"] = list(map(int, curr[1].replace(
                "Button B: X+", "").replace("Y+", "").split(", ")))
            machine["Prize"] = list(map(int, curr[2].replace(
                "Prize: X=", "").replace("Y=", "").split(", ")))
            data.append(machine)
    #         print(machine)

    # print(data)

    return data


def part1(data):
    result = 0
    a_cost = 3
    b_cost = 1

    for machine in data:
        a_uses, b_uses = get_target(machine)
        if a_uses.is_integer() and b_uses.is_integer():
            result += (int(a_uses) * a_cost) + (int(b_uses) * b_cost)

    return result


def part2(data):
    result = 0
    a_cost = 3
    b_cost = 1
    offset = 10000000000000

    for machine in data:
        machine["Prize"][0] += offset
        machine["Prize"][1] += offset
        a_uses, b_uses = get_target(machine)
        if a_uses.is_integer() and b_uses.is_integer():
            result += (int(a_uses) * a_cost) + (int(b_uses) * b_cost)

    return result


def get_target(machine):
    # - a_x * a + b_x * b = prize_x
    # - a_y * a + b_y * b = prize_y

    a_x_with_b_y = machine["A"][0] * machine["B"][1]
    prize_x_with_b_y = machine["Prize"][0] * machine["B"][1]

    a_y_with_b_x = machine["A"][1] * machine["B"][0]
    prize_y_with_b_x = machine["Prize"][1] * machine["B"][0]

    a = (prize_x_with_b_y - prize_y_with_b_x) / (a_x_with_b_y - a_y_with_b_x)

    b = (machine["Prize"][1] - machine["A"][1] * a) / machine["B"][1]

    return a, b


if __name__ == "__main__":
    data = load_data()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
