import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(current_dir, 'input.txt')


rows = []
with open(input_path) as f:
    rows = f.read().split('\n')


cols = list(map("".join, zip(*rows)))

part1 = 0
targets = ["XMAS", "SAMX"]
for row in rows:
    for target in targets:
        part1 += row.count(target)

for col in cols:
    for target in targets:
        if target in col:
            part1 += col.count(target)

# Diagonals
for i in range(len(rows) - 3):
    for j in range(len(cols) - 3):
        curr_square = []

        for k in range(4):
            row = []
            for l in range(4):
                row.append(rows[i+k][j+l])
            curr_square.append(row)

        topleft_bottomright = [curr_square[k][k] for k in range(4)]
        bottomleft_topright = [curr_square[k][3-k] for k in range(4)]

        for target in targets:
            part1 += "".join(topleft_bottomright).count(target)

            part1 += "".join(bottomleft_topright).count(target)


print("PART 1: ", part1)
