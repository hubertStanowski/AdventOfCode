import os
import re

current_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(current_dir, 'input.txt')

instructions = []
with open(input_path) as f:
    valid_sections = []
    between_donts = f.read().split('don\'t()')
    # first section is always valid as there is no "don't" at the beginning
    valid_sections.append(between_donts[0])
    for section in between_donts:
        if "do()" in section:
            first_do = section.index("do()")
            # valid instructions are after the first "do()"
            valid_sections.append(section[first_do:])

    for section in valid_sections:
        matches = re.findall(r'mul\((\d+),\s*(\d+)\)', section)
        for match in matches:
            instructions.append((int(match[0]), int(match[1])))

part2 = 0
for (a, b) in instructions:
    part2 += a*b

print("PART 2: ", part2)
