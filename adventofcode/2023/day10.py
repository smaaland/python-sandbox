lines = [line.strip() for line in open("input10.txt", "r").readlines()]

for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "S":
            position = (y, x)
            start_position = (y, x)

visited = set()
direction = (0, 0)

allowed_tiles_in_dir = {
    (0, 1): ["-", "7", "J"],
    (1, 0): ["|", "J", "L"],
    (0, -1): ["-", "L", "F"],
    (-1, 0): ["|", "F", "7"],
}

new_dirs = {
    "7": {
        (0, 1): (1, 0),
        (-1, 0): (0, -1),
    },
    "J": {
        (0, 1): (-1, 0),
        (1, 0): (0, -1),
    },
    "L": {
        (0, -1): (-1, 0),
        (1, 0): (0, 1),
    },
    "F": {
        (-1, 0): (0, 1),
        (0, -1): (1, 0),
    },
    "-": {
        (0, 1): (0, 1),
        (0, -1): (0, -1),
    },
    "|": {
        (1, 0): (1, 0),
        (-1, 0): (-1, 0),
    },
}

for y, x in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
    next_pos = tuple(map(sum, zip(position, (y, x))))
    if lines[next_pos[0]][next_pos[1]] in allowed_tiles_in_dir[(y, x)]:
        direction = (y, x)
        start_direction = (y, x)
        break


while position not in visited:
    visited.add(position)
    position = tuple(map(sum, zip(position, direction)))
    if lines[position[0]][position[1]] in new_dirs:
        direction = new_dirs[lines[position[0]][position[1]]][direction]

print(f"Part 1: {len(visited) // 2}")


for c, d in new_dirs.items():
    for k, v in d.items():
        if start_direction == v and direction == k:
            lines[start_position[0]] = lines[start_position[0]].replace("S", c)

# Begin ray casting
inside = 0
for y, line in enumerate(lines):
    wall_hits = 0
    wall_start = ""
    for x in range(len(line)):
        if (y, x) in visited:
            if lines[y][x] == "|":
                wall_hits += 1
            elif lines[y][x] in ["F", "L"]:
                wall_start = lines[y][x]
            elif lines[y][x] in ["J", "7"]:
                if wall_start == "F" and lines[y][x] == "J":
                    wall_hits += 1
                    wall_start = ""
                elif wall_start == "L" and lines[y][x] == "7":
                    wall_hits += 1
                    wall_start = ""
        else:
            if wall_hits % 2 == 1:
                inside += 1

print(f"Part 2: {inside}")
