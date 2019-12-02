with open('input2.txt', 'r') as f:
    data = ''
    for line in f:
        data += line.strip()
    data = [int(i) for i in data.split(',')]

    index = 0
    data[1] = 12
    data[2] = 2

    while data[index] != 99:
        if data[index] == 1:
            data[data[index+3]] = data[data[index+1]] + data[data[index+2]]
        elif data[index] == 2:
            data[data[index+3]] = data[data[index+1]] * data[data[index+2]]
        index += 4

print(f'Part 1: {data[0]}')
