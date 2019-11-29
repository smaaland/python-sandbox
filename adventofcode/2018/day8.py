def rec_row(row):
    c, m = row[:2]
    data = row[2:]
    scores = []
    totals = 0

    for i in range(c):
        total, score, data = rec_row(data)
        totals += total
        scores.append(score)

    totals += sum(data[:m])

    if c == 0:
        return totals, sum(data[:m]), data[m:]
    else:
        return totals, sum(scores[k - 1] for k in data[:m] if 0 < k <= len(scores)), data[m:]


with open('input8.txt', 'r') as f:
    for line in f:
        row = [int(x) for x in line.strip().split()]
        total, value, _ = rec_row(row)
        print(f'Part 1: {total}')
        print(f'Part 2: {value}')
