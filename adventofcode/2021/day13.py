from typing import List

with open('input13.txt', 'r') as f:
    lines = [line.rstrip() for line in f]

pattern = lines[:lines.index('')]
instructions = lines[lines.index('')+1:]


def fold(data: List[List[str]], axis: str, value: int) -> List[List[str]]:
    if axis == 'y':
        for y in range(value+1, len(data)):
            for x in range(len(data[y])):
                if data[y][x] == '#':
                    data[len(data) - y - 1][x] = data[y][x]
        return data[0:value]
    if axis == 'x':
        for y in range(len(data)):
            for x in range(value + 1, len(data[y])):
                if data[y][x] == '#':
                    data[y][len(data[y]) - x - 1] = data[y][x]
        return [x[0:value] for x in data]

    return data


max_x = max([int(_.split(',')[0]) for _ in pattern])
max_y = max([int(_.split(',')[1]) for _ in pattern])
sheet = [[' ' for _ in range(max_x + 1)] for __ in range((max_y + 1))]

for point in pattern:
    sheet[int(point.split(',')[1])][int(point.split(',')[0])] = '#'

axis, value = instructions[0].split(' ')[-1].split('=')
sheet_1 = fold(sheet, axis, int(value))
print(f"Part 1: {sum([row.count('#') for row in sheet_1])}")

for instruction in instructions:
    axis, value = instruction.split(' ')[-1].split('=')
    sheet = fold(sheet, axis, int(value))

print("Part 2:")
for line in sheet:
    print(''.join(line))