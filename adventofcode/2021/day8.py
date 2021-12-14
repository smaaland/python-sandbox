with open('input8.txt', 'r') as f:
    lines = [[part.split() for part in line.rstrip().split(" | ")] for line in f]

print(f"Part 1 {sum(len(w) in [2, 3, 4, 7] for l in lines for w in l[1])}")
