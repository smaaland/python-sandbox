import copy
from typing import List

with open('input4.txt', 'r') as f:
    lines = [line.rstrip() for line in f]

numbers = lines[0].split(',')
board_data = lines[1:]

boards = []

for _, l1, l2, l3, l4, l5 in zip(*[iter(board_data)]*6):
    boards.append([l1.split(), l2.split(), l3.split(), l4.split(), l5.split()])

first_win = None
last_win = None
bingo_boards = []
number_of_boards = len(boards)


class BingoException(Exception):
    pass


def has_bingo(board: List[List[str]]) -> bool:
    for row in board:
        if all([x == "X" for x in row]):
            return True
    for col in range(len(board[0])):
        if all([x == "X" for x in [r[col] for r in board]]):
            return True
    return False


last_number_first_win = None
last_number_last_win = None

try:
    for n in numbers:
        for i, b in enumerate(boards):
            for row in b:
                matches = [i for i, x in enumerate(row) if x == n]
                for m in matches:
                    row[m] = "X"
                    if has_bingo(b):
                        if first_win is None:
                            first_win = copy.deepcopy(b)
                            last_number_first_win = int(n)
                        last_win = copy.deepcopy(b)
                        last_number_last_win = int(n)
                        if i not in bingo_boards:
                            bingo_boards.append(i)
                        if len(bingo_boards) == len(boards):
                            raise BingoException
except BingoException:
    pass

unmarked_sum_first_win = sum([sum([int(x) for x in row if x != "X"]) for row in first_win])
unmarked_sum_last_win = sum([sum([int(x) for x in row if x != "X"]) for row in last_win])

print(f"Part 1: {unmarked_sum_first_win*last_number_first_win}")
print(f"Part 2: {unmarked_sum_last_win*last_number_last_win}")
