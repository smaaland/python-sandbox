with open('input2.txt', 'r') as f:

    buttons = [['1', '2', '3'],
               ['4', '5', '6'],
               ['7', '8', '9']]
    sequence = []

    pos_x = 0
    pos_y = 0

    for line in f:

        print('Starting from {}'.format((pos_x + 1, pos_y + 1)))

        for c in line.strip(' '):
            if c == 'U':
                pos_y = pos_y - 1 if pos_y - 1 >= -1 else -1
            elif c == 'D':
                pos_y = pos_y + 1 if pos_y + 1 <= 1 else 1
            elif c == 'L':
                pos_x = pos_x - 1 if pos_x - 1 >= -1 else -1
            elif c == 'R':
                pos_x = pos_x + 1 if pos_x + 1 <= 1 else 1

        # Move the coordinates
        print(pos_x+1, pos_y+1)
        sequence.append(buttons[pos_y+1][pos_x+1])

    print(''.join(sequence))

