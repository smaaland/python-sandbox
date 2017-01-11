import sys
sys.setrecursionlimit(100000)


def decompress_string_iteration(s):
    bracket_level = 0
    new_str = ''
    l = list(s)
    inside_str = ''
    skipping = 0

    for c in s:
        if skipping > 0:
            skipping -= 1
        else:
            if c == '(':
                bracket_level += 1
                l.pop(0)
            elif c == ')':
                bracket_level -= 1
                l.pop(0)
                characters_to_repeat, multiplier = [int(i) for i in
                                                    inside_str.split('x')]
                inside_str = ''
                app = ''
                for _ in range(characters_to_repeat):
                    app += l.pop(0)

                for _ in range(multiplier):
                    new_str += app
                skipping = characters_to_repeat

            else:
                if bracket_level < 1:
                    new_str += l.pop(0)
                    pass
                else:
                    # inside the parenthesis
                    l.pop(0)
                    inside_str += c
                    pass

    return new_str


def part_2_recursive(l, total_length=0, string_to_prepend=[], inside_str='', skipping=0, bracket_level=0):

    if len(string_to_prepend) and skipping == 0:
        l = string_to_prepend + l
        string_to_prepend = []

    if len(l):
        print(len(l))
        c = l.pop(0)

        if skipping > 0:
            skipping -= 1

        if c == '(':
            bracket_level += 1

        elif c == ')':
            bracket_level -= 1

            characters_to_repeat, multiplier = [int(i) for i in
                                                inside_str.split('x')]
            inside_str = ''

            app = l[:characters_to_repeat]

            for _ in range(multiplier):
                string_to_prepend += app

            skipping = characters_to_repeat
        else:
            if bracket_level < 1:
                # removing regular character
                total_length += 1
            else:
                # inside the parenthesis
                inside_str += c
                pass
        return part_2_recursive(l, total_length, string_to_prepend, inside_str, skipping, bracket_level)
    else:
        return total_length


with open('input9.txt', 'r') as f:
    for line in f:
        #print(line)
        # s = 'ABCDEF'
        # print(s)
        # s = get_len_of_string(s)
        # print(s)
        #
        # s = '(3x3)XYZ'
        # print(s)
        # s = get_len_of_string(s)
        # print(s)
        #
        # s = 'A(2x2)BCD(2x2)EFG'
        # print(s)
        # s = get_len_of_string(s)
        # print(s)
        # s = '(6x1)(1x3)A'
        # print(s)
        # s = get_len_of_string(s)
        # print(s)
        # s = 'X(8x2)(3x3)ABCY'
        # print(s)
        # s = get_len_of_string(s)
        # print(s)

        s = decompress_string_iteration(line.strip())
        print('Part 1: {}'.format(len(s)))

        s = line.strip()
        # print(s)
        # print(list(s))
        num = part_2_recursive(list(s))
        print('Part 2: {}'.format(num))
