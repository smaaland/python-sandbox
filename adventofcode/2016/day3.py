import re

with open('input3.txt', 'r') as f:
    possible = 0

    for line in f:
        parts = sorted([int(i) for i in re.split('\s+', line.strip())])

        if parts[0] + parts[1] > parts[2]:
            possible += 1

    print('Part 1: {}'.format(possible))
