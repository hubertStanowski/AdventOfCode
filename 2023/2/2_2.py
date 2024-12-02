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
        min_counts = {
            "red": 0,
            "blue": 0,
            "green": 0
        }
        for set in sets:
            current_counts = {
                "red": 0,
                "blue": 0,
                "green": 0
            }
            for current in set:
                count, color = current.split(" ")[1:]
                color = color.replace("\n", "")
                current_counts[color] += int(count)

            min_counts["red"] = max(min_counts["red"], current_counts["red"])
            min_counts["blue"] = max(
                min_counts["blue"], current_counts["blue"])
            min_counts["green"] = max(
                min_counts["green"], current_counts["green"])
        # print(min_counts)
        power = min_counts["red"] * min_counts["blue"] * min_counts["green"]
        # print(power)
        result += power


print(result)
