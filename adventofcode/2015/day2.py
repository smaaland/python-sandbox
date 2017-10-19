with open('input2.txt', 'r') as f:
    total = 0
    for line in f:
        sides = [int(i) for i in line.split('x')]
        # normal sides
        total += 2 * sides[0] * sides[1] + 2 * sides[1] * sides[2] + \
            2 * sides[0] * sides[2]
        # area of the smallest side
        total += min([sides[0] * sides[1], sides[1] * sides[2],
                     sides[0] * sides[2]])
print(total)
