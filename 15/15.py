import os
import sys
from collections import defaultdict


def main():
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        data = f.read().replace("\n", "").split(",")
        boxes = {i: defaultdict(int) for i in range(256)}
        part1 = 0
        for step in data:
            part1 += hash_algorithm(step)
            initialize(step, boxes)

        part2 = get_focusing_power(boxes)

        print(part1)
        print(part2)


def hash_algorithm(input):
    current_value = 0
    for ch in input:
        current_value += ord(ch)
        current_value *= 17
        current_value %= 256

    return current_value


def initialize(step, boxes):
    if "-" in step:
        label, _ = step.split("-")
        box_id = hash_algorithm(label)
        if label in boxes[box_id]:
            del boxes[box_id][label]
    else:
        label, focal_length = step.split("=")
        box_id = hash_algorithm(label)
        boxes[box_id][label] = int(focal_length)


def get_focusing_power(boxes):
    focusing_power = 0
    for box in boxes:
        slot = 1
        for focal_length in boxes[box].values():
            focusing_power += (box+1) * slot * focal_length
            slot += 1

    return focusing_power


if __name__ == "__main__":
    main()
