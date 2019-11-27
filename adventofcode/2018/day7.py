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

    print(f'Part 1: {order}')


blockers = {}
steps = set()
order = ''
currently_running = {}
max_simultaneous_tasks = 5
task_base_time = 60

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

    second = 0
    while len(steps_sorted):
        finished_tasks = []
        for t in currently_running:
            if currently_running[t] == 0:
                finished_tasks.append(t)
        for ft in finished_tasks:
            for x in blockers:
                if ft in blockers[x]:
                    blockers[x].remove(ft)
            steps_sorted.remove(ft)
            order += ft
            del(currently_running[ft])

        non_blocked = [k for k in blockers if len(blockers[k]) == 0]
        non_blocked.sort()
        if non_blocked:
            max_to_start = max_simultaneous_tasks - len(currently_running)
            to_start = non_blocked[:max_to_start]
            for t in to_start:
                del (blockers[t])
                task_time = task_base_time + ord(t) - 64
                currently_running[t] = task_time
        for t in currently_running:
            currently_running[t] -= 1
        if currently_running:
            second += 1

    print(f'Part 2: {second}')
