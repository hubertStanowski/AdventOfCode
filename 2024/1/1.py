import os
from collections import Counter

current_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(current_dir, 'input.txt')


left, right = [], []
with open(input_path) as f:
    for line in f:
        col1, col2 = map(int, line.split())
        left.append(col1)
        right.append(col2)


left.sort()
right.sort()
right_counts = Counter(right)

n = len(left)

part1 = 0
for i in range(n):
    part1 += abs(left[i] - right[i])

print("PART 1: ", part1)

part2 = 0
for num in left:
    part2 += num * right_counts[num]

print("PART 2: ", part2)
