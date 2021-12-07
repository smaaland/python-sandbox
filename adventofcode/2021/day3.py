from collections import Counter

with open('input3.txt', 'r') as f:
    lines = [line.rstrip() for line in f]

gamma = ''
epsilon = ''
for i in range(len(lines[0])):
    count = Counter([line[i] for line in lines])
    gamma += max(count, key=count.get)
    epsilon += min(count, key=count.get)

print(f"Part 1: {int(gamma, 2) * int(epsilon, 2)}")


lines_oxygen = lines
for i in range(len(lines_oxygen[0])):
    count = Counter([line[i] for line in lines_oxygen])
    lines_oxygen = [_ for _ in lines_oxygen if _[i] == max(count, key=count.get)]
    if len(lines_oxygen) == 1:
        break

lines_co2 = lines
for i in range(len(lines_co2[0])):
    count = Counter([line[i] for line in lines_co2])
    lines_co2 = [_ for _ in lines_co2 if _[i] == min(count, key=count.get)]
    if len(lines_co2) == 1:
        break

print(f"Part 2: {int(lines_oxygen[0], 2) * int(lines_co2[0], 2)}")