lines = [line.strip() for line in open('input3.txt', 'r').readlines()]
priorities = []
priorities_2 = []


for l in lines:
    left = l[:int(len(l)/2)]
    right = l[int(len(l)/2):]
    intersection = set(left).intersection(right)
    for i in intersection:
        if i.isupper():
            priorities.append(ord(i)-38)
        else:
            priorities.append(ord(i)-96)


for x, y, z in zip(lines[::3], lines[1::3], lines[2::3]):
    intersection = set(x).intersection(y).intersection(z)
    for i in intersection:
        if i.isupper():
            priorities_2.append(ord(i)-38)
        else:
            priorities_2.append(ord(i)-96)


print(f"Part 1: {sum(priorities)}")
print(f"Part 2: {sum(priorities_2)}")

