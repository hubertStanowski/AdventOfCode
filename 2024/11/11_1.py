import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(current_dir, 'input.txt')


data = []
with open(input_path) as f:
    for line in f.read().split('\n'):
        data.append(line.split())

stones = data[0]


def split_in_two(num):
    half1 = str(int(num[:len(num)//2]))
    half2 = str(int(num[len(num)//2:]))
    return half1, half2


blinks = 25
for _ in range(blinks):
    i = 0
    while i < len(stones):
        if stones[i] == '0':
            stones[i] = '1'
        elif len(stones[i]) % 2 == 0:
            half1, half2 = split_in_two(stones[i])
            stones[i] = half1
            stones.insert(i + 1, half2)
            i += 1
        else:
            stones[i] = str(int(stones[i]) * 2024)
        i += 1
    # print(stones)


part1 = len(stones)
print("PART 1: ", part1)
