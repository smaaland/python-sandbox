from typing import List


def coordinates_visited(x: int, y: int, moves: List) -> List:

    visited: List = [(0, 0)]

    for move in moves:
        direction, steps = move[:1], int(move[1:])

        if direction == 'R':
            y_range = range(y, y+1)
            x_range = range(x+1, x + steps + 1)
        elif direction == 'L':
            y_range = range(y, y+1)
            x_range = range(x-1, x - steps - 1, -1)
        elif direction == 'U':
            y_range = range(y+1, y + steps + 1)
            x_range = range(x, x+1)
        elif direction == 'D':
            y_range = range(y-1, y - steps - 1, -1)
            x_range = range(x, x+1)
        else:
            break

        for y in y_range:
            for x in x_range:
                visited.append((x, y))

    return visited


def manhattan_distance(a: List, b: List) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


with open('input3.txt', 'r') as f:
    wires: List = []
    for line in f:
        wires.append(line.strip().split(','))

    points: List = []
    for i in range(len(wires)):
        points.append(coordinates_visited(x=0, y=0, moves=wires[i]))

    intersections = list(set(points[0]).intersection(points[1]))
    intersections.remove((0, 0))

    part_1 = min(manhattan_distance([0, 0], list(x)) for x in intersections)


print(f'Part 1: {part_1}')
