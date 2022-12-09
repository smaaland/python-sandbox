from collections import defaultdict

lines = [line.strip("\n") for line in open('input7.txt', 'r').readlines()]

terminal_output = []
path = []
sizes = defaultdict(int)
part_1_total = 0
max_size = 100000
total_space = 70000000
update_size = 30000000
used_space = sizes['/']
free_space = total_space - used_space
space_needed = update_size - free_space


for line in lines:
    if line.startswith('$ cd'):
        directory = line.split()[-1]
        if directory == '..':
            path.pop()
        else:
            path.append(directory)
    elif line.startswith('$ ls'):
        continue
    else:
        size, _ = line.split()
        if size.isdigit():
            size = int(size)
            for i in range(len(path)):
                sizes['/'.join(path[:i + 1])] += size

options = []
for key, value in sizes.items():
    if value <= max_size:
        part_1_total += value
    if value > space_needed:
        options.append(value)

print(f"Part 1: {part_1_total}")
print(f"Part 2: {min(options)}")
