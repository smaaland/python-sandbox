with open('input1.txt', 'r') as f:
    lines = [int(line.rstrip()) for line in f]

part_1 = 0
part_2 = 0

for x, y in zip(lines, lines[1:]):
    part_1 += 1 if y > x else 0

print(f"Part 1: {part_1}")

tmp = [(x, y, z,) for x, y, z in zip(lines, lines[1:], lines[2:])]
for x, y in zip(tmp, tmp[1:]):
    part_2 += 1 if sum(y) > sum(x) else 0

print(f"Part 2: {part_2}")
