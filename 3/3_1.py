import os
import sys

with open(os.path.join(sys.path[0], "input.txt")) as f:
    result = 0
    lines = f.readlines()
    for i in range(len(lines) - 1):
        lines[i] = lines[i][:-1]

    for i, line in enumerate(lines):
        number = ""
        valid = False
        for j, ch in enumerate(line):
            if ch.isdigit():
                number += ch
                for y in range(max(0, i-1), min(len(lines), i+2)):
                    for x in range(max(0, j-1), min(len(line), j+2)):
                        if not lines[y][x].isdigit() and lines[y][x] != ".":
                            valid = True
            else:
                if valid and number != "":
                    result += int(number)
                valid = False
                number = ""
        if valid and number != "":
            result += int(number)

# for line in lines:
#     print("".join(line))

print(result)
