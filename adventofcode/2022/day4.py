lines = [line.strip() for line in open('input4.txt', 'r').readlines()]
total_overlaps = 0
partial_overlaps = 0

for l in lines:
    a, b = [x for x in l.split(",")]
    i = [int(x) for x in a.split("-")]
    j = [int(x) for x in b.split("-")]

    left = set([x for x in range(i[0], i[1]+1)])
    right = set([x for x in range(j[0], j[1] + 1)])
    if left.issubset(right) or right.issubset(left):
        total_overlaps += 1
    if left.intersection(right):
        partial_overlaps += 1


print(f"Part 1: {total_overlaps}")
print(f"Part 2: {partial_overlaps}")