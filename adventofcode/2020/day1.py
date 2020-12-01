import math
from itertools import combinations

with open('input1.txt', 'r') as f:
    lines = [int(line.rstrip()) for line in f]

part_1 = math.prod(list(filter(lambda a: a[0]+a[1] == 2020, combinations(lines, 2)))[0])
part_2 = math.prod(list(filter(lambda a: a[0]+a[1]+a[2] == 2020, combinations(lines, 3)))[0])

print(f'Part 1: {part_1}')
print(f'Part 2: {part_2}')