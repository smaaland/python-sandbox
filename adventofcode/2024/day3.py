import math
import re


lines = open("input3.txt", "r").read()
sum = 0
sum_2 = 0

for s in re.findall(r"mul\(\d{1,3},\d{1,3}\)", lines):
    sum += math.prod([int(x) for x in re.findall(r"\d{1,3}", s)])

enabled = True
for s in re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", lines):
    if s == "do()":
        enabled = True
    elif s == "don't()":
        enabled = False
    else:
        if enabled:
            sum_2 += math.prod([int(x) for x in re.findall(r"\d{1,3}", s)])

print(f"Part 1: {sum}")
print(f"Part 2: {sum_2}")
