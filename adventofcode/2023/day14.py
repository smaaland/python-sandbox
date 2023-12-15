import copy
import math

lines = [list(line.strip()) for line in open("input14.txt", "r").readlines()]
lines_2 = copy.deepcopy(lines)


def get_total_load(_lines):
    total_load = 0
    for y, line in enumerate(_lines):
        for c in line:
            if c == "O":
                total_load += len(_lines) - y
    return total_load


def tilt(lines, direction):
    current_obstacles = {
        "W": [-1 for _ in range(len(lines[0]))],
        "E": [len(lines[0]) for _ in range(len(lines[0]))],
        "N": [-1 for _ in range(len(lines[0]))],
        "S": [len(lines) for _ in range(len(lines[0]))],
    }
    current_obstacle = current_obstacles[direction]
    if direction == "N":
        for y in range(len(lines)):
            for x in range(len(lines[0])):
                if lines[y][x] == "#":
                    current_obstacle[x] = y
                elif lines[y][x] == "O":
                    lines[y][x] = "."
                    lines[current_obstacle[x] + 1][x] = "O"
                    current_obstacle[x] += 1
    if direction == "S":
        for y in reversed(range(len(lines))):
            for x in range(len(lines[0])):
                if lines[y][x] == "#":
                    current_obstacle[x] = y
                elif lines[y][x] == "O":
                    lines[y][x] = "."
                    lines[current_obstacle[x] - 1][x] = "O"
                    current_obstacle[x] -= 1
    if direction == "W":
        for x in range(len(lines[0])):
            for y in range(len(lines)):
                if lines[y][x] == "#":
                    current_obstacle[y] = x
                elif lines[y][x] == "O":
                    lines[y][x] = "."
                    lines[y][current_obstacle[y] + 1] = "O"
                    current_obstacle[y] += 1
    if direction == "E":
        for x in reversed(range(len(lines[0]))):
            for y in range(len(lines)):
                if lines[y][x] == "#":
                    current_obstacle[y] = x
                elif lines[y][x] == "O":
                    lines[y][x] = "."
                    lines[y][current_obstacle[y] - 1] = "O"
                    current_obstacle[y] -= 1


tilt(lines, "N")
print(f"Part 1: {get_total_load(lines)}")


cache = {}
i = 0
while i < 1000000000:
    key = "".join(["".join(line) for line in lines_2])
    if key in cache:
        if cache[key] + i < 1000000000:
            loop_size = i - cache[key]
            offset = i % loop_size
            i = math.floor((1000000000 - offset) / loop_size) * loop_size + offset
            continue
    if key not in cache:
        cache[key] = i

    tilt(lines_2, "N")
    tilt(lines_2, "W")
    tilt(lines_2, "S")
    tilt(lines_2, "E")
    i += 1

print(f"Part 2: {get_total_load(lines_2)}")
