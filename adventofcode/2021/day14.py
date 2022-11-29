import string
from collections import Counter

lines = [line.strip() for line in open('input14.txt', 'r').readlines()]
template = lines[0]
rules = [rule.split(' ') for rule in lines[2:]]
rules = {a: (a[0] + c, c + a[1]) for a, _, c in rules}
pairs = [''.join(p) for p in zip(template, template[1:])]


def run(steps):
    ctr = Counter(pairs)
    for i in range(steps):
        new_ctr = {key: 0 for key in rules.keys()}
        for key, value in ctr.items():
            new_ctr[rules[key][0]] += value
            new_ctr[rules[key][1]] += value
        ctr = new_ctr

    letter_totals = {letter: 0 for letter in list(string.ascii_uppercase)}
    for key, value in ctr.items():
        letter_totals[key[0]] += value

    letter_totals[template[-1]] += 1

    lmax = max(letter_totals.values())
    lmin = min([value for value in letter_totals.values() if value > 0])
    return lmax - lmin


print(f"Part 1: {run(10)}")
print(f"Part 2: {run(40)}")
