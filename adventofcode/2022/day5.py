import copy

lines = [line.strip("\n") for line in open('input5.txt', 'r').readlines()]

width = len(lines[0])
entries = int((width + 1) / 4)
stacks_1 = [[] for _ in range(entries)]

crates = lines[:lines.index('')]
instructions = lines[lines.index('')+1:]

for l in crates:
    for i in range(entries):
        j = (i*4)+1
        if l[j] != " ":
            stacks_1[i].append(l[j])

for s in stacks_1:
    s.pop()
    s.reverse()

stacks_2 = copy.deepcopy(stacks_1)

for i in instructions:
    j = i.split()
    for _ in range(int(j[1])):
        t = stacks_1[int(j[3]) - 1].pop()
        stacks_1[int(j[5]) - 1].append(t)

    t = stacks_2[int(j[3]) - 1][-int(j[1]):]
    for _ in range(int(j[1])):
        stacks_2[int(j[3]) - 1].pop()
    stacks_2[int(j[5]) - 1].extend(t)

print(f"Part 1: {''.join([s[-1:][0] for s in stacks_1])}")
print(f"Part 2: {''.join([s[-1:][0] for s in stacks_2])}")