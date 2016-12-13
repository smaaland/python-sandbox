with open('input2.txt', 'r') as f:

    buttons = [['1', '2', '3'],
               ['4', '5', '6'],
               ['7', '8', '9']]
    sequence = []

    pos_x = 0
    pos_y = 0

    for line in f:

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
        sequence.append(buttons[pos_y+1][pos_x+1])

    print('Part 1: ' + ''.join(sequence))

# Part 2
with open('input2.txt', 'r') as f:

    def can_i_go(direction, x, y):
        if direction == 'U':
            if x == 2 and y > 0:
                return True
            elif (x == 1 or x == 3) and y > 1:
                return True
            else:
                return False
        elif direction == 'D':
            if x == 2 and y < 4:
                return True
            elif (x == 1 or x == 3) and y < 3:
                return True
            else:
                return False
        elif direction == 'L':
            if y == 2 and x > 0:
                return True
            elif (y == 1 or y == 3) and x > 1:
                return True
            else:
                return False
        elif direction == 'R':
            if y == 2 and x < 4:
                return True
            elif (y == 1 or y == 3) and x < 3:
                return True
            else:
                return False
        return False

    buttons = [['', '', '1', '', ''],
               ['', '2', '3', '4', ''],
               ['5', '6', '7', '8', '9'],
               ['', 'A', 'B', 'C', ''],
               ['', '', 'D', '', ''],
               ]
    sequence = []

    pos_x = 0
    pos_y = 2

    for line in f:

        for c in line.strip(' '):
            if can_i_go(c, pos_x, pos_y):
                if c == 'U':
                    pos_y -= 1
                elif c == 'D':
                    pos_y += 1
                elif c == 'L':
                    pos_x -= 1
                elif c == 'R':
                    pos_x += 1

        sequence.append(buttons[pos_y][pos_x])

    print('Part 2: ' + ''.join(sequence))