lines = []
with open('input1.txt', 'r') as f:
    for line in f:
        lines.append(line.strip())

    sum = 0
    for line in lines:
        operator = line[0]
        val = int(line[1:])
        if operator == '+':
            sum += val
        elif operator == '-':
            sum -= val
    print(f'Part 1: {sum}')

    sum = 0
    visited = set()
    while True:
        for line in lines:
            operator = line[0]
            val = int(line[1:])
            if operator == '+':
                sum += val
            elif operator == '-':
                sum -= val
            if sum in visited:
                print(f'Part 2: {sum}')
                exit()
            visited.add(sum)

