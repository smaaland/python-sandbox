lines = [line.strip() for line in open("input5.txt", "r").readlines()]


def run(seed_range):
    for line in lines:
        if line.startswith("seeds: "):
            if seed_range:
                it = iter([int(x) for x in line.split(": ")[1].split(" ")])
                seeds = []
                for x, y in zip(it, it):
                    for n in range(x, x + y):
                        seeds.append(n)
            else:
                seeds = [int(x) for x in line.split(": ")[1].split(" ")]
        elif line == "":
            continue
        elif line.endswith(" map:"):
            moved = [False for _ in seeds]
            source, _, destination = line.split(" ")[0].split("-")
        else:
            destination_range_start, source_range_start, range_length = [
                int(x) for x in line.split(" ")
            ]
            for i, seed in enumerate(seeds):
                if not moved[i]:
                    if source_range_start <= seed < source_range_start + range_length:
                        seeds[i] = destination_range_start + seed - source_range_start
                        moved[i] = True
    return seeds


print(f"Part 1: {min(run(seed_range=False))}")
print(f"Part 2: {min(run(seed_range=True))}")
