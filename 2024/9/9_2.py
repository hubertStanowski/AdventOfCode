import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(current_dir, 'input.txt')


def calculate_sum(length, block):
    return length * (2 * block + length - 1) // 2


data = []
with open(input_path) as f:
    for line in f.read().split('\n'):
        data.append(line)

original = list(map(int, list(data[0]))) + [0]
# print(original)


triple = {}

for i in range(0, len(original), 2):
    triple[i // 2] = {
        "l": original[i],
        "f": original[i + 1],
        "s": [],
    }

for candidate_id in reversed(triple):
    c = triple[candidate_id]
    for target_free_id in triple:
        if candidate_id <= target_free_id:
            break
        t = triple[target_free_id]
        if t["f"] >= c["l"] > 0:
            t["s"].append({"l": c["l"], "id": candidate_id})
            t["f"] -= c["l"]
            c["ff"] = c["l"]
            c["l"] = 0
            break
part2 = 0
block = 0
for file_id, file in triple.items():
    if "ff" in file:
        block += file["ff"]
    else:
        part2 += file_id * calculate_sum(file["l"], block)
        block += file["l"]

    for subfile in file["s"]:
        part2 += subfile["id"] * calculate_sum(subfile["l"], block)
        block += subfile["l"]
    block += file["f"]

print("PART 2: ", part2)
