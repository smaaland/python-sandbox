# keep chips Therefore, it is assumed that you will follow procedure and
# keep chips connected to their corresponding RTG when they're in the same
# room, and away from other RTGs otherwise.

# Its capacity rating means it can carry at most yourself and two RTGs or
# microchips in any combination.

# the elevator will only function if it contains at least one RTG or microchip

# The elevator always stops on each floor to recharge, and this takes long
# enough that the items within it and the items on that floor can irradiate
# each other. (You can prevent this if a Microchip and its Generator end up
# on the same floor in this way, as they can be connected while the elevator
#  is recharging.)

# if a chip (0) is ever left in the same area as another RTG, and it's not
# connected to its own RTG, the chip will be fried.


class State:
    def __init__(self, level, pairs):
        self.level = level
        self.pairs = sorted(pairs)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


def parse_initial_state():
    with open('input11.txt', 'r') as f:
        contents = {}
        c = 1
        for line in f:
            instr = line.strip().replace(', and', '').replace(', ',
                                                              ' ').strip(

            ).split(
                ' a ')[1:]
            content = []
            for i in instr:
                content.append(''.join([s[0] for s in i.split(' ')]))
            contents[c] = content
            c += 1

        # print(contents)
        pairs = []

        for c in ['s', 'p', 't', 'r', 'c']:
            pair = {}
            for i in range(1, 5):
                for e in contents[i]:
                    if e[0] == c:
                        # microchip = 0, generator = 1
                        pair[0 if e[1] == 'm' else 1] = i
            pairs.append(list(pair.values()))

        return State(level=1, pairs=pairs)


def get_possible_moves(state):
    l = state.level

    if l == 1:
        possible_levels = [2]
    elif l == 4:
        possible_levels = [3]
    else:
        possible_levels = [l - 1, l + 1]

    possibilities = []
    for level in possible_levels:
        for p in state.pairs:
            # We can bring at most two items (no matter which) in ONE direction
            print(p)
            # TODO return the states that's possible

            # create a state and append to the possibilities list

    # TODO validate against valid and not visited
    return possibilities


floor = 1
instructions = []
current_state = False
states = []


states.append(parse_initial_state())
print(states)

# keep states in the recursive algorithm or loop somehow
possible_moves = get_possible_moves(states[-1])
print(possible_moves)
