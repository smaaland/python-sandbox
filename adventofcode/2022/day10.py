from collections import defaultdict

lines = [line.strip() for line in open("input10.txt", "r").readlines()]
x = 1
ptr = 0
sig_str = 0


executions = defaultdict(str)

for i in range(len(lines)):
    if lines[i].split()[0] == "addx":
        executions[ptr+2] = lines[i]
        ptr += 2
    else:
        ptr += 1


for i in range(max(executions)+1):
    if executions[i]:
        parts = executions[i].split()
        if parts[0] == "addx":
            x += int(parts[1])
    if (i + 1) == 20 or (i + 1 + 20) % 40 == 0:
        sig_str += (i+1) * x


print(f"Part 1: {sig_str}")