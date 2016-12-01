data = {}

with open('input14.txt', 'r') as f:

    for line in f:
        parts = line.split(' ')
        print(parts)
        data[parts[0]] = {}
        data[parts[0]]['total'] = 0
        data[parts[0]]['speed'] = int(parts[3])
        data[parts[0]]['time'] = int(parts[6])
        data[parts[0]]['wait'] = int(parts[13])
        data[parts[0]]['seq'] = []
        data[parts[0]]['score'] = 0
        for x in range(data[parts[0]]['time']):
            data[parts[0]]['seq'].append(data[parts[0]]['speed'])
        for x in range(data[parts[0]]['wait']):
            data[parts[0]]['seq'].append(0)


for t in range(2503):

    for r in data:
        data[r]['total'] += data[r]['seq'][t % len(data[r]['seq'])]

    max = 0
    for r in data:
        max = data[r]['total'] if data[r]['total'] > max else max

    for r in data:
        if data[r]['total'] == max:
            data[r]['score'] += 1

for x in data:
    # print(data[x]['total'])
    print(data[x]['score'])