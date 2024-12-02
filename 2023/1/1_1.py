import os
import sys

with open(os.path.join(sys.path[0], "input.txt")) as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        first_digit = 0
        last_digit = 0
        for i, ch in enumerate(line):
            if ch.isdigit():
                if first_digit == 0:
                    first_digit = int(ch)
                last_digit = int(ch)

        sum += first_digit*10 + last_digit

print(sum)
