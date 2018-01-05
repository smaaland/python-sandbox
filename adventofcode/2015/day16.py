data = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}
aunts = {}

with open('input16.txt', 'r') as f:
    for line in f:
        id = line.split(':')[0].split(' ')[1]
        a = line.split(':', 1)[1].split('\n')[0]
        b = a.split(',')
        aunts[int(id)] = {}
        for x in b:
            p = x.split(': ')
            aunts[int(id)][p[0].strip()] = int(p[1])

for id in aunts:
    possible = True
    for key, val in aunts[id].items():
        if val != data[key]:
            possible = False

    if possible:
        print(id)

exclude_list = []
for id in aunts:
    for k in aunts[id]:
        if k.strip() in ['cats', 'trees']:
            if not data[k.strip()] <= aunts[id][k.strip()]:
                exclude_list.append(int(id))
        elif k.strip() in ['pomeranians', 'goldfish']:
            if not data[k.strip()] > aunts[id][k.strip()]:
                exclude_list.append(int(id))
        else:
            if data[k.strip()] != aunts[id][k.strip()]:
                exclude_list.append(int(id))

for i in range(1, 501):
    if i not in exclude_list:
        print(i)
        print(aunts[i])
