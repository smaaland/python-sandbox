struct = {}

with open('input13.txt', 'r') as f:

    for line in f:
        # print(line)
        parts = line.split(' ')
        p1 = parts[0]
        p2 = parts[-1].split('.')[0]
        val = int(parts[3]) if parts[2] == 'gain' else -int(parts[3])
        if not p1 in struct:
            struct[p1] = {}
        struct[p1][p2] = val

struct['smaaland'] = {}

for x in struct:
    struct['smaaland'][x] = 0
    struct[x]['smaaland'] = 0

# print(struct)
scores = []


def calculateScore(current):
    score = 0

    for x in range(-1, len(current)-1):
        score += struct[current[x]][current[x+1]]
        score += struct[current[x+1]][current[x]]

    return score

def iterate(current, left):
    # print(current)
    # print(left)
    if len(left):
        for p in left:
            # TODO append won't work
            iterate(current + [p], [x for x in left if x != p])
    else:
        # Calculate score
        # print(current)
        scores.append(calculateScore(current))

for p1 in struct:
    iterate([p1], [x for x in struct if x != p1])

print(max(scores))