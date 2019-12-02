import copy
from typing import List


def compute(data: List[int]):
    index = 0
    while data[index] != 99:
        if data[index] == 1:
            data[data[index+3]] = data[data[index+1]] + data[data[index+2]]
        elif data[index] == 2:
            data[data[index+3]] = data[data[index+1]] * data[data[index+2]]
        else:
            return None
        index += 4
    return data[0]


with open('input2.txt', 'r') as f:
    input_str: str = ''
    for line in f:
        input_str += line.strip()

org_data: List[int] = [int(i) for i in input_str.split(',')]

data: List[int] = copy.copy(org_data)
data[1] = 12
data[2] = 2
computed_1 = compute(data)

noun: int = 0
found: bool = False
computed_2: int = False

while not found:
    for verb in range(noun+1):
        data = copy.copy(org_data)
        data[1] = noun
        data[2] = verb
        if compute(data) == 19690720:
            computed_2 = (100 * noun) + verb
            found = True
            break
    noun += 1

print(f'Part 1: {computed_1}')
print(f'Part 2: {computed_2}')
