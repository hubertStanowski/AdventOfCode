from functools import reduce
import os
import sys

"""
code mostly by: https://www.reddit.com/user/4HbQ/
my approach didn't work on the scale of input,
learned about reduce today
https://www.geeksforgeeks.org/reduce-in-python/
"""

seeds, * \
    maps = open(os.path.join(
        sys.path[0], "input.txt")).read().split('\n\n')
seeds = list(map(int, seeds.split()[1:]))


def check(input, mapping):
    output = []

    for start, size in input:
        while size > 0:
            for curr in mapping.split('\n')[1:]:
                dst, src, n = map(int, curr.split())
                if src <= start and start < src+n:
                    n -= max(start - src, n - size)
                    output.append((start - src + dst, n))
                    start += n
                    size -= n
                    break
            else:
                output.append((start, size))
                break

    return output


results = []
for seed in [zip(seeds, [1] * len(seeds)), zip(seeds[0::2], seeds[1::2])]:
    results.append(min(reduce(check, maps, seed)))

print("Part 1: ", results[0][0])
print("Part 2 ", results[1][0])
