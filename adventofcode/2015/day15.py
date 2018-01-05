data = {}
max_result = 0
with open('input15.txt', 'r') as f:
    i = 0
    for line in f:
        parts = line.strip().replace(',', '').split(' ')
        data[i] = {}
        data[i][1] = int(parts[2])
        data[i][2] = int(parts[4])
        data[i][3] = int(parts[6])
        data[i][4] = int(parts[8])
        data[i][5] = int(parts[10])
        i += 1


for a in range(0, 101):
    for b in range(0, 101):
        for c in range(0, 101):
            for d in range(0, 101):
                if a + b + c + d == 100:
                    total = None
                    for prop in range(1, 5):
                        s1 = data[0][prop] * a
                        s2 = data[1][prop] * b
                        s3 = data[2][prop] * c
                        s4 = data[3][prop] * d

                        if total is not None:
                            total *= ((s1 + s2 + s3 + s4) if (s1 + s2 + s3 + s4) > 0 else 0)
                        else:
                            total = ((s1 + s2 + s3 + s4) if (s1 + s2 + s3 + s4) > 0 else 0)
                    max_result = total if total > max_result else max_result

print(max_result)

max_result = 0

for a in range(0, 101):
    for b in range(0, 101):
        for c in range(0, 101):
            for d in range(0, 101):
                if a + b + c + d == 100:
                    total = None
                    for prop in range(1, 5):
                        s1 = data[0][prop] * a
                        s2 = data[1][prop] * b
                        s3 = data[2][prop] * c
                        s4 = data[3][prop] * d

                        c1 = data[0][5] * a
                        c2 = data[1][5] * b
                        c3 = data[2][5] * c
                        c4 = data[3][5] * d

                        cals = c1 + c2 + c3 + c4

                        if cals == 500:
                            if total is not None:
                                total *= ((s1 + s2 + s3 + s4) if (s1 + s2 + s3 + s4) > 0 else 0)
                            else:
                                total = ((s1 + s2 + s3 + s4) if (s1 + s2 + s3 + s4) > 0 else 0)
                        else:
                            total = 0
                    max_result = total if total > max_result else max_result

print(max_result)
