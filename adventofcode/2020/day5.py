with open('input5.txt', 'r') as f:
    lines = [line.rstrip() for line in f]


def row_and_column(input):
    s = input.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
    return int(s[0:7], 2), int(s[7:], 2)


def seat_id(r, c):
    return r*8 + c


highest = 0
rows, cols = (128, 8)
seats = [[0 for i in range(cols)] for j in range(rows)]


for line in lines:
    r, c = row_and_column(line)
    _seat_id = seat_id(r, c)
    seats[r-1][c-1] = 1
    if _seat_id > highest:
        highest = _seat_id

for i in range(1, len(seats)-1):
    if 1 in seats[i - 1] and 1 in seats[i + 1] and 0 in seats[i]:
        row = i + 1
        col = seats[i].index(0) + 1
        break

print(f"Part 1: {highest}")
print(f"Part 2: {seat_id(row, col)}")