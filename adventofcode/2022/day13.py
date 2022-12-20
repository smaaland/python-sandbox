import ast
from functools import cmp_to_key
from itertools import zip_longest

lines = [line.strip() for line in open("input13.txt", "r").readlines()]
pairs = [lines[i:i + 2] for i in range(0, len(lines), 3)]
all_packets = []
div1, div2 = [[2]], [[6]]
right_order = []


def cmp(first, second):
    if first is None:
        return -1
    if second is None:
        return 1
    if isinstance(first, int) and isinstance(second, int):
        if first < second:
            return -1
        elif first > second:
            return 1
        else:
            return 0
    if isinstance(first, list) and isinstance(second, list):
        for a, b in zip_longest(first, second):
            if (res := cmp(a, b)) != 0:
                return res
        return 0
    if isinstance(first, int):
        first = [first]
    if isinstance(second, int):
        second = [second]
    return cmp(first, second)


for i, p in enumerate(pairs, 1):
    p0 = ast.literal_eval(p[0])
    p1 = ast.literal_eval(p[1])
    all_packets.append(p0)
    all_packets.append(p1)
    if cmp(p0, p1) != 1:
        right_order.append(i)

print(f"Part 1: {sum(right_order)}")

sorted_packets = sorted([*all_packets, div1, div2], key=cmp_to_key(cmp))
print(f"Part 2: {(sorted_packets.index(div1) + 1) * (sorted_packets.index(div2) + 1)}")
