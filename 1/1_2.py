import os
import sys
import re

digits_worded = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
                 "six": 6, "seven": 7, "eight": 8, "nine": 9}
with open(os.path.join(sys.path[0], "input.txt")) as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        first_digit = 0
        first_idx = -1
        last_digit = 0
        last_digit = -1
        for i, ch in enumerate(line):
            if ch.isdigit():
                if first_digit == 0:
                    first_digit = int(ch)
                    first_idx = i
                last_digit = int(ch)
                last_idx = i

        for worded in digits_worded.keys():
            idxs = [d.start() for d in re.finditer(worded, line)]
            if idxs != []:
                if min(idxs) < first_idx:
                    first_idx = min(idxs)
                    first_digit = digits_worded[worded]
                if max(idxs) > last_idx:
                    last_idx = max(idxs)
                    last_digit = digits_worded[worded]

        sum += first_digit*10 + last_digit

print(sum)
