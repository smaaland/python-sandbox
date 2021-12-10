from typing import Dict, List

with open('input5.txt', 'r') as f:
    lines = [line.rstrip() for line in f]

rows = [
    {
        "x1": int(d[0].split(",")[0]),
        "y1": int(d[0].split(",")[1]),
        "x2": int(d[1].split(",")[0]),
        "y2": int(d[1].split(",")[1]),
    } for d in [_.split(" -> ") for _ in lines]
]

max_x = max(max([_["x1"] for _ in rows]), max([_["x2"] for _ in rows]))
max_y = max(max([_["y1"] for _ in rows]), max([_["y2"] for _ in rows]))
matrix_1 = [[0 for _ in range(max_x + 1)] for __ in range((max_y + 1))]
matrix_2 = [[0 for _ in range(max_x + 1)] for __ in range((max_y + 1))]


def get_all_points_on_line(l: Dict) -> List[List[int]]:
    min_x = min(l["x1"], l["x2"])
    max_x = max(l["x1"], l["x2"])
    min_y = min(l["y1"], l["y2"])
    max_y = max(l["y1"], l["y2"])
    reversed_x = l["x1"] > l["x2"]
    reversed_y = l["y1"] > l["y2"]
    if l["x1"] == l["x2"]:
        return [[min_x, y] for y in range(min_y, max_y+1)]
    if l["y1"] == l["y2"]:
        return [[x, min_y] for x in range(min_x, max_x+1)]

    x_values = [_ for _ in range(min_x, max_x + 1)]
    if reversed_x:
        x_values = reversed(x_values)
    y_values = [_ for _ in range(min_y, max_y + 1)]
    if reversed_y:
        y_values = reversed(y_values)
    return list(map(list, zip(x_values, y_values)))


for row in rows:
    points = get_all_points_on_line(row)
    for x, y in points:
        if row["x1"] == row["x2"] or row["y1"] == row["y2"]:
            matrix_1[y][x] += 1
        matrix_2[y][x] += 1


part_1 = sum([1 if _ > 1 else 0 for __ in matrix_1 for _ in __])
part_2 = sum([1 if _ > 1 else 0 for __ in matrix_2 for _ in __])
print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")

