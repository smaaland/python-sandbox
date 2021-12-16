import copy
from collections import Counter
from typing import List

with open('input12.txt', 'r') as f:
    lines = [line.rstrip().split("-") for line in f]

keys = set([x[0] for x in lines])
keys.update(set([x[1] for x in lines]))
paths = {k: [] for k in keys}

for f, t in lines:
    paths[f].append(t)
    paths[t].append(f)

distinct_paths_1 = []
distinct_paths_2 = []


def traverse(path: List[str], position: str) -> None:
    path.append(position)
    if position == 'end':
        distinct_paths_1.append(path)
        return
    for n in paths[position]:
        if n.isupper():
            traverse(copy.deepcopy(path), n)
        elif n not in path:
            traverse(copy.deepcopy(path), n)


def traverse_2(path: List[str], position: str) -> None:
    path.append(position)
    if position == 'end':
        distinct_paths_2.append(path)
        return
    for n in paths[position]:
        counter = Counter(path)
        if n.isupper():
            traverse_2(copy.deepcopy(path), n)
        elif (n not in path or len([k for k, v in dict(counter).items() if counter[k] > 1]) < 1) and n != 'start':
            traverse_2(copy.deepcopy(path), n)


traverse([], 'start')
traverse_2([], 'start')

for l in distinct_paths_2:
    print(l)

print(f"Part 1: {len(distinct_paths_1)}")
print(f"Part 1: {len(distinct_paths_2)}")