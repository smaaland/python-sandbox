lines = [line.strip() for line in open("input3.txt", "r").readlines()]


def adjacent(x1, x2, y1):
    for y in range(y1 - 1, y1 + 2, 1):
        for x in range(x1 - 1, x2 + 2, 1):
            try:
                if lines[y][x]:
                    if not (lines[y][x].isdigit() or lines[y][x] == "."):
                        return True
            except IndexError:
                pass
    return False


part_numbers = []
for y, line in enumerate(lines):
    digits = {i: c for i, c in enumerate(line) if c.isdigit()}
    digit_indexes = list(digits.keys())
    breaks = [
        i
        for i, (a, b) in enumerate(zip(digit_indexes, digit_indexes[1:]), 1)
        if b - a > 1
    ]
    groups = [digit_indexes[s:e] for s, e in zip([0] + breaks, breaks + [None])]
    for group in groups:
        if group:
            if adjacent(group[0], group[-1], y):
                part_numbers.append(int("".join([digits[i] for i in group])))

print(f"Part 1: {sum(part_numbers)}")
