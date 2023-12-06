from functools import reduce

lines = [line.strip() for line in open("input6.txt", "r").readlines()]

times_1 = [int(x) for x in lines[0].split(":")[1].strip().split(" ") if x]
distances_1 = [int(x) for x in lines[1].split(":")[1].strip().split(" ") if x]
times_2 = [int("".join([str(x) for x in times_1]))]
distances_2 = [int("".join([str(x) for x in distances_1]))]


def get_ways_to_win(time, distance):
    ways_to_win = []
    for t, d in zip(time, distance):
        distances_travelled = []
        for i in range(1, t):
            distances_travelled.append(i * (t - i))
        ways_to_win.append(len([x for x in distances_travelled if x > d]))
    return ways_to_win


print(f"Part 1: {reduce(lambda x, y: x * y, get_ways_to_win(times_1, distances_1))}")
print(f"Part 2: {get_ways_to_win(times_2, distances_2)[0]}")
