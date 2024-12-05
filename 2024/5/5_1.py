from collections import defaultdict
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(current_dir, 'input.txt')

with open(input_path) as f:
    rules, updates = f.read().split("\n\n")

rules = rules.split('\n')
updates = updates.split('\n')
before = defaultdict(list)
after = defaultdict(list)
part1 = 0

for i, rule in enumerate(rules):
    rule = rule.split('|')
    rule = tuple(map(int, rule))
    before[rule[1]].append(rule[0])
    after[rule[0]].append(rule[1])


def is_valid(update):
    should_be_before = set()
    for curr in update:
        if curr in should_be_before:
            return False
        should_be_before = should_be_before.union(set(before[curr]))

    return True


for i, update in enumerate(updates):
    update = update.split(',')
    update = list(map(int, update))

    if is_valid(update):
        part1 += update[len(update) // 2]

print("PART 1: ", part1)
