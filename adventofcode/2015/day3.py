with open('input3.txt', 'r') as f:
    total = 0
    coordinates = [(0, 0)]
    for line in f:
        for c in line:
            last = coordinates[-1]
            if c == '<':
                coordinates.append((last[0]-1, last[1]))
            elif c == '>':
                coordinates.append((last[0] + 1, last[1]))
            elif c == '^':
                coordinates.append((last[0], last[1] + 1))
            elif c == 'v':
                coordinates.append((last[0], last[1] - 1))

    print(len(set(coordinates)))