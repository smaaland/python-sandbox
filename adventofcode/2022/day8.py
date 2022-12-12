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

for y in range(len(lines)):
    for x in range(len(lines[y])):
        if x == 0 or y == 0 or x == len(lines[y]) - 1 or y == len(lines[x]) - 1:
            continue
        height = int(lines[y][x])

        left = 0
        for xl in reversed(range(x)):
            if int(lines[y][xl]) < height:
                left += 1
            else:
                left += 1
                break
        # print(y, x, left)
        right = 0
        for xl in range(x+1, len(lines[y])):
            # print(xl)
            if int(lines[y][xl]) < height:
                right += 1
            else:
                right += 1
                break
        # print(y, x, right)


print(f"Part 1: {len(visible)}")
