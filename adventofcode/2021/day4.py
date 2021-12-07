with open('input4.txt', 'r') as f:
    lines = [line.rstrip() for line in f]

numbers = lines[0].split(',')
board_data = lines[1:]

boards = []

for _, l1, l2, l3, l4, l5 in zip(*[iter(board_data)]*6):
    boards.append([l1.split(), l2.split(), l3.split(), l4.split(), l5.split()])


print(numbers)
print(boards)