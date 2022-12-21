from collections import defaultdict

class OutOfBoundaryException(Exception):
    pass

lines = [line.strip() for line in open("input14.txt", "r").readlines()]
stones = defaultdict(lambda: defaultdict(dict))
all_x = set()
all_y = set()


for l in lines:
    for p, q in [l.split(" -> ")[i:i + 2] for i in range(0, len(l.split(" -> ")) - 1, 1)]:
        px, py = [int(x) for x in p.split(",")]
        qx, qy = [int(y) for y in q.split(",")]
        all_x.add(px)
        all_x.add(qx)
        all_y.add(py)
        all_y.add(qy)
        for y in range(min(py, qy), max(py, qy)+1):
            for x in range(min(px, qx), max(px, qx) + 1):
                stones[y][x] = "#"

def move(y, x, s):
    if y+1 > max(all_y):
        raise OutOfBoundaryException
    if not s[y+1][x]:
        return (y+1, x)
    elif not s[y+1][x-1]:
        return (y + 1, x - 1)
    elif not s[y+1][x+1]:
        return (y + 1, x + 1)
    return (y, x)


iterations = 0
try:
    while True:
        pos = (0, 500)
        while (new_pos := move(pos[0], pos[1], stones)) != pos:
            pos = new_pos
        stones[pos[0]][pos[1]] = "o"
        iterations += 1
except OutOfBoundaryException:
    pass

for y in range(0, max(all_y)+1):
    for x in range(min(all_x), max(all_x)+1):
        if stones[y][x]:
            print(stones[y][x], end="")
        else:
            print(".", end="")
    print()

print(f"Part 1: {iterations}")
