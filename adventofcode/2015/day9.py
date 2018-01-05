destinations = []
distances = {}


def rec_max(current, left, total):
    if len(left) == 0:
        return total

    t = []
    for x in left:
        t.append(rec_max(x, [y for y in left if not x == y], total + int(distances[current][x])))

    return max(t)


def rec_min(current, left, total):
    if len(left) == 0:
        return total

    t = []
    for x in left:
        t.append(rec_min(x, [y for y in left if not x == y], total + int(distances[current][x])))

    return min(t)


with open('input9.txt', 'r') as f:
    for line in f:
        dist = line.split(' = ')[1]
        pl = line.split(' = ')[0].split(' to ')
        destinations.append(pl[0])
        destinations.append(pl[1])

        if not pl[0] in distances:
            distances[pl[0]] = {}
        distances[pl[0]][pl[1]] = dist

        if not pl[1] in distances:
            distances[pl[1]] = {}
        distances[pl[1]][pl[0]] = dist

destinations = set(destinations)

total_distances = []
for start in destinations:
    middle = [x for x in destinations if x != start]
    d = rec_min(start, middle, 0)
    total_distances.append(d)
print(min(total_distances))


total_distances = []
for start in destinations:
    middle = [x for x in destinations if x != start]
    d = rec_max(start, middle, 0)
    total_distances.append(d)
print(max(total_distances))
