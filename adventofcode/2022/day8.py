lines = [line.strip("\n") for line in open("input8.txt", "r").readlines()]

visible = set()
scenic_scores = []

for y in range(len(lines)):
    highest = -1
    for x in range(len(lines[y])):
        if int(lines[y][x]) > highest:
            visible.add((y, x))
            highest = int(lines[y][x])
    highest = -1
    for x in reversed(range(len(lines[y]))):
        if int(lines[y][x]) > highest:
            visible.add((y, x))
            highest = int(lines[y][x])
for x in range(len(lines[0])):
    highest = -1
    for y in range(len(lines)):
        if int(lines[y][x]) > highest:
            visible.add((y, x))
            highest = int(lines[y][x])
    highest = -1
    for y in reversed(range(len(lines))):
        if int(lines[y][x]) > highest:
            visible.add((y, x))
            highest = int(lines[y][x])

for y in range(len(lines)):
    for x in range(len(lines[y])):
        if x == 0 or y == 0 or x == len(lines[y]) - 1 or y == len(lines[x]) - 1:
            continue
        height = int(lines[y][x])
        left, right, up, down = 0, 0, 0, 0

        for xl in reversed(range(x)):
            left += 1
            if int(lines[y][xl]) >= height:
                break
        for xl in range(x+1, len(lines[y])):
            right += 1
            if int(lines[y][xl]) >= height:
                break
        for yl in reversed(range(y)):
            up += 1
            if int(lines[yl][x]) >= height:
                break
        for yl in range(y+1, len(lines)):
            down += 1
            if int(lines[yl][x]) >= height:
                break
        scenic_scores.append(left * right * up * down)

print(f"Part 1: {len(visible)}")
print(f"Part 2: {max(scenic_scores)}")
