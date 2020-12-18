with open('input7.txt', 'r') as f:
    lines = [line.rstrip() for line in f]

my_bag = 'shiny gold'


def get_all_parents(_parents, child, so_far):
    if child not in _parents:
        return so_far
    else:
        [get_all_parents(_parents, _p, so_far) for _p in _parents[child] if _p not in so_far]
        so_far.extend(_parents[child])
    return so_far


def get_all_children(_children, child):
    if child in _children:
        return sum([c['amount'] + c['amount'] * get_all_children(_children, c['type']) for c in _children[child]])
    else:
        return 0


parents = {}
children = {}

for line in lines:
    bag, contents = line.strip('.').split(' bags contain ')
    for content in contents.split(', '):
        if content == 'no other bags':
            continue
        parts = content.split(' ')
        _bag = ' '.join(parts[1:-1])
        amount = int(parts[0])
        if _bag not in parents:
            parents[_bag] = []
        if bag not in parents[_bag]:
            parents[_bag].append(bag)
        if bag not in children:
            children[bag] = []
        if _bag not in children[bag]:
            children[bag].append({'type': _bag, 'amount': amount})

print(f"Part 1: {len(list(set(get_all_parents(parents, my_bag, []))))}")
print(f"Part 2: {get_all_children(children, my_bag)}")