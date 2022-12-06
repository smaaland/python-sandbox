lines = [line.strip() for line in open('input1.txt', 'r').readlines()]

max_sum = 0
total_sums = []
elf_sum = 0
for l in lines:
    if l:
        elf_sum += int(l)
    else:
        if elf_sum > max_sum:
            max_sum = elf_sum
        total_sums.append(elf_sum)
        elf_sum = 0

total_sums.sort(reverse=True)

print(f"Part 1: {max_sum}")
print(f"Part 2: {sum(total_sums[:3])}")