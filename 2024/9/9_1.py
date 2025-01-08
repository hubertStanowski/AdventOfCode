import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(current_dir, 'input.txt')


def find_free_space(start, state):
    try:
        while state[start] != '.':
            start += 1
        return start
    except:
        return len(state)


data = []
with open(input_path) as f:
    for line in f.read().split('\n'):
        data.append(line)

original = list(map(int, list(data[0])))
# print(original)


state = []

id = 0
for i, count in enumerate(original):
    if i % 2 == 1:
        state += ["."] * count
    else:
        state += [id] * count
        id += 1


curr = 0

while curr < len(state):
    curr = find_free_space(curr, state)
    while curr < len(state) and state[curr] == '.':
        back = state.pop()
        while back == '.':
            back = state.pop()
        state[curr] = back
        curr += 1

part1 = 0
for i, id in enumerate(state):
    part1 += i * id

print("PART 1: ", part1)
