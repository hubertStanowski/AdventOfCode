import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(current_dir, 'input.txt')

reports = []
with open(input_path) as f:
    for line in f:
        reports.append(list(map(int, line.split())))


def is_safe(report):
    prev_diff = None
    for i in range(1, len(report)):
        curr_diff = report[i] - report[i-1]
        if (prev_diff and curr_diff * prev_diff <= 0) or not (1 <= abs(curr_diff) <= 3):
            return False
        prev_diff = curr_diff
    return True


part1 = 0
for report in reports:
    if is_safe(report):
        part1 += 1

print("PART 1: ", part1)

part2 = 0
for report in reports:
    for level in range(len(report)):
        if is_safe(report[:level] + report[level + 1:]):
            part2 += 1
            break

print("PART 2: ", part2)
