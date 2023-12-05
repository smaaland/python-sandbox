lines = [line.strip() for line in open("input3.txt", "r").readlines()]


def adjacent_symbol(x1, x2, y1):
    for y in range(y1 - 1, y1 + 2, 1):
        for x in range(x1 - 1, x2 + 2, 1):
            try:
                if lines[y][x]:
                    if not (lines[y][x].isdigit() or lines[y][x] == "."):
                        return True
            except IndexError:
                pass
    return False


number_groups = {i: [] for i, _ in enumerate(lines)}
all_digits = {}
part_numbers = []

for y, line in enumerate(lines):
    digits = {i: c for i, c in enumerate(line) if c.isdigit()}
    all_digits[y] = digits
    digit_indexes = list(digits.keys())
    breaks = [
        i
        for i, (a, b) in enumerate(zip(digit_indexes, digit_indexes[1:]), 1)
        if b - a > 1
    ]
    groups = [digit_indexes[s:e] for s, e in zip([0] + breaks, breaks + [None])]
    for group in groups:
        if group:
            number_groups[y].append(group)
            if adjacent_symbol(group[0], group[-1], y):
                part_numbers.append(int("".join([digits[i] for i in group])))

print(f"Part 1: {sum(part_numbers)}")

gear_ratios = []
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "*":
            matches = []
            for _y in range(y - 1, y + 2, 1):
                for group in number_groups[_y]:
                    for _x in group:
                        if _x <= x + 1 and _x >= x - 1:
                            matches.append(
                                int("".join([all_digits[_y][i] for i in group]))
                            )
                            break
            if len(matches) == 2:
                gear_ratios.append(matches[0] * matches[1])

print(f"Part 2: {sum(gear_ratios)}")
