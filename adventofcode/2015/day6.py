with open('input6.txt', 'r') as f:

    matrix = [[False for _ in range(1000)] for _ in range(1000)]

    total = 0
    for line in f:
        if "turn on" in line:
            p1, p2 = line.strip('turn on').strip().split(' through ')
            p1 = p1.split(',')
            p2 = p2.split(',')
            for x in range(int(p1[0]), int(p2[0])+1):
                for y in range(int(p1[1]), int(p2[1])+1):
                    matrix[x][y] = True
        elif "turn off" in line:
            p1, p2 = line.strip('turn off').strip().split(' through ')
            p1 = p1.split(',')
            p2 = p2.split(',')
            for x in range(int(p1[0]), int(p2[0]) + 1):
                for y in range(int(p1[1]), int(p2[1]) + 1):
                    matrix[x][y] = False
        else:
            p1, p2 = line.strip('toggle').strip().split(' through ')
            p1 = p1.split(',')
            p2 = p2.split(',')
            for x in range(int(p1[0]), int(p2[0]) + 1):
                for y in range(int(p1[1]), int(p2[1]) + 1):
                    matrix[x][y] = not matrix[x][y]

    total = 0
    for x in range(1000):
        for y in range(1000):
            if matrix[x][y]:
                total += 1

    print(total)

with open('input6.txt', 'r') as f:

    matrix = [[0 for _ in range(1000)] for _ in range(1000)]

    total = 0
    for line in f:
        if "turn on" in line:
            p1, p2 = line.strip('turn on').strip().split(' through ')
            p1 = p1.split(',')
            p2 = p2.split(',')
            for x in range(int(p1[0]), int(p2[0])+1):
                for y in range(int(p1[1]), int(p2[1])+1):
                    matrix[x][y] += 1
        elif "turn off" in line:
            p1, p2 = line.strip('turn off').strip().split(' through ')
            p1 = p1.split(',')
            p2 = p2.split(',')
            for x in range(int(p1[0]), int(p2[0]) + 1):
                for y in range(int(p1[1]), int(p2[1]) + 1):
                    matrix[x][y] = matrix[x][y] - 1 if matrix[x][y] - 1 >= 0 else 0
        else:
            p1, p2 = line.strip('toggle').strip().split(' through ')
            p1 = p1.split(',')
            p2 = p2.split(',')
            for x in range(int(p1[0]), int(p2[0]) + 1):
                for y in range(int(p1[1]), int(p2[1]) + 1):
                    matrix[x][y] = matrix[x][y] + 2

    total = 0
    for x in range(1000):
        for y in range(1000):
            total += matrix[x][y]

    print(total)
