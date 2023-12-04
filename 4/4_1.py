import os
import sys

with open(os.path.join(sys.path[0], "input.txt")) as f:
    result = 0
    cards = f.read().split("\n")
    for i, card in enumerate(cards):
        card = card.split(": ")[1]
        card = card.split("| ")
        card[0] = card[0].split()
        card[1] = card[1].split()
        cards[i] = card

    for winning, available in cards:
        matches = len(set(winning) & set(available))
        if matches > 0:
            points = pow(2, matches - 1)
            result += points

print(int(result))
