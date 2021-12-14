with open('input9.txt', 'r') as f:
    lines = [[int(x) for x in list(line.rstrip())] for line in f]

risk_levels = []
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

print(f"Part 1: {sum(risk_levels)}")
