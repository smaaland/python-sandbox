lines = [line.strip() for line in open("input1.txt", "r").readlines()]

calibration_values = []

for line in lines:
    left, right = "", ""
    for c in line:
        if c.isdigit():
            left = c
            break
    for c in reversed(line):
        if c.isdigit():
            right = c
            break
    calibration_values.append(int(left + right))

print(f"Part 1: {sum(calibration_values)}")

mapping = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def find_int(input_str, reversed_keys=False):
    for k, v in mapping.items():
        if reversed_keys:
            k = k[::-1]
        if input_str.startswith(k):
            return v
    return None


calibration_values = []
for line in lines:
    left, right = "", ""
    for i, c in enumerate(line):
        if c.isdigit():
            left = c
            break
        else:
            found = find_int(line[i:])
            if found:
                left = found
                break
    for i, c in enumerate(line[::-1]):
        if c.isdigit():
            right = c
            break
        else:
            found = find_int(line[::-1][i:], reversed_keys=True)
            if found:
                right = found
                break
    calibration_values.append(int(left + right))

print(f"Part 2: {sum(calibration_values)}")

