with open('input11.txt', 'r') as f:
    lines = [[int(x) for x in list(line.rstrip())] for line in f]

total_flashes_part_1 = 0
i = 0
while True:
    lines = [[x+1 for x in row] for row in lines]
    is_flashing = True
    all_flashing = []
    while is_flashing:
        is_flashing = False
        flashing = []
        for y in range(len(lines)):
            for x in range(len(lines[y])):
                if lines[y][x] > 9 and (y, x) not in all_flashing:
                    is_flashing = True
                    flashing.append((y, x))
                    all_flashing.append((y, x))
        for y, x in flashing:
            if y - 1 >= 0:
                lines[y - 1][x] += 1
            if y + 1 <= len(lines) - 1:
                lines[y + 1][x] += 1
            if x - 1 >= 0:
                lines[y][x - 1] += 1
            if x + 1 <= len(lines[y]) - 1:
                lines[y][x + 1] += 1
            if x - 1 >= 0 and y - 1 >= 0:
                lines[y - 1][x - 1] += 1
            if x - 1 >= 0 and y + 1 <= len(lines) - 1:
                lines[y + 1][x - 1] += 1
            if x + 1 <= len(lines[y]) - 1 and y - 1 >= 0:
                lines[y - 1][x + 1] += 1
            if x + 1 <= len(lines[y]) - 1 and y + 1 <= len(lines) - 1:
                lines[y + 1][x + 1] += 1
    for y, x in all_flashing:
        lines[y][x] = 0
    if i < 100:
        total_flashes_part_1 += len(all_flashing)
    i += 1

    if len(all_flashing) == len(lines)*len(lines[0]):
        break

print(f"Part 1: {total_flashes_part_1}")
print(f"Part 2: {i}")