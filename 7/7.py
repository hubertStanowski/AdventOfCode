import os
import sys
from collections import Counter


def get_value(card):
    return "J23456789TQKA".index(card)


def get_type(hand, part2=False):
    counts = Counter(hand)
    if part2 and "J" in hand:
        joker_count = counts["J"]
        del counts["J"]
        if len(counts) == 0:
            return 50
        else:
            highest = counts.most_common()[0][0]
            counts[highest] += joker_count
    match sorted(counts.values(), reverse=True):
        case [5]:
            return 50
        case [4, 1]:
            return 40
        case [3, 2]:
            return 30
        case [3, 1, 1, ]:
            return 20
        case [2, 2, 1]:
            return 10
        case [2, 1, 1, 1]:
            return 1
        case _:
            return 0


def sort_key(data):
    hand = data[0]
    return [get_type(hand, part2=True)] + [get_value(c) for c in hand]
    # change part2 to false for part 1


with open(os.path.join(sys.path[0], "input.txt")) as f:
    result = 0
    data = f.read().split('\n')
    for line in range(len(data)):
        data[line] = data[line].split()
        data[line][1] = int(data[line][1])
    data.sort(key=sort_key)
    rank = 1
    for hand, bid in data:
        result += bid * rank
        rank += 1

    print(result)
