import math


def fuel(x: int) -> int:
    return math.floor(int(x)/3)-2


total: int = 0
total_2: int = 0

with open('input1.txt', 'r') as f:
    for line in f:
        fuel_consumption = fuel(int(line.strip()))
        total += fuel_consumption
        while fuel_consumption > 0:
            total_2 += fuel_consumption
            fuel_consumption = fuel(fuel_consumption)


print(f'Part 1: {total}')
print(f'Part 2: {total_2}')
