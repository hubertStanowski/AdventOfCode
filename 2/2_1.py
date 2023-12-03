import os
import sys

with open(os.path.join(sys.path[0], "input.txt")) as f:
    lines = f.readlines()
    result = 0
    for line in lines:
        id, sets = line.split(":")
        id = int(id[5:])
        sets = sets.split(";")
        sets = [x.split(",") for x in sets]
        valid = True
        for set in sets:
            counts = {
                "red": 0,
                "blue": 0,
                "green": 0
            }
            for current in set:
                count, color = current.split(" ")[1:]
                color = color.replace("\n", "")
                counts[color] += int(count)
            # print(id)
            # print(counts)
            if counts["red"] > 12 or counts["green"] > 13 or counts["blue"] > 14:
                valid = False

        if valid:
            result += id

print(result)
