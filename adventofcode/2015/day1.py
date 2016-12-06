with open('input1.txt', 'r') as f:
    level = 0
    for line in f:
        for c in line:
            if c == '(':
                level += 1
            elif c == ')':
                level -= 1

    print('Part 1: {}'.format(level))

with open('input1.txt', 'r') as f:
    level = 0
    counter = 0
    for line in f:
        for c in line:
            counter += 1
            if c == '(':
                level += 1
            elif c == ')':
                level -= 1
            if level < 0:
                break

print('Part 2: {}'.format(counter))
