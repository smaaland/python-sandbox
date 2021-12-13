data = [int(x) for x in open("input7.txt").read().strip().split(",")]

costs_1 = {}
costs_2 = {}
for pos in range(len(data)):
    cost_1 = 0
    cost_2 = 0
    for p in data:
        steps = abs(p-pos)
        cost_1 += steps
        cost_2 += steps * (steps + 1) / 2
    costs_1[pos] = cost_1
    costs_2[pos] = cost_2

print(f"Part 1: {min(costs_1.values())}")
print(f"Part 2: {int(min(costs_2.values()))}")
