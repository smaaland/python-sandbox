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

errors = []
for line in lines:
    stack = []
    for c in line:
        if c in matching_chars.values():
            stack.append(c)
        else:
            if stack.pop() != matching_chars[c]:
                errors.append(c)
                continue

print(f"Part 1: {sum([points[k] for k in errors])}")


