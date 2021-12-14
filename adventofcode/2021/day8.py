with open('input8.txt', 'r') as f:
    lines = [[part.split() for part in line.rstrip().split(" | ")] for line in f]

print(f"Part 1: {sum(len(w) in [2, 3, 4, 7] for l in lines for w in l[1])}")

values = []
for line in lines:
    digits = {k: None for k in range(10)}
    for digit in line[0]:
        if len(digit) == 2:
            digits[1] = sorted(digit)
        if len(digit) == 3:
            digits[7] = sorted(digit)
        if len(digit) == 4:
            digits[4] = sorted(digit)
        if len(digit) == 7:
            digits[8] = sorted(digit)
    for digit in line[0]:
        if len(digit) == 6:
            if set(digits[4]).issubset(list(digit)):
                digits[9] = sorted(digit)
            elif set(digits[1]).issubset(list(digit)):
                digits[0] = sorted(digit)
            else:
                digits[6] = sorted(digit)
    for digit in line[0]:
        if len(digit) == 5:
            if set(digits[1]).issubset(list(digit)):
                digits[3] = sorted(digit)
            elif set(digit).issubset(digits[6]):
                digits[5] = sorted(digit)
            else:
                digits[2] = sorted(digit)

    val = ''
    for output in line[1]:
        val += [str(k) for k, v in digits.items() if v == sorted(output)][0]
    values.append(int(val))

print(f"Part 2: {sum(values)}")
