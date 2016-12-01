"""
Techniques: https://www.kristanix.com/sudokuepic/sudoku-solving-techniques.php
"""
import sys

import math

import itertools

__author__ = 'smaaland'


class SudokuSolver(object):
    puzzles = {
        'easy': [[0, 3, 5, 0, 9, 0, 0, 4, 8],
                 [0, 0, 9, 0, 0, 8, 0, 0, 3],
                 [0, 4, 0, 6, 0, 5, 0, 0, 1],
                 [0, 0, 0, 0, 7, 4, 0, 0, 0],
                 [0, 2, 0, 0, 0, 0, 0, 6, 0],
                 [0, 0, 0, 1, 5, 0, 0, 0, 0],
                 [8, 0, 0, 9, 0, 2, 0, 7, 0],
                 [9, 0, 0, 5, 0, 0, 2, 0, 0],
                 [6, 1, 0, 0, 4, 0, 5, 3, 0],
                 ],
        'app': [[0, 4, 0, 0, 0, 1, 0, 3, 0],
                [3, 6, 0, 0, 0, 2, 8, 0, 0],
                [0, 0, 5, 0, 7, 0, 0, 0, 0],
                [2, 0, 7, 0, 0, 0, 0, 4, 0],
                [0, 0, 0, 0, 0, 7, 0, 0, 3],
                [0, 0, 0, 0, 0, 0, 6, 0, 0],
                [0, 0, 0, 0, 0, 8, 0, 0, 0],
                [4, 0, 0, 0, 1, 0, 0, 0, 5],
                [0, 0, 1, 6, 2, 0, 0, 0, 8],
                ],
        'naked': [[0, 2, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 6, 0, 0, 0, 0, 0, 0],
                  [5, 0, 3, 0, 0, 0, 0, 0, 0],
                  [0, 3, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 0, 2, 0, 6, 0, 0],
                  [0, 0, 0, 6, 0, 0, 0, 0, 0],
                  [8, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [9, 0, 0, 0, 0, 0, 0, 0, 0],
                  ],
        'hidden': [[4, 0, 0, 0, 0, 0, 0, 0, 0],
                   [8, 0, 0, 0, 0, 0, 0, 0, 0],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 1, 5, 6, 7, 0, 0, 0],
                   [0, 8, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 9, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 5, 3, 6, 0, 0, 0],
                   [0, 0, 7, 0, 0, 0, 6, 9, 0],
                   [0, 0, 0, 6, 5, 0, 0, 0, 0],
                   ],
        'hard': [[0, 0, 9, 0, 0, 8, 0, 0, 3],
                 [0, 5, 0, 0, 1, 0, 0, 2, 0],
                 [3, 0, 0, 6, 0, 0, 4, 0, 0],
                 [6, 0, 0, 4, 0, 0, 3, 0, 0],
                 [0, 9, 0, 0, 6, 0, 0, 8, 0],
                 [0, 0, 2, 0, 0, 5, 0, 0, 6],
                 [0, 0, 5, 0, 0, 1, 0, 0, 2],
                 [0, 4, 0, 0, 3, 0, 0, 9, 0],
                 [1, 0, 0, 5, 0, 0, 7, 0, 0],
                 ],
    }

    puzzle = None
    possibilities = None
    done = False

    puzzle_stack = []
    possibilities_stack = []

    # this need a stack as well, since a chance can seem invalid
    # because of an earlier bad chance

    chances_taken = []
    chances_taken_stack = []

    def print_possibilities(self):
        """print the possibilities matrix
        """
        print('')

        for y in range(27):
            s = ''

            if y in [3, 6, 12, 15, 21, 24]:
                print(
                    '- - - - - - - - - - - █ - - - - - - - - - - - █ - - - - '
                    '- - - - - - - ')
            if y in [9, 18]:
                print(
                    '█████████████████████████████████████████████████████████'
                    '█████████████')

            for x in range(9):
                if x in [1, 2, 4, 5, 7, 8]:
                    s += '| '
                if x in [3, 6]:
                    s += '█ '

                number_y = math.floor(y / 3)

                for z in range((y % 3) * 3, (y % 3) * 3 + 3):
                    s += '{} '.format(self.possibilities[number_y][x][z])
            print(s)
        print('')

        print('{} / 81 numbers left to assign'.format(self.get_numbers_left()))
        print('{} / 648 possibilities removed'.format(
            self.get_possibilities_removed()))

        self.print_current_puzzle()

    def get_numbers_left(self):
        left = 0
        for y in range(9):
            for x in range(9):
                if self.puzzle[y][x] == 0:
                    left += 1
        return left

    def get_possibilities_removed(self):
        removed = 0
        for y in range(9):
            for x in range(9):
                for val in range(9):
                    if self.possibilities[y][x][val] == ' ':
                        removed += 1
        return removed

    def print_current_puzzle(self):
        """print the current puzzle state
        """
        print('')
        y = 0
        for row in self.puzzle:
            s = ''
            if y == 3 or y == 6:
                print('------+-------+------')
            x = 0
            for v in row:
                if x == 3 or x == 6:
                    s += '| '
                s += '{} '.format(v if v != 0 else ' ')
                x += 1
            print(s)
            y += 1
        print('')

    def is_solved(self):
        """check if the puzzle is solved
        """
        for y in range(9):
            for x in range(9):
                if self.puzzle[y][x] == 0:
                    return False
        return True

    def clear_possibilities_for_assigned(self):
        """clear possibilities
        """
        print('clear_possibilities_for_assigned')
        modified = False
        for y in range(9):
            for x in range(9):
                if self.puzzle[y][x] != 0:
                    # We have a number on the position
                    for i in range(9):
                        # Clear all possibilities
                        if (i + 1) != (self.puzzle[y][x]) and \
                                self.possibilities[y][x][i] != ' ':
                            # Remove options
                            self.possibilities[y][x][i] = ' '
                            modified = True
        return modified

    def assign_puzzle_cells_with_exactly_one_possibility(self):
        """set the ones with only one possibility
        """
        print('assign_puzzle_cells_with_exactly_one_possibility')
        modified = False
        for y in range(9):
            for x in range(9):
                if self.puzzle[y][x] == 0:
                    p = []
                    for a in range(9):
                        if self.possibilities[y][x][a] != ' ':
                            p.append(self.possibilities[y][x][a])
                    if len(p) == 1 and self.puzzle[y][x] != p[0]:
                        self.puzzle[y][x] = p[0]
                        modified = True
        return modified

    def clear_row_col_and_block_possibilities_for_assigned(self):
        """clears all rows, cols and block possibilities if we have
        something assigned at a position
        """
        print('clear_row_col_and_block_possibilities_for_assigned')
        modified = False

        for y in range(9):
            for x in range(9):
                if self.puzzle[y][x] != 0:
                    # clear row
                    for x_2 in range(9):
                        if x != x_2:
                            if self.possibilities[y][x_2][
                                    self.puzzle[y][x] - 1] != ' ':
                                self.possibilities[y][x_2][
                                    self.puzzle[y][x] - 1] = ' '
                                modified = True
                    # clear col
                    for y_2 in range(9):
                        if y != y_2:
                            if self.possibilities[y_2][x][
                                    self.puzzle[y][x] - 1] != ' ':
                                self.possibilities[y_2][x][
                                    self.puzzle[y][x] - 1] = ' '
                                modified = True

                    # clear block
                    start_y = int(math.floor(y / 3))
                    start_x = int(math.floor(x / 3))
                    for y_2 in range(start_y * 3, start_y * 3 + 3):  # 0,1,2
                        for x_2 in range(start_x * 3,
                                         start_x * 3 + 3):  # 3,4,5
                            if y != y_2 and x != x_2:
                                if self.possibilities[y_2][x_2][
                                        self.puzzle[y][x] - 1] != ' ':
                                    self.possibilities[y_2][x_2][
                                        self.puzzle[y][x] - 1] = ' '
                                    modified = True

        return modified

    def sole_candidates(self):
        """clear due to the sole candidates rule
        """
        print('sole_candidates')
        modified = False

        for y in range(9):
            for x in range(9):
                if self.puzzle[y][x] == 0:
                    # We should check this one, it's not assigned

                    numbers_taken = [' ' for x in range(9)]

                    # check what's taken in row
                    for i in range(9):
                        if self.puzzle[y][i] != 0:
                            numbers_taken[int(self.puzzle[y][i]) - 1] = \
                                self.puzzle[y][i]

                    # check what's taken in col
                    for i in range(9):
                        if self.puzzle[i][x] != 0:
                            numbers_taken[int(self.puzzle[i][x]) - 1] = \
                                self.puzzle[i][x]

                    # check what's taken in box
                    start_y = int(math.floor(y / 3))
                    start_x = int(math.floor(x / 3))
                    for y in range(start_y * 3, start_y * 3 + 3):  # 0,1,2
                        for x in range(start_x * 3, start_x * 3 + 3):  # 3,4,5
                            if self.puzzle[y][x] != 0:
                                numbers_taken[self.puzzle[y][x] - 1] = \
                                    self.puzzle[y][x]

                    # Set the actual number if it's just one left
                    temp = [x for x in numbers_taken if x != ' ']
                    if len(temp) == 8:
                        # We know that there's just one possibility left
                        for i in range(9):
                            if numbers_taken[i] != ' ' and self.puzzle[y][
                                x] == ' ':
                                self.puzzle[y][x] = numbers_taken[i]
                                modified = True
        return modified

    def get_candidates_list_for_val_in_block(self, block_y, block_x, val):
        possibilities_list = []
        for y in range(block_y * 3,
                       block_y * 3 + 3):  # the y positions to check
            for x in range(block_x * 3,
                           block_x * 3 + 3):  # the x positions to check

                impossible = False

                if self.puzzle[y][x] == 0:
                    # This is empty right now

                    # Is it in the current row?
                    for i in range(9):
                        if self.puzzle[y][i] == val:
                            impossible = True

                    # Is it in the current col?
                    for i in range(9):
                        if self.puzzle[i][x] == val:
                            impossible = True
                else:
                    if self.puzzle[y][x] != val:
                        # Something else is already there
                        impossible = True
                    else:
                        # The number is already in the block at this position
                        return [[y, x]]

                if not impossible:
                    possibilities_list.append([y, x])
        return possibilities_list

    def unique_candidates(self):
        """clear due to the unique candidates rule
        """
        print('unique_candidates')
        modified = False

        for start_y in range(3):  # Block counter for Y axis
            for start_x in range(3):  # Block counter for X axis
                for val in range(1, 10):  # The val to check

                    possibilities = self.get_candidates_list_for_val_in_block(
                        start_y, start_x, val)

                    if len(possibilities) == 1:
                        # The current val must be placed here
                        if self.puzzle[possibilities[0][0]][
                            possibilities[0][1]] != val:
                            self.puzzle[possibilities[0][0]][
                                possibilities[0][1]] = val
                            modified = True

        return modified

    def block_column_row_interaction(self):
        """clear due to the Block and column / Row Interaction rule
        """
        print('block_column_row_interaction')
        modified = False

        for block_y in range(3):  # Block counter for Y axis
            for block_x in range(3):  # Block counter for X axis
                for val in range(1, 10):  # The val to check

                    possibilities_list = \
                        self.get_candidates_list_for_val_in_block(
                            block_y, block_x, val)

                    y_vals = []
                    x_vals = []

                    for p in possibilities_list:
                        # Check if all y or x values are the same,
                        # if so remove the possibilities for that col/row from
                        # the other blocks on that same row
                        y_vals.append(p[0])
                        x_vals.append(p[1])

                    y_vals_set = set(y_vals)
                    x_vals_set = set(x_vals)

                    if len(y_vals_set) == 1:
                        # Only one row possible
                        row = next(iter(y_vals_set))

                        # Remove val from this row in it's horizontal block
                        # neighbours
                        for i in range(9):
                            if i not in [j for j in
                                         range(block_x * 3, block_x * 3 + 3)]:
                                if self.possibilities[row][i][val - 1] != ' ':
                                    self.possibilities[row][i][val - 1] = ' '
                                    print("REMOVED a {} for value {}".format(
                                        [row, i], val))
                                    modified = True

                    if len(x_vals_set) == 1:
                        # Only one col possible
                        col = next(iter(x_vals_set))

                        # Remove val from this col in it's vertical block
                        # neighbours
                        for i in range(9):
                            if i not in [j for j in
                                         range(block_y * 3, block_y * 3 + 3)]:
                                if self.possibilities[i][col][val - 1] != ' ':
                                    self.possibilities[i][col][val - 1] = ' '
                                    print("REMOVED b {} for value {}".format(
                                        [i, col], val))
                                    modified = True

        return modified

    def block_block_interaction(self):
        """clear due to the Block / Block Interaction rule
        """
        print('block_block_interaction')
        modified = False

        possibilities_list = [[[[] for _ in range(9)] for _ in range(3)] for _
                              in range(3)]

        # Get all the possibilities
        for block_y in range(3):  # Block counter for Y axis
            for block_x in range(3):  # Block counter for X axis
                for val in range(1, 10):  # The val to check
                    possibilities_list[block_y][block_x][
                        val - 1] = self.get_candidates_list_for_val_in_block(
                        block_y, block_x, val)

        for block_y in range(3):  # Block counter for Y axis
            for block_x in range(3):  # Block counter for X axis
                for val in range(1, 10):  # The val to check
                    other_y_blocks = [a for a in range(3) if a != block_y]
                    # When checking the other y blocks, we want to see if
                    # the x-possibilities set is of size 2
                    x_vals = []
                    for other_y in other_y_blocks:
                        for p in possibilities_list[other_y][block_x][val - 1]:
                            x_vals.append(p[1])

                    x_vals_set = set(x_vals)
                    if len(x_vals_set) == 2:
                        for x_val in list(x_vals_set):
                            # Remove this x possibility from the CURRENT
                            # block for the current val
                            for local_y in range(block_y * 3, block_y * 3 + 3):
                                if self.possibilities[local_y][x_val][
                                        val - 1] != ' ':
                                    self.possibilities[local_y][x_val][
                                        val - 1] = ' '
                                    print("REMOVED c {} for value {}".format(
                                        [local_y, x_val], val))
                                    modified = True

                    other_x_blocks = [a for a in range(3) if a != block_x]
                    # When checking the other x blocks, we want to see if
                    # the y-possibilities set is of size 2
                    y_vals = []
                    for other_x in other_x_blocks:
                        for p in possibilities_list[block_y][other_x][val - 1]:
                            y_vals.append(p[0])

                    y_vals_set = set(y_vals)
                    if len(y_vals_set) == 2:
                        for y_val in list(y_vals_set):
                            # Remove this y possibility from the CURRENT
                            # block for the current val
                            for local_x in range(block_x * 3, block_x * 3 + 3):
                                if self.possibilities[y_val][local_x][
                                        val - 1] != ' ':
                                    self.possibilities[y_val][local_x][
                                        val - 1] = ' '
                                    print("REMOVED d {} for value {}".format(
                                        [y_val, local_x], val))
                                    modified = True

        return modified

    def naked_subset(self):
        """clear due to the Naked Subset rule
        """
        print('naked_subset')
        modified = False

        # COL
        for x in range(9):
            sets = {}
            for y in range(9):
                sets[y] = set(
                    [i for i in self.possibilities[y][x] if i != ' '])

            for y in range(9):
                set_counter = 0
                y_values_for_subsets = []
                for j in range(9):
                    if sets[j] <= sets[y]:
                        set_counter += 1
                        y_values_for_subsets.append(j)

                if set_counter > 1:
                    if set_counter == len(sets[y]):
                        # remove these possibilities from all cells not in list
                        for local_y in range(9):
                            if local_y not in y_values_for_subsets:
                                for val in list(sets[y]):
                                    if self.possibilities[local_y][x][
                                            val - 1] != ' ':
                                        self.possibilities[local_y][x][
                                            val - 1] = ' '
                                        print(
                                            "REMOVED {} for value {}".format(
                                                [local_y, x], val))
                                        modified = True

        # ROW
        for y in range(9):
            sets = {}
            for x in range(9):
                sets[x] = set(
                    [i for i in self.possibilities[y][x] if i != ' '])

            for x in range(9):
                set_counter = 0
                x_values_for_subsets = []
                for j in range(9):
                    if sets[j] <= sets[x]:
                        set_counter += 1
                        x_values_for_subsets.append(j)
                # print(set_counter)
                if set_counter > 1:
                    if set_counter == len(sets[x]):
                        # remove these possibilities from all cells not in list
                        for local_x in range(9):
                            if local_x not in x_values_for_subsets:
                                for val in list(sets[x]):
                                    if self.possibilities[y][local_x][
                                            val - 1] != ' ':
                                        self.possibilities[y][local_x][
                                            val - 1] = ' '
                                        print(
                                            "REMOVED {} for value {}".format(
                                                [y, local_x], val))
                                        modified = True

        # BLOCK
        for block_x in range(3):
            for block_y in range(3):
                sets = {}
                for y in range(block_y * 3, block_y * 3 + 3):
                    sets[y] = {}
                    for x in range(block_x * 3, block_x * 3 + 3):
                        sets[y][x] = set(
                            [i for i in self.possibilities[y][x] if i != ' '])

                for y in range(block_y * 3, block_y * 3 + 3):
                    for x in range(block_x * 3, block_x * 3 + 3):
                        set_counter = 0
                        y_x_values_for_subsets = []
                        for i in range(block_y * 3, block_y * 3 + 3):
                            for j in range(block_x * 3, block_x * 3 + 3):
                                if sets[i][j] <= sets[y][x]:
                                    set_counter += 1
                                    y_x_values_for_subsets.append([i, j])
                        if set_counter > 1 and set_counter == len(sets[y][x]):
                            # remove these possibilities from all cells
                            # not in list
                            for local_y in range(block_y * 3, block_y * 3 + 3):
                                for local_x in range(block_x * 3,
                                                     block_x * 3 + 3):
                                    if [local_y,
                                        local_x] not in y_x_values_for_subsets:
                                        for val in sets[y][x]:
                                            if self.possibilities[local_y][
                                                local_x][val - 1] != ' ':
                                                self.possibilities[local_y][
                                                    local_x][val - 1] = ' '
                                                print(
                                                    "REMOVED BLOCK {} for "
                                                    "value {}".format(
                                                        [local_y, local_x],
                                                        val))
                                                modified = True

        return modified

    def hidden_subset(self):
        """clear due to the Hidden Subset rule
        """
        print('hidden_subset')
        modified = False

        # TODO
        # loop through blocks.

        # COL
        for x in range(9):

            size_of_biggest_subset = 0
            all_numbers_in_subsets = []

            # find the biggest set in row
            for y in range(9):
                p = [i for i in self.possibilities[y][x] if i != ' ']
                if len(p) > 1:
                    size_of_biggest_subset = len(p) if len(
                        p) > size_of_biggest_subset else size_of_biggest_subset
                    all_numbers_in_subsets.extend(p)

            all_numbers_in_subsets = list(set(all_numbers_in_subsets))

            # print('numbers in subsets: {}'.format(all_numbers_in_subsets))
            # print('size of biggest subset: {}'.format(
            # size_of_biggest_subset))

            if size_of_biggest_subset > 1:

                # loop between 2 and the largest possibilities set size
                for size in range(2, size_of_biggest_subset):

                    # print('current size for subset: {}'.format(size))

                    # get all unique numbers in subset. get all combinations of
                    # them for all sizes in the loop below.
                    combos = list(
                        itertools.combinations(all_numbers_in_subsets, size))
                    # print(combos)

                    for combo in combos:
                        y_vals_where_set_member_occurs = []

                        # check if all the values in the combo only occurs in
                        # the same "size" places"

                        for y in range(9):
                            for val in combo:
                                # print(val)
                                if val in self.possibilities[y][x]:
                                    y_vals_where_set_member_occurs.append(y)

                        y_vals_where_set_member_occurs = list(
                            set(y_vals_where_set_member_occurs))
                        if len(y_vals_where_set_member_occurs) == size:
                            # Found hidden subset
                            print('Found hidden subset Y')
                            print(combo)
                            print(y_vals_where_set_member_occurs)

                            for local_y in y_vals_where_set_member_occurs:
                                for i in self.possibilities[local_y][x]:
                                    if i != ' ' and i not in combo:
                                        self.possibilities[local_y][x][
                                            i - 1] = ' '
                                        print(
                                            'removed {} from '
                                            'possibilities[{}][{}]'.format(
                                                i, local_y, x))
                                        modified = True

        # ROW
        for y in range(9):

            size_of_biggest_subset = 0
            all_numbers_in_subsets = []

            # find the biggest set in row
            for x in range(9):
                p = [i for i in self.possibilities[y][x] if i != ' ']
                if len(p) > 1:
                    size_of_biggest_subset = len(p) if len(
                        p) > size_of_biggest_subset else size_of_biggest_subset
                    all_numbers_in_subsets.extend(p)

            all_numbers_in_subsets = list(set(all_numbers_in_subsets))

            # print('numbers in subsets: {}'.format(all_numbers_in_subsets))
            # print('size of biggest subset: {}'.format(
            # size_of_biggest_subset))

            if size_of_biggest_subset > 1:

                # loop between 2 and the largest possibilities set size
                for size in range(2, size_of_biggest_subset):

                    # print('current size for subset: {}'.format(size))

                    # get all unique numbers in subset. get all combinations of
                    # them for all sizes in the loop below.
                    combos = list(
                        itertools.combinations(all_numbers_in_subsets, size))
                    # print(combos)

                    for combo in combos:
                        x_vals_where_set_member_occurs = []

                        # check if all the values in the combo only occurs in
                        # the same "size" places"

                        for x in range(9):
                            for val in combo:
                                # print(val)
                                if val in self.possibilities[y][x]:
                                    x_vals_where_set_member_occurs.append(x)

                        x_vals_where_set_member_occurs = list(
                            set(x_vals_where_set_member_occurs))
                        if len(x_vals_where_set_member_occurs) == size:
                            # Found hidden subset
                            print('Found hidden subset X')
                            print(combo)
                            print(x_vals_where_set_member_occurs)

                            for local_x in x_vals_where_set_member_occurs:
                                for i in self.possibilities[y][local_x]:
                                    if i != ' ' and i not in combo:
                                        self.possibilities[y][local_x][
                                            i - 1] = ' '
                                        print(
                                            'removed {} from '
                                            'possibilities[{}][{}]'.format(
                                                i, y, local_x))
                                        modified = True

        return modified

    def take_a_chance(self):

        # Find a place with the lowest amount of possibilities > 1, and take
        #  a chance if we have not done it before
        combination_to_try = False
        smallest_size_with_untried = 10

        print('chances taken: {}'.format(self.chances_taken))

        for y in range(9):
            for x in range(9):

                temp = [i for i in self.possibilities[y][x] if i != ' ']
                if smallest_size_with_untried > len(temp) > 1:
                    print(temp)
                    for val in temp:
                        if (y, x, val) not in self.chances_taken:
                            combination_to_try = (y, x, val)
                            smallest_size_with_untried = len(temp)

                            break
        if combination_to_try:
            self.puzzle_stack.append(self.puzzle)
            self.possibilities_stack.append(self.possibilities)
            # self.chances_taken_stack.append(self.chances_taken)
            self.chances_taken_stack.append([i for i in self.chances_taken])
            print('..............')
            print(self.chances_taken_stack)
            self.chances_taken.append(combination_to_try)
            print('Combination to try: {}'.format(combination_to_try))
            self.puzzle[combination_to_try[0]][combination_to_try[1]] = \
            combination_to_try[2]
            return True
        return False

    def rollback(self):
        print('ROLLING BACK (stack size: {})'.format(len(self.puzzle_stack)))
        if len(self.puzzle_stack) and len(self.possibilities_stack) and len(
            self.chances_taken_stack):
            self.puzzle = self.puzzle_stack.pop()
            self.possibilities = self.possibilities_stack.pop()
            print(self.chances_taken_stack)
            # TODO we need to keep all the faulty chances as well so we
            # don't make them again, probably also as a stack
            self.chances_taken = self.chances_taken_stack.pop()
            print(self.chances_taken_stack)
            self.print_possibilities()
            return True
        return False

    def is_puzzle_valid(self):
        for y in range(9):
            for x in range(9):
                if len([i for i in self.possibilities[y][x] if i != ' ']) < 1:
                    return False
        return True

    def init(self, puzzle):
        print("Setting puzzle to :{}".format(puzzle))
        self.puzzle = self.puzzles[puzzle]
        self.possibilities = [[[x for x in range(1, 10)] for _ in range(9)] for
                              _ in range(9)]

    def main(self, argv):

        print('starting')
        puzzle = 'easy'

        if len(argv) > 1:
            puzzle = argv[1]

        self.init(puzzle)

        while True:

            did_something_already = False

            if self.is_solved():
                print('SOLVED')
                break

            if not self.is_puzzle_valid():
                if not self.rollback():
                    print('Could not solve... {} empty numbers left'.format(
                        self.get_numbers_left()))

            if not did_something_already and \
                self.clear_possibilities_for_assigned():
                did_something_already = True
                self.print_possibilities()

            if not did_something_already and \
                self.assign_puzzle_cells_with_exactly_one_possibility():
                did_something_already = True
                self.print_possibilities()

            if not did_something_already and \
                self.clear_row_col_and_block_possibilities_for_assigned():
                did_something_already = True
                self.print_possibilities()

            if not did_something_already and self.sole_candidates():
                did_something_already = True
                self.print_possibilities()

            if not did_something_already and self.unique_candidates():
                did_something_already = True
                self.print_possibilities()

            if not did_something_already and \
                self.block_column_row_interaction():
                did_something_already = True
                self.print_possibilities()

            if not did_something_already and self.block_block_interaction():
                did_something_already = True
                self.print_possibilities()

            if not did_something_already and self.naked_subset():
                did_something_already = True
                self.print_possibilities()

            if not did_something_already and self.hidden_subset():
                did_something_already = True
                self.print_possibilities()

            if not did_something_already:
                if self.take_a_chance():
                    did_something_already = True
                else:
                    break

        # self.print_current_puzzle()
        # print(self.puzzle)
        #     self.set_cells_with_one_possibility()
        self.print_possibilities()

        exit()


if __name__ == "__main__":
    SudokuSolver().main(sys.argv)
