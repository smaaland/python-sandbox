from typing import List


def manhattan_distance(a: List, b: List) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


data = {}
counters = {}
sum_distances_threshold = 10000

counter = 0
with open('input6.txt', 'r') as f:
    for line in f:
        data[counter] = ([int(x) for x in line.strip().split(', ')])
        counter += 1

    min_x = min([data[r][0] for r in data])
    max_x = max([data[r][0] for r in data])
    min_y = min([data[r][1] for r in data])
    max_y = max([data[r][1] for r in data])

    matrix = [[None for _ in range(min_x, max_x + 1)] for _ in range(min_y, max_y + 1)]
    distances_matrix = [[0 for _ in range(min_x, max_x + 1)] for _ in range(min_y, max_y + 1)]

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            distances = {z: manhattan_distance([x, y], [data[z][0], data[z][1]]) for z in data}
            min_distance = min(distances.values())
            sum_distances = sum(distances.values())
            if sum_distances < sum_distances_threshold:
                distances_matrix[y - min_y][x - min_x] = 1
            min_keys = [key for key in distances if distances[key] == min_distance]

            if len(min_keys) > 1:
                matrix[y - min_y][x - min_x] = None
            else:
                matrix[y - min_y][x - min_x] = min_keys[0]

    on_the_edge = []
    on_the_edge.extend(matrix[0])
    on_the_edge.extend(matrix[len(matrix) - 1])
    on_the_edge.extend([s[0] for s in matrix])
    on_the_edge.extend([s[len(s) - 1] for s in matrix])
    on_the_edge = list(set([x for x in on_the_edge if x is not None]))

    all_distances = []
    for y in matrix:
        all_distances.extend(y)
    finite_distances = [x for x in all_distances if x not in on_the_edge and x is not None]

    for i in finite_distances:
        if i in counters:
            counters[i] += 1
        else:
            counters[i] = 1
    print(f'Part 1: {max(counters.values())}')

    all_sum_distances = []
    for y in distances_matrix:
        all_sum_distances.extend(y)
    print(f'Part 2: {sum(all_sum_distances)}')