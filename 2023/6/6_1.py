import os
import sys

with open(os.path.join(sys.path[0], "input.txt")) as f:
    times, distances = f.read().split("\n")
    times = list(map(int, times.split()[1:]))
    distances = list(map(int, distances.split()[1:]))
    result = 1

    for race in range(len(times)):
        count = 0
        time = times[race]
        distance = distances[race]
        for i in range(time):
            current = i * (time-i)
            if current > distance:
                count += 1
        result *= count

    print(result)
