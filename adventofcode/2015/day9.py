input = 'AlphaCentauri to Snowdin = 66:AlphaCentauri to Tambi = 28:AlphaCentauri to Faerun = 60:AlphaCentauri to Norrath = 34:AlphaCentauri to Straylight = 34:AlphaCentauri to Tristram = 3:AlphaCentauri to Arbre = 108:Snowdin to Tambi = 22:Snowdin to Faerun = 12:Snowdin to Norrath = 91:Snowdin to Straylight = 121:Snowdin to Tristram = 111:Snowdin to Arbre = 71:Tambi to Faerun = 39:Tambi to Norrath = 113:Tambi to Straylight = 130:Tambi to Tristram = 35:Tambi to Arbre = 40:Faerun to Norrath = 63:Faerun to Straylight = 21:Faerun to Tristram = 57:Faerun to Arbre = 83:Norrath to Straylight = 9:Norrath to Tristram = 50:Norrath to Arbre = 60:Straylight to Tristram = 27:Straylight to Arbre = 81:Tristram to Arbre = 90'

destinations = []
distances = {}


def rec(current, left, total):
    if len(left) == 0:
        return total

    t = []
    for x in left:
        t.append(rec(x, [y for y in left if not x == y], total + int(distances[current][x])))

    return max(t)


for line in input.split(':'):
    print(line)
    dist = line.split(' = ')[1]
    print(dist)
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

print(destinations)
print(distances)


total_distances = []
for start in destinations:
    middle = [x for x in destinations if x != start]
    print(middle)

    d = rec(start, middle, 0)
    total_distances.append(d)


    print('---')
print(max(total_distances))