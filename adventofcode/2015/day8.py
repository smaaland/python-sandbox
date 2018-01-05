total = 0
total_2 = 0
with open('input8.txt', 'r') as f:
    for line in f:
        total += len(line[:-1]) - len(eval(line))
        total_2 += (2 + line.count('\\') + line.count('"'))

print(total)
print(total_2)
