blockers = {}
steps = set()
order = ''

with open('input7.txt', 'r') as f:
    for line in f:
        row = line.strip().strip('Step ').strip(' can begin.').split(' must be finished before step ')
        if not row[1] in blockers:
            blockers[row[1]] = [row[0]]
        else:
            blockers[row[1]].append(row[0])
        steps.add(row[0])
        steps.add(row[1])

    steps_sorted = list(steps)
    steps_sorted.sort()

    for s in steps_sorted:
        if s not in blockers:
            blockers[s] = []

    while len(steps_sorted):
        non_blocked = [k for k in blockers if len(blockers[k]) == 0]
        next_step = min(non_blocked)
        steps_sorted.remove(next_step)
        for x in blockers:
            if next_step in blockers[x]:
                blockers[x].remove(next_step)
        del(blockers[next_step])
        order += next_step

    print(order)
