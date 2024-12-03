import os
import re

current_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(current_dir, 'input.txt')

instructions = []
with open(input_path) as f:
    for line in f:
        matches = re.findall(r'mul\((\d+),\s*(\d+)\)', line)
        for match in matches:
            instructions.append((int(match[0]), int(match[1])))

part1 = 0
for (a, b) in instructions:
    part1 += a*b

print("PART 1: ", part1)
