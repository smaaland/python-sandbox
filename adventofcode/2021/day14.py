import string
from collections import Counter
from typing import Dict

lines = [line.strip() for line in open('input14.txt', 'r').readlines()]
template = lines[0]
rules = [rule.split(' ') for rule in lines[2:]]
rules = {a: (a[0]+c,c+a[1]) for a,b,c in rules}
pairs = [''.join(p) for p in zip(template, template[1:])]

# print(rules)
# print(pairs)

# total the pairs created by substitution
def run(steps):
    ctr = Counter(pairs)
    # print(ctr)
    for i in range(steps):
        newCtr = {key : 0 for key in rules.keys()}
        # print(newCtr)
        for key, value in ctr.items():
            newCtr[rules[key][0]] += value
            newCtr[rules[key][1]] += value
        ctr = newCtr

    letterTotals = {letter : 0 for letter in list(string.ascii_uppercase)}
    for key, value in ctr.items():
        letterTotals[key[0]] += value

    # the last character in the template gets another count
    letterTotals[template[-1]] += 1

    lmax = max(letterTotals.values())
    lmin = min([value for value in letterTotals.values() if value > 0])
    return lmax - lmin

print('part 1:', run(10))
print('part 2:', run(40))

with open('input14.txt', 'r') as f:
    lines = [line.rstrip() for line in f]

# print(lines)
pairs = [''.join(x) for x in zip(lines[:lines.index('')][0], lines[:lines.index('')][0][1:])]
# print(pairs)
instructions = {k: (k[0]+v, v+k[1]) for k, v in [line.split(" -> ") for line in lines[lines.index('')+1:]]}
# rules = {a: (a[0]+c,c+a[1]) for a,b,c in rules}
# print(pattern)
print(instructions)
print(rules)


def iterate(counter: Counter, max_depth: int, iteration: int) -> Dict:
    # print(counter)
    _counter = {key: 0 for key in instructions.keys()}
    for key, value in counter.items():
            _counter[instructions[key][0]] += value
            _counter[instructions[key][1]] += value

    # print(_counter)

    if iteration < max_depth-1:
        return iterate(counter=_counter, max_depth=max_depth, iteration=iteration+1)
    return {k: v for k, v in _counter.items() if v > 0}

data_1 = iterate(Counter(pairs), 10, 0)
# print(data_1)
print(f"Part 1: {max(data_1.values()) - min(data_1.values())}")

# data_2 = iterate(Counter(pairs), 40, 0)
# print(f"Part 2: {max(data_2.values()) - min(data_2.values())}")
