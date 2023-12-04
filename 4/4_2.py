import os
import sys

with open(os.path.join(sys.path[0], "input.txt")) as f:
    cards = f.read().split("\n")
    for i, card in enumerate(cards):
        card = card.split(": ")[1]
        card = card.split("| ")
        card[0] = card[0].split()
        card[1] = card[1].split()
        cards[i] = card

    result = [1] * len(cards)
    matches = []
    for winning, available in cards:
        current_matches = len(set(winning) & set(available))
        matches.append(current_matches)

    for i, current in enumerate(matches):
        for j in range(current):
            result[i+j+1] += result[i]

    print(sum(result))
