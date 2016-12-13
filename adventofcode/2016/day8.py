def shift(s, val):
    val %= len(s)
    return s[-val:] + s[:len(s) - val] if val != 0 else s


def pretty_print(matrix):
    for y in range(6):
        s = ''
        for x in range(50):
            if matrix[y][x] == 1:
                s += '█'
            else:
                s += ' '
        print(s)


with open('input8.txt', 'r') as f:
    matrix = [[0 for _ in range(50)] for _ in range(6)]

    for line in f:
        parts = line.strip().split(' ')
        if parts[0] == 'rect':
            width, height = [int(i) for i in parts[1].split('x')]
            for y in range(height):
                for x in range(width):
                    matrix[y][x] = 1
        elif parts[1] == 'row':
            y = int(parts[2].split('=')[1])
            val = int(parts[4])
            shifted = shift([matrix[y][x] for x in range(50)], val)
            matrix[y] = shifted
        elif parts[1] == 'column':
            x = int(parts[2].split('=')[1])
            val = int(parts[4])
            shifted = shift([matrix[y][x] for y in range(6)], val)
            for y in range(6):
                matrix[y][x] = shifted[y]

    count = 0
    for y in range(6):
        for x in range(50):
            if matrix[y][x] == 1:
                count += 1
    print('Part 1: {}'.format(count))
    print('Part 2:')
    pretty_print(matrix)
