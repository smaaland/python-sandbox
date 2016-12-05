import re

with open('input3.txt', 'r') as f:
    possible = 0

    for line in f:
        parts = sorted([int(i) for i in re.split('\s+', line.strip())])

        if parts[0] + parts[1] > parts[2]:
            possible += 1

    print('Part 1: {}'.format(possible))

with open('input3.txt', 'r') as f:
    possible = 0

    data = []

    for line in f:

        data.append([int(i) for i in re.split('\s+', line.strip())])

        if len(data) == 3:
            for x in range(3):
                parts = sorted([data[y][x] for y in range(3)])
                if parts[0] + parts[1] > parts[2]:
                    possible += 1

            data = []

    print('Part 2: {}'.format(possible))
