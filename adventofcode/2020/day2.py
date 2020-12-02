import re

with open('input2.txt', 'r') as f:
    lines = [line.rstrip() for line in f]

p = re.compile('(\d*)-(\d*) (\w): (\w*)')

part_1 = 0
part_2 = 0

for line in lines:
    first, last, char, _input = p.match(line).groups()
    if int(first) <= _input.count(char) <= int(last):
        part_1 += 1
    if (_input[int(first)-1] == char) ^ (_input[int(last)-1] == char):
        part_2 += 1

print(f'Part 1: {part_1}')
print(f'Part 2: {part_2}')
