from collections import Counter
from typing import List

data = [int(x) for x in open("input6.txt").read().strip().split(",")]


def solve(data: List[int], days: int) -> int:
    counter = Counter(data)
    for day in range(days):
        counter[(day + 7) % 9] += counter[day % 9]
    return sum(counter.values())


print(f"Part 1: {solve(data, 80)}")
print(f"Part 2: {solve(data, 256)}")
