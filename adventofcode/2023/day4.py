lines = [line.strip() for line in open("input4.txt", "r").readlines()]

points = 0
number_of_cards = {i: 1 for i, _ in enumerate(lines)}

for i, line in enumerate(lines):
    numbers = line.split(":")[1].split("|")
    winning_numbers = [int(x) for x in numbers[0].strip().split(" ") if x]
    my_numbers = [int(x) for x in numbers[1].strip().split(" ") if x]
    intersection = list(set(winning_numbers) & set(my_numbers))
    if len(intersection):
        points += pow(2, len(intersection) - 1)
        for x in range(i + 1, i + 1 + len(intersection), 1):
            number_of_cards[x] += number_of_cards[i]

print(f"Part 1: {points}")
print(f"Part 2: {sum(number_of_cards.values())}")
