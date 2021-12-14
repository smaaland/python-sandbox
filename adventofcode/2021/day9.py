import math
from typing import Tuple

with open('input9.txt', 'r') as f:
    lines = [[int(x) for x in list(line.rstrip())] for line in f]

risk_levels = []
low_points = []
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if y - 1 >= 0:
            if lines[y-1][x] <= lines[y][x]:
                continue
        if y + 1 <= len(lines) - 1:
            if lines[y+1][x] <= lines[y][x]:
                continue
        if x - 1 >= 0:
            if lines[y][x-1] <= lines[y][x]:
                continue
        if x + 1 <= len(lines[y]) - 1:
            if lines[y][x+1] <= lines[y][x]:
                continue
        risk_levels.append(1 + lines[y][x])
        low_points.append((x, y))

print(f"Part 1: {sum(risk_levels)}")

basins = {k: [k] for k in low_points}


def find_neighbours(low_point: Tuple[int, int], x: int, y: int) -> None:
    if y - 1 >= 0:
        if lines[y - 1][x] != 9:
            if (x, y-1) not in basins[low_point]:
                basins[low_point].append((x, y-1))
                find_neighbours(low_point, x, y-1)
    if y + 1 <= len(lines) - 1:
        if lines[y + 1][x] != 9:
            if (x, y+1) not in basins[low_point]:
                basins[low_point].append((x, y+1))
                find_neighbours(low_point, x, y+1)
    if x - 1 >= 0:
        if lines[y][x - 1] != 9:
            if (x - 1, y) not in basins[low_point]:
                basins[low_point].append((x - 1, y))
                find_neighbours(low_point, x - 1, y)
    if x + 1 <= len(lines[y]) - 1:
        if lines[y][x + 1] != 9:
            if (x + 1, y) not in basins[low_point]:
                basins[low_point].append((x + 1, y))
                find_neighbours(low_point, x + 1, y)


for p in basins:
    find_neighbours(p, p[0], p[1])

print(f"Part 2: {math.prod(sorted([len(r) for r in basins.values()])[-3:])}")