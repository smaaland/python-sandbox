struct = {}


def calculate_score(current):
    score = 0

    for x in range(-1, len(current) - 1):
        score += struct[current[x]][current[x + 1]]
        score += struct[current[x + 1]][current[x]]

    return score


def iterate(current, left, scores):
    if len(left):
        for p in left:
            iterate(current + [p], [x for x in left if x != p], scores)
    else:
        # Calculate score
        scores.append(calculate_score(current))
    return scores


with open('input13.txt', 'r') as f:
    for line in f:
        parts = line.split(' ')
        p1 = parts[0]
        p2 = parts[-1].split('.')[0]
        val = int(parts[3]) if parts[2] == 'gain' else -int(parts[3])
        if not p1 in struct:
            struct[p1] = {}
        struct[p1][p2] = val

for p1 in struct:
    scores1 = iterate([p1], [x for x in struct if x != p1], [])

print(max(scores1))


struct['smaaland'] = {}
for x in struct:
    struct['smaaland'][x] = 0
    struct[x]['smaaland'] = 0


for p1 in struct:
    scores2 = iterate([p1], [x for x in struct if x != p1], [])

print(max(scores2))
