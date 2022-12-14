lines = [line.strip().split() for line in open("input9.txt", "r").readlines()]
print(lines)
hx, hy, tx, ty = 0, 0, 0, 0
tail_visits = set()
tail_visits.add((tx, ty))


def touching():
    return abs(hx-tx) <= 1 and abs(hy-ty) <= 1


def move_tail():
    global hx, hy, tx, ty
    if hx > tx:
        tx += 1
    elif hx < tx:
        tx -= 1
    if hy > ty:
        ty += 1
    elif hy < ty:
        ty -= 1


for l in lines:
    for _ in range(int(l[1])):
        if l[0] == "R":
            hx += 1
        if l[0] == "L":
            hx -= 1
        if l[0] == "U":
            hy += 1
        if l[0] == "D":
            hy -= 1
        if not touching():
            move_tail()
            tail_visits.add((tx, ty))

print(f"Part 1: {len(tail_visits)}")