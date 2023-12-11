lines = [line.strip() for line in open("input9.txt", "r").readlines()]
next_values = []

for line in lines:
    values = [int(x) for x in line.split(" ")]
    to_sum = []
    while not all(x == 0 for x in values):
        to_sum.append(values[-1])
        values = [j - i for i, j in zip(values, values[1:])]
    next_values.append(sum(to_sum))
print(f"Part 1: {sum(next_values)}")

next_values = []
for line in lines:
    values = [int(x) for x in line.split(" ")]
    to_sum = []

    while not all(x == 0 for x in values):
        to_sum.append(values[0])
        values = [j - i for i, j in zip(values, values[1:])]
    current = 0
    for x in reversed(to_sum):
        current = x - current
    next_values.append(current)
print(f"Part 2: {sum(next_values)}")
