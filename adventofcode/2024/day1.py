lines = [line.strip() for line in open("input1.txt", "r").readlines()]

left = []
right = []
diffs = []
similarities = []

for line in lines:
    l, r = [int(x) for x in line.split()]
    left.append(l)
    right.append(r)

for a, b in zip(sorted(left), sorted(right)):
    diffs.append(abs(a - b))

for l in left:
    similarities.append(l * right.count(l))

print(f"Part 1: {sum(diffs)}")
print(f"Part 2: {sum(similarities)}")
