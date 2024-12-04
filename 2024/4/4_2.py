import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(current_dir, 'input.txt')


rows = []
with open(input_path) as f:
    rows = f.read().split('\n')


part2 = 0

# M.S
# .A.
# M.S

targets = {"MSAMS", "SMASM", "MMASS", "SSAMM"}
irrelevant_positions = {(0, 1), (1, 0), (1, 2), (2, 1)}

for i in range(len(rows) - 2):
    for j in range(len(rows[0]) - 2):
        curr_square = []

        for k in range(3):
            for l in range(3):
                if (k, l) not in irrelevant_positions:
                    curr_square.append(rows[i+k][j+l])

        if "".join(curr_square) in targets:
            part2 += 1


print("PART 2: ", part2)
