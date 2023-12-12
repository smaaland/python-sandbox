import itertools

lines = [line.strip() for line in open("input11.txt", "r").readlines()]

vertical_splits = []
for i, line in enumerate(lines):
    if all(c == "." for c in line):
        vertical_splits.append(i)

horizontal_splits = []
for x in range(len(lines[0])):
    if all(lines[y][x] == "." for y in range(len(lines))):
        horizontal_splits.append(x)

galaxies = []
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "#":
            galaxies.append((y, x))

lengths_1 = []
lengths_2 = []
for a, b in itertools.combinations(galaxies, 2):
    unexpanded_distance = abs(a[0] - b[0]) + abs(a[1] - b[1])
    y_splits = len(
        list(
            set([y for y in range(min(a[0], b[0]), max(a[0], b[0]))])
            & set(vertical_splits)
        )
    )
    x_splits = len(
        list(
            set([x for x in range(min(a[1], b[1]), max(a[1], b[1]))])
            & set(horizontal_splits)
        )
    )
    lengths_1.append(unexpanded_distance + y_splits * 1 + x_splits * 1)
    lengths_2.append(unexpanded_distance + y_splits * 999999 + x_splits * 999999)

print(f"Part 1: {sum(lengths_1)}")
print(f"Part 2: {sum(lengths_2)}")
