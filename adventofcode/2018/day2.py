from collections import Counter

lines = []
with open('input2.txt', 'r') as f:
    for line in f:
        lines.append(line.strip())

    twos = 0
    threes = 0
    for line in lines:
        d = Counter(line)
        if 2 in d.values():
            twos += 1
        if 3 in d.values():
            threes += 1
    print(f'Part 1: {twos * threes}')

    for i in range(0, len(lines)):
        for j in range(i+1, len(lines)):
            if sum(a != b for a, b in zip(lines[i], lines[j])) == 1:
                ans = "".join([a for a, b in zip(lines[i], lines[j]) if a == b])
                print(f'Part 2: {ans}')

