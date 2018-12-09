import re

lines = []
with open('input3.txt', 'r') as f:
    for line in f:
        lines.append(line.strip())

    fabric = [[0 for _ in range(1000)] for _ in range(1000)]
    p = re.compile(r'\d+')

    for line in lines:
        claim, left, top, width, height = [int(x) for x in p.findall(line)]
        for x in range(left, width+left):
            for y in range(top, height+top):
                fabric[x][y] += 1

    multiple_claims = 0
    for x in fabric:
        for y in x:
            if y > 1:
                multiple_claims += 1
    print(f'Part 1: {multiple_claims}')

    for line in lines:
        claim, left, top, width, height = [int(x) for x in p.findall(line)]
        possible = True
        for x in range(left, width+left):
            for y in range(top, height+top):
                if fabric[x][y] != 1:
                    possible = False
        if possible:
            print(f'Part 2: {claim}')
            break


