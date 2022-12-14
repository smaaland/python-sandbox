lines = [line.strip().split() for line in open("input9.txt", "r").readlines()]
knots = [[0, 0] for _ in range(10)]
tail_visits = set()
tail_visits_2 = set()
tail_visits.add(tuple(knots[1]))
tail_visits_2.add(tuple(knots[-1]))


def touching(hx, hy, tx, ty):
    return abs(hx-tx) <= 1 and abs(hy-ty) <= 1


def move_tail(hx, hy, tx, ty):
    if hx > tx:
        tx += 1
    elif hx < tx:
        tx -= 1
    if hy > ty:
        ty += 1
    elif hy < ty:
        ty -= 1
    return [tx, ty]


for l in lines:
    for _ in range(int(l[1])):
        if l[0] == "R":
            knots[0][0] += 1
        if l[0] == "L":
            knots[0][0] -= 1
        if l[0] == "U":
            knots[0][1] += 1
        if l[0] == "D":
            knots[0][1] -= 1
        for i in range(len(knots) - 2 + 1):
            if not touching(knots[i][0], knots[i][1], knots[i+1][0], knots[i+1][1]):
                new_pos = move_tail(knots[i][0], knots[i][1], knots[i+1][0], knots[i+1][1])
                knots[i+1] = new_pos
        tail_visits.add(tuple(knots[1]))
        tail_visits_2.add(tuple(knots[-1]))


print(f"Part 1: {len(tail_visits)}")
print(f"Part 2: {len(tail_visits_2)}")