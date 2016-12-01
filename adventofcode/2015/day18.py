c = 0
r = 0
current_state = {}

with open('input18.txt', 'r') as f:
    for line in f:
        c = 0

        if r not in current_state:
            current_state[r] = {}

        for s in line.split('\n')[0]:
            current_state[r][c] = s
            c += 1
        r += 1


def neighbours(state, col, row):
    n = 0
    for x in range(col-1, col+2):
        for y in range(row-1, row+2):
            try:
                if not (col == x and row == y):
                    if state[x][y] == '#':
                        # if col == 1 and row == 1:
                            # print(x,y)
                        n += 1
            except KeyError:
                pass
    return n


def rec(state_orig, iterations):
    state = {}
    for x in range(100):
        for y in range(100):
            if x not in state:
                state[x] = {}
            state[x][y] = state_orig[x][y]

    for x in range(100):
        for y in range(100):
            n = neighbours(state_orig, x, y)
            if state[x][y] == '#':
                # it's on now
                if n == 2 or n == 3:
                    # Should be on in the next state
                    pass
                else:
                    # Should be off in the next state
                    state[x][y] = '.'
            else:
                # It's off now
                if n == 3:
                    # Should be on in the next state
                    state[x][y] = '#'
                else:
                    # Should be off in the next state
                    pass

    state[0][0] = '#'
    state[0][99] = '#'
    state[99][0] = '#'
    state[99][99] = '#'

    iterations += 1
    if iterations == 100:
        # Count the lights and break
        on = 0
        for _x in range(100):
            for _y in range(100):
                if state[_x][_y] == '#':
                    on += 1
        print('---', on)
        return
    else:
        rec(state, iterations)
current_state[0][0] = '#'
current_state[0][99] = '#'
current_state[99][0] = '#'
current_state[99][99] = '#'
rec(current_state, 0)