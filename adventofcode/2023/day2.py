from functools import reduce

lines = [line.strip() for line in open("input2.txt", "r").readlines()]

game_1 = {
    "red": 12,
    "green": 13,
    "blue": 14
}

possible_games = []
powers = []
for line in lines:
    minimum_needed = {}

    game_id = line.split(":")[0].split(" ")[1]
    games = line.split(":")[1].split(";")
    possible = True
    for reveal in games:
        sets = [s.strip() for s in reveal.split(",")]
        for s in sets:
            quantity, color = s.split(" ")
            if color not in minimum_needed:
                minimum_needed[color] = int(quantity)
            else:
                if minimum_needed[color] < int(quantity):
                    minimum_needed[color] = int(quantity)
            if color in game_1:
                if game_1[color] < int(quantity):
                    possible = False

            else:
                possible = False
    powers.append(reduce(lambda x, y: x*y, minimum_needed.values()))
    if possible:
        possible_games.append(int(game_id))

print(f"Part 1: {sum(possible_games)}")
print(f"Part 2: {sum(powers)}")
