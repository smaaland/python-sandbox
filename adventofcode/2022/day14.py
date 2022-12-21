from collections import defaultdict


class OutOfBoundsException(Exception):
    pass


lines = [line.strip() for line in open("input14.txt", "r").readlines()]
stones = defaultdict(lambda: defaultdict(dict))
stones_2 = defaultdict(lambda: defaultdict(dict))
min_x = None
max_x = None
min_y = None
max_y = None

for l in lines:
    for p, q in [l.split(" -> ")[i:i + 2] for i in
        range(0, len(l.split(" -> ")) - 1, 1)]:
        px, py = [int(x) for x in p.split(",")]
        qx, qy = [int(y) for y in q.split(",")]
        min_x = px if not min_x or px < min_x else min_x
        min_x = qx if not min_x or qx < min_x else min_x
        max_x = px if not max_x or px > max_x else max_x
        max_x = qx if not max_x or qx > max_x else max_x
        min_y = py if not min_y or py < min_y else min_y
        min_y = qy if not min_y or qy < min_y else min_y
        max_y = py if not max_y or py > max_y else max_y
        max_y = qy if not max_y or qy > max_y else max_y

        for y in range(min(py, qy), max(py, qy) + 1):
            for x in range(min(px, qx), max(px, qx) + 1):
                stones[y][x] = "#"
                stones_2[y][x] = "#"


def move(y, x, s, infinite_floor=False):
    if y + 1 > max_y and not infinite_floor:
        raise OutOfBoundsException
    if infinite_floor:
        if y >= max_y + 1:
            return y, x
    if not s[y + 1][x]:
        return y + 1, x
    elif not s[y + 1][x - 1]:
        return y + 1, x - 1
    elif not s[y + 1][x + 1]:
        return y + 1, x + 1
    return y, x


iterations = 0
try:
    while True:
        pos = (0, 500)
        while (new_pos := move(pos[0], pos[1], stones)) != pos:
            pos = new_pos
        stones[pos[0]][pos[1]] = "o"
        iterations += 1
except OutOfBoundsException:
    pass

# for y in range(0, max_y+1):
#     for x in range(min_x, max_x+1):
#         if stones[y][x]:
#             print(stones[y][x], end="")
#         else:
#             print(".", end="")
#     print()

print(f"Part 1: {iterations}")

iterations_2 = 0
try:
    while True:
        pos = (0, 500)
        while (
        new_pos := move(pos[0], pos[1], stones_2, infinite_floor=True)) != pos:
            pos = new_pos
        stones_2[pos[0]][pos[1]] = "o"
        # min_x = pos[1] if not min_x or pos[1] < min_x else min_x
        # max_x = pos[1] if not max_x or pos[1] > max_x else max_x
        iterations_2 += 1
        if pos == (0, 500):
            raise OutOfBoundsException
except OutOfBoundsException:
    pass

# for y in range(0, max_y + 3):
#     for x in range(min_x, max_x + 1):
#         if stones_2[y][x]:
#             print(stones_2[y][x], end="")
#         else:
#             print(".", end="")
#     print()

print(f"Part 2: {iterations_2}")
