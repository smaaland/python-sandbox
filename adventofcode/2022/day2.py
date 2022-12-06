lines = [line.strip().split() for line in open('input2.txt', 'r').readlines()]
data = [(ord(line[0])-65, ord(line[1])-88) for line in lines]
part_1_score = 0
part_2_score = 0

for x, y in data:
    if x == y:  # draw
        part_1_score += (y + 1 + 3)
    elif (y-x) % 3 == 1:  # win
        part_1_score += (y + 1 + 6)
    else:  # lose
        part_1_score += (y + 1 + 0)

    if y == 0:  # lose
        part_2_score += (((x-1) % 3) + 1 + 0)
    elif y == 1:  # draw
        part_2_score += (x + 1 + 3)
    else:   # win
        part_2_score += (((x + 1) % 3) + 1 + 6)


print(f"Part 1: {part_1_score}")
print(f"Part 2: {part_2_score}")
