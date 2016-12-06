with open('input6.txt', 'r') as f:

    data = [{chr(key): 0 for key in range(ord('a'), ord('z')+1)} for _ in range(8)]

    for line in f:
        for i in range(8):
            data[i][line[i]] += 1

    message = ''
    for i in range(8):
        biggest_num = 0
        c = ''
        for key in range(ord('a'), ord('z')+1):
            if data[i][chr(key)] > biggest_num:
                biggest_num = data[i][chr(key)]
                c = chr(key)
        message += c
    print('Part 1: {}'.format(message))

    message = ''
    for i in range(8):
        smallest_num = 600
        c = ''
        for key in range(ord('a'), ord('z') + 1):
            if data[i][chr(key)] < smallest_num:
                smallest_num = data[i][chr(key)]
                c = chr(key)
        message += c
    print('Part 2: {}'.format(message))