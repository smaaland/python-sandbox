input = range(134792, 675810+1)

possible_combinations = 0


def has_adjacent(input):
    for x in range(len(input)-1):
        if input[x] == input[x+1]:
            return True
    return False


def never_decrease(input):
    last = '0'
    for x in input:
        if x < last:
            return False
        last = x
    return True


for r in input:
    if has_adjacent(str(r)) and never_decrease(str(r)):
        possible_combinations += 1

print(f'Part 1: {possible_combinations}')