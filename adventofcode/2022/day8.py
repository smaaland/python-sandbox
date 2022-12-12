lines = [line.strip("\n") for line in open("input8.txt", "r").readlines()]

visible = set()

for y in range(len(lines)):
    highest = -1
    for x in range(len(lines[y])):
        if int(lines[y][x]) > highest:
            visible.add((y,x))
            highest = int(lines[y][x])
    highest = -1
    for x in reversed(range(len(lines[y]))):
        if int(lines[y][x]) > highest:
            visible.add((y,x))
            highest = int(lines[y][x])
for x in range(len(lines[0])):
    highest = -1
    for y in range(len(lines)):
        if int(lines[y][x]) > highest:
            visible.add((y,x))
            highest = int(lines[y][x])
    highest = -1
    for y in reversed(range(len(lines))):
        if int(lines[y][x]) > highest:
            visible.add((y,x))
            highest = int(lines[y][x])

print(f"Part 1: {len(visible)}")
