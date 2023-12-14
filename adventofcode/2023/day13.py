from itertools import groupby

lines = [line.strip() for line in open("input13.txt", "r").readlines()]

patterns = [list(g) for k, g in groupby(lines, key=bool) if k]


def get_vertical_mirrors(_pattern):
    vertical_intersections = []
    for row in _pattern:
        row_intersections = set()
        for i in range(1, len(row)):
            start = row[:i][::-1]
            end = row[i:]
            if all(x == y for x, y in zip(start, end)):
                row_intersections.add(i)

        vertical_intersections.append(row_intersections)
    return list(set.intersection(*vertical_intersections))


def get_horizontal_mirrors(_pattern):
    horizontal_intersections = []
    for i in range(1, len(_pattern)):
        start = _pattern[:i][::-1]
        end = _pattern[i:]
        if all(x == y for x, y in zip(start, end)):
            horizontal_intersections.append(i)
    return horizontal_intersections


sum_1 = 0
sum_2 = 0

for pattern in patterns:
    vertical_mirrors = get_vertical_mirrors(pattern)
    if vertical_mirrors:
        sum_1 += vertical_mirrors[0]
    horizontal_mirrors = get_horizontal_mirrors(pattern)
    if horizontal_mirrors:
        sum_1 += horizontal_mirrors[0] * 100

    new_horizontal_mirrors = set()
    new_vertical_mirrors = set()
    for y, row in enumerate(pattern):
        for x, c in enumerate(row):
            if pattern[y][x] == "#":
                new = "."
                old = "#"
            else:
                new = "#"
                old = "."
            pattern[y] = pattern[y][:x] + new + pattern[y][x + 1 :]
            vm = get_vertical_mirrors(pattern)
            for new in [m for m in vm if m not in vertical_mirrors]:
                new_vertical_mirrors.add(new)
            hm = get_horizontal_mirrors(pattern)
            for new in [m for m in hm if m not in horizontal_mirrors]:
                new_horizontal_mirrors.add(new)
            pattern[y] = pattern[y][:x] + old + pattern[y][x + 1 :]

    for m in list(new_vertical_mirrors):
        sum_2 += m
    for m in list(new_horizontal_mirrors):
        sum_2 += m * 100

print(f"Part 1: {sum_1}")
print(f"Part 2: {sum_2}")
