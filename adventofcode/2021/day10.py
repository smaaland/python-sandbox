import math

with open('input10.txt', 'r') as f:
    lines = [line.rstrip() for line in f]

matching_chars = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
completion_points = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}

errors = []
completion_scores = []

for line in lines:
    stack = []
    error = False
    for c in line:
        if c in matching_chars.values():
            stack.append(c)
        else:
            if stack.pop() != matching_chars[c]:
                errors.append(c)
                error = True
                continue
    if not error:
        score = 0
        for c in reversed(stack):
            score = score * 5 + completion_points[c]
        completion_scores.append(score)

print(f"Part 1: {sum([points[k] for k in errors])}")
print(f"Part 2: {sorted(completion_scores)[math.floor(len(completion_scores)/2)]}")

