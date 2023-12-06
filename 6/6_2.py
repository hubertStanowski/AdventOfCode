import os
import sys

with open(os.path.join(sys.path[0], "input.txt")) as f:
    time, distance = f.read().split("\n")
    time = int("".join(time.split()[1:]))
    distance = int("".join(distance.split()[1:]))
    i = -1
    current = 0
    while current <= distance:
        i += 1
        current = i * (time-i)

    result = time - (2 * i) + 1
    print(result)
