from collections import defaultdict
from functools import cmp_to_key
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(current_dir, 'input.txt')

with open(input_path) as f:
    rules, updates = f.read().split("\n\n")

rules = rules.split('\n')
updates = updates.split('\n')
before = defaultdict(list)
after = defaultdict(list)
part2 = 0

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


part2 = 0
for update in updates:
    update = update.split(',')
    update = list(map(int, update))

    if not is_valid(update):
        sorting_key = cmp_to_key(lambda x, y: 1 if y in before[x] else -1)
        changed = sorted(update, key=sorting_key)
        part2 += changed[len(changed)//2]

print("PART 2: ", part2)
