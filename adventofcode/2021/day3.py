with open('input3.txt', 'r') as f:
    lines = [line.rstrip() for line in f]

ones = [0] * 12
zeros = [0] * 12

for line in lines:
    for i, d in enumerate(line):
        if int(d) == 0:
            zeros[i] += 1
        if int(d) == 1:
            ones[i] += 1
gamma = ''
epsilon = ''
for i in range(12):
    gamma += '1' if ones[i] > zeros[i] else '0'
    epsilon += '1' if ones[i] < zeros[i] else '0'

print(f"Part 1: {int(gamma, 2) * int(epsilon, 2)}")