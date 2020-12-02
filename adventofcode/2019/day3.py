from typing import List, Dict, Tuple, Any


def coordinates_visited(moves: List) -> Tuple[List[Any], Dict[Any, Any]]:

    visited: List = [(0, 0)]
    distances: Dict = {}
    x: int = 0
    y: int = 0
    distance = 0

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
                distance += 1
                if f"{x},{y}" not in distances:
                    distances[f"{x},{y}"] = distance
                else:
                    distances[f"{x},{y}"] = min(distances[f"{x},{y}"], distance)
                visited.append((x, y))

    return visited, distances


def manhattan_distance(a: List, b: List) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


with open('input3.txt', 'r') as f:
    wires: List = []
    for line in f:
        wires.append(line.strip().split(','))

    points: List = []
    distances: Dict[str, int] = {}
    for i in range(len(wires)):
        visited, _distances = coordinates_visited(moves=wires[i])
        points.append(visited)
        for k, v in _distances.items():
            distances[k] = v if k not in distances else distances[k] + v

    intersections = list(set(points[0]).intersection(points[1]))
    intersections.remove((0, 0))

    part_1 = min(manhattan_distance([0, 0], list(key)) for key in intersections)
    part_2 = min([distances[f'{key[0]},{key[1]}'] for key in intersections])

print(f'Part 1: {part_1}')
print(f'Part 2: {part_2}')
