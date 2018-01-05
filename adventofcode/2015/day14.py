data = {}

with open('input14.txt', 'r') as f:

    for line in f:
        parts = line.split(' ')
        data[parts[0]] = {}
        data[parts[0]]['total_distance'] = 0
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
        data[r]['total_distance'] += data[r]['seq'][t % len(data[r]['seq'])]

    max_distance = 0
    for r in data:
        max_distance = data[r]['total_distance'] if data[r]['total_distance'] > max_distance else max_distance

    for r in data:
        if data[r]['total_distance'] == max_distance:
            data[r]['score'] += 1


print(max([data[x]['total_distance'] for x in data.keys()]))
print(max([data[x]['score'] for x in data.keys()]))
