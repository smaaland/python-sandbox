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


parents = {}
for line in lines:
    bag, contents = line.strip('.').split(' bags contain ')
    for content in contents.split(', '):
        if content == 'no other bags':
            continue
        _bag = ' '.join(content.split(' ')[1:-1])
        if _bag not in parents:
            parents[_bag] = []
        if bag not in parents[_bag]:
            parents[_bag].append(bag)

print(f"Part 1: {len(list(set(get_all_parents(parents, my_bag, []))))}")
