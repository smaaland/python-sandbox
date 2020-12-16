import itertools
from functools import reduce

with open('input6.txt', 'r') as f:
    lines = [line.rstrip() for line in f]

key = lambda sep: sep == ''
group_answers = [" ".join(list(group)).split(" ") for is_key, group in itertools.groupby(lines, key) if not is_key]

_sum = 0
_sum_2 = 0

for group in group_answers:
    unique_answers = list(set(''.join(group)))
    _sum += len(unique_answers)
    all_yes = list(reduce(set.intersection, [set(item) for item in group]))
    _sum_2 += len(all_yes)

print(f"Part 1: {_sum}")
print(f"Part 2: {_sum_2}")