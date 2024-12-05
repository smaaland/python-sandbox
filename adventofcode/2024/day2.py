from typing import List


lines = [[int(x) for x in line.strip().split()] for line in open("input2.txt", "r").readlines()]

safe = 0
safe_with_dampener = 0

def is_safe(l: List) -> bool:
    return (all(x > 0 for x in l) or all(x < 0 for x in l)) and all(1 <= abs(x) <= 3 for x in l)

def get_diffs(l: List[int]) -> List[int]:
    return [a-b for a, b in zip(l, l[1:])]

for line in lines:
    diffs = get_diffs(line)
    if is_safe(diffs):
        safe += 1
        safe_with_dampener += 1
    else:
        for i in range(len(line)):
            if is_safe(get_diffs(line[:i] + line[i+1:])):
                safe_with_dampener += 1
                break

print(f"Part 1: {safe}")
print(f"Part 2: {safe_with_dampener}")
