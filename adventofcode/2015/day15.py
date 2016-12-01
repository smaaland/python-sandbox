data = {}
max = 0
with open('input15.txt', 'r') as f:
    i = 0
    for line in f:
        parts = line.split(' ')
        # parts = line.split(',')
        # print(parts)
        data[i] = {}
        # data[parts[0]][0] = parts[2]
        data[i][1] = int(parts[2])
        data[i][2] = int(parts[4])
        data[i][3] = int(parts[6])
        data[i][4] = int(parts[8])
        data[i][5] = int(parts[10].split('\n')[0])
        i += 1


print(data)

for a in range(0,101):
    for b in range(0, 101):
        for c in range(0, 101):
            for d in range(0, 101):
                if a+b+c+d == 100:
                    # print(a,b,c,d)
                    total = None
                    for prop in range(1,5):
                        s1 = data[0][prop]*a
                        s2 = data[1][prop]*b
                        s3 = data[2][prop]*c
                        s4 = data[3][prop]*d

                        c1 = data[0][5]*a
                        c2 = data[1][5]*b
                        c3 = data[2][5]*c
                        c4 = data[3][5]*d
                        cals = c1 + c2 + c3 + c4

                        # Remove this if statement for part 1
                        if cals == 500:
                            if total is not None:
                                total *= ((s1 + s2 + s3 + s4) if (s1 + s2 + s3 + s4) > 0 else 0)
                            else:
                                total = ((s1 + s2 + s3 + s4) if (s1 + s2 + s3 + s4) > 0 else 0)
                        else:
                            total = 0
                    max = total if total > max else max


print(max)