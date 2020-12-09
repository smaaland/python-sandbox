import math

with open('input3.txt', 'r') as f:
    lines = [line.rstrip() for line in f]

line_length = len(lines[0])
number_of_lines = len(lines)


def trees_hit(right_steps, down_steps=1):
    total_trees = 0
    step = 0
    for y in range(0, number_of_lines, down_steps):
        x = right_steps * step % line_length
        if lines[y][x] == '#':
            total_trees += 1
        step += 1
    return total_trees


slopes = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2],
]

print(f"Part 1: {trees_hit(3)}")
print(f"Part 2: {math.prod([trees_hit(slope[0], slope[1]) for slope in slopes])}")
