import os
import math

current_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(current_dir, 'input.txt')


data = []
with open(input_path) as f:
    for line in f.read().split('\n'):
        data.append(line.split())

stones = list(map(int, data[0]))


def num_len(num): return int(math.log10(num)) + 1


def blink(n):
    if n == 0:
        return [1]
    elif num_len(n) % 2 == 0:
        p = 10 ** (num_len(n) / 2)
        return [int(n / p), int(n % p)]
    else:
        return [n * 2024]


blinks = 75
stone_dict = dict((n, 1) for n in stones)
for i in range(blinks):
    temp = dict()
    for num, n in stone_dict.items():
        for new in blink(num):
            if new in temp:
                temp[new] += n
            else:
                temp[new] = n

    stone_dict = temp

part2 = sum(n for n in stone_dict.values())
print("PART 2: ", part2)
