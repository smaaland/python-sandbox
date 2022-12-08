message = open('input6.txt', 'r').read().strip("\n")
window_size_1 = 4
window_size_2 = 14

for i in range(len(message) - window_size_1 + 1):
    if len(set(message[i: i + window_size_1])) == window_size_1:
        part_1 = i + window_size_1
        break

for i in range(len(message) - window_size_2 + 1):
    if len(set(message[i: i + window_size_2])) == window_size_2:
        part_2 = i + window_size_2
        break

print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
