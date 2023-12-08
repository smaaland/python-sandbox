import math

lines = [line.strip() for line in open("input8.txt", "r").readlines()]

instructions = lines[0]
network_input = lines[2:]
network = {}

for line in network_input:
    from_node, to_nodes = line.split(" = ")
    l, r = to_nodes.replace("(", "").replace(")", "").split(", ")
    network[from_node] = {"L": l, "R": r}

current = "AAA"
found = False
iterations = 0

while not found:
    for i in instructions:
        current = network[current][i]
        iterations += 1
        if current == "ZZZ":
            found = True
            break

print("Part 1:", iterations)

current = [n for n in [x.split(" = ")[0] for x in network_input] if n.endswith("A")]
iterations = 0
found = False

loop_lengths = []
for j, c in enumerate(current):
    iterations = 0
    while not current[j].endswith("Z"):
        for i in instructions:
            current[j] = network[current[j]][i]
            iterations += 1
            if current[j].endswith("Z"):
                break
    loop_lengths.append(iterations)

print("Part 2:", math.lcm(*loop_lengths))
