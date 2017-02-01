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
from copy import deepcopy


class State:
    def __init__(self, level, pairs):
        self.level = level
        self.pairs = sorted(deepcopy(pairs))

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return 'level: {} - pairs: {}'.format(self.level, self.pairs)

    def __str__(self):
        return 'level: {} - pairs: {}'.format(self.level, self.pairs)


def parse_initial_state():
    with open('input11.txt', 'r') as f:
        contents = {}
        c = 1
        for line in f:
            instr = line.strip().replace(', and', '').replace(', ', ' ') \
                        .strip().split(' a ')[1:]
            content = []
            for i in instr:
                content.append(''.join([s[0] for s in i.split(' ')]))
            contents[c] = content
            c += 1

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


def validate_state(state, old_states):
    # TODO validate against valid and not visited
    # for all chips pair[0], it's ok if it's on the same level as
    # it's RTG OR if there are no other RTG:s there
    return True


def get_possible_moves(current_state, old_states):
    old_states.append(current_state)

    if current_state.level == 1:
        possible_levels = [2]
    elif current_state.level == 4:
        possible_levels = [3]
    else:
        possible_levels = [current_state.level - 1, current_state.level + 1]

    possibilities = []
    for level in possible_levels:
        print('level: {}'.format(level))
        # select ONE
        for x in range(2):
            for y in range(len(current_state.pairs)):
                if current_state.pairs[y][x] == current_state.level and abs(
                        level - current_state.level) == 1:
                    new_state = State(level=level, pairs=current_state.pairs)
                    new_state.pairs[y][x] += (level - current_state.level)
                    # print('adding {} to {} {}'.format(
                    #     level - current_state.level, y, x))
                    # print(new_state)
                    possibilities.append(new_state)

        # select TWO

        # We can bring AT MOST two items (no matter which) in ONE direction
        # select one or two of any type to bring THAT ARE ON THIS LEVEL

        # for p in current_state.pairs:
        #     print(p)
        #     # TODO return the states that's possible
        #
        #     new_pairs = []
        #     new_state = State(level=level, pairs=new_pairs)
        #     if validate_state(new_state, old_states=old_states):
        #         possibilities.append(new_state)

    for p in possibilities:
        print(p)
    return possibilities


floor = 1
instructions = []
# current_state = False
states = [parse_initial_state()]

print(states)

# keep states in the recursive algorithm or loop somehow
possible_moves = get_possible_moves(states[-1], [])
print(possible_moves)
