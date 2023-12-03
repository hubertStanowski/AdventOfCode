import os
import sys
from collections import defaultdict

with open(os.path.join(sys.path[0], "input.txt")) as f:
    lines = f.readlines()
    for i in range(len(lines) - 1):
        lines[i] = lines[i][:-1]

    gears = defaultdict(list)
    for i, line in enumerate(lines):
        number = ""
        symbols = set()
        for j, ch in enumerate(line):
            if ch.isdigit():
                number += ch
                for y in range(max(0, i-1), min(len(lines), i+2)):
                    for x in range(max(0, j-1), min(len(line), j+2)):
                        if not lines[y][x].isdigit() and lines[y][x] != ".":
                            symbols.add((lines[y][x], y, x))
            elif len(symbols) != 0 and number != "":
                for symbol, y, x in symbols:
                    if symbol == "*":
                        gears[(y, x)].append(int(number))
                symbols = set()
                number = ""
            else:
                symbols = set()
                number = ""

        if len(symbols) != 0 and number != "":
            for symbol, y, x in symbols:
                if symbol == "*":
                    gears[(y, x)].append(int(number))


# for line in lines:
#     print("".join(line))

result = 0
for key, values in gears.items():
    if len(values) == 2:
        result += values[0] * values[1]
print(result)
