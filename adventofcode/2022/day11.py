import copy
import math

lines = [line.strip() for line in open("input11.txt", "r").readlines()]
rows = [lines[i:i + 7] for i in range(0, len(lines), 7)]
monkeys = []

class Monkey:
    items = []
    divisible_by = -1
    true_throw_to = -1
    false_throw_to = -1
    operation = ''
    rhs = ''
    inspections = 0

for r in rows:
    m = Monkey()
    m.items = [int(x) for x in r[1].replace("Starting items: ", "").split(", ")]
    m.divisible_by = int(r[3].split("divisible by ")[1])
    m.true_throw_to = int(r[4].split("throw to monkey ")[1])
    m.false_throw_to = int(r[5].split("throw to monkey ")[1])
    m.operation, m.rhs = r[2].split("new = old ")[1].split()
    monkeys.append(m)

lcm = math.lcm(*[m.divisible_by for m in monkeys])
monkeys_2 = copy.deepcopy(monkeys)

def keep_away(_monkeys, iterations = 20, worry=True):
    for i in range(iterations):
        for m in _monkeys:
            for j in range(len(m.items)):
                if m.rhs == "old":
                    val = m.items[j]
                else:
                    val = int(m.rhs)
                if m.operation == "+":
                    m.items[j] = m.items[j] + val
                elif m.operation == "*":
                    m.items[j] = m.items[j] * val
                m.inspections += 1
                if worry:
                    m.items[j] = m.items[j] // 3
                else:
                    m.items[j] = m.items[j] % lcm
                if m.items[j] % m.divisible_by == 0:
                    _monkeys[m.true_throw_to].items.append(m.items[j])
                else:
                    _monkeys[m.false_throw_to].items.append(m.items[j])
            m.items = []
    monkey_business = math.prod(sorted([m.inspections for m in _monkeys])[-2:])
    return monkey_business

print(f"Part 1: {keep_away(monkeys)}")
print(f"Part 2: {keep_away(monkeys_2, iterations=10000, worry=False)}")
