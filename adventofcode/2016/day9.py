import re
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
        else:
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


# def part_2_loop(l):
#
#     total_length = 0
#     string_to_prepend = []
#     inside_str = ''
#     skipping = 0
#     bracket_level = 0
#     iterations = 0
#
#     # s = ''
#
#     while True:
#         # print(''.join(l))
#
#         if not iterations % 1000:
#             print(len(l))
#         iterations += 1
#
#         if len(string_to_prepend) and skipping == 0:
#             l = string_to_prepend + l
#             # print('# ' + ''.join(string_to_prepend))
#             # print(''.join(l))
#             string_to_prepend = []
#
#         if len(l):
#             # print(len(l))
#             c = l.pop(0)
#
#             if skipping > 0:
#                 skipping -= 1
#             else:
#
#                 if c == '(':
#                     bracket_level += 1
#                 elif c == ')':
#                     bracket_level -= 1
#
#                     characters_to_repeat, multiplier = [int(i) for i in
#                                                         inside_str.split('x')]
#                     inside_str = ''
#
#                     app = l[:characters_to_repeat]
#
#                     for _ in range(multiplier):
#                         string_to_prepend += app
#
#                     skipping = characters_to_repeat
#                 else:
#                     if bracket_level < 1:
#                         # removing regular character
#                         # print(c)
#                         # s += c
#                         total_length += 1
#                     else:
#                         # inside the parenthesis
#                         inside_str += c
#                         pass
#         else:
#             return total_length
#
#     # print(s)
#     return total_length

def get_len_of_string(s):
    regexp = re.compile(r'\(\w+x\w+\)')
    total = 0
    iterations = 0
    while len(s):

        if not iterations % 10000:
            print(len(s))
        iterations += 1

        match = regexp.search(s)
        if match is None:
            total += len(s)
            s = ''
        else:
            # print(match.start(), match.end())
            # print(s)
            characters_to_repeat, multiplier = [int(i) for i in s[
                                                                match.start() + 1:match.end() - 1].split(
                'x')]
            total += match.start()

            # print(s[match.end():match.end()+characters_to_repeat])
            # print('"')
            # print(s[match.end()+characters_to_repeat:])
            s = s[
                match.end():match.end() + characters_to_repeat] * multiplier \
                + s[
                  match.end() + characters_to_repeat:]
            # print(s)
    return total


def get_len_of_string_no_regex(s):
    total = 0
    iterations = 0
    while len(s):

        if not iterations % 10000:
            print(len(s))
        iterations += 1

        if '(' not in s:
            total += len(s)
            s = ''
        else:

            start = s.find('(')
            end = s[start:].find(')') + start
            marker = s[start+1:end].split('x')
            total += s.find('(')

            s = s[end+1:end +1+ int(marker[0])] * int(marker[1]) + s[
                                                                 end +
                                                                 int(marker[1]):]
    return total


def decompress(s, part2=True):
    if '(' not in s:
        return len(s)
    ret = 0
    while '(' in s:
        ret += s.find('(')
        s = s[s.find('('):]
        marker = s[1:s.find(')')].split('x')
        s = s[s.find(')') + 1:]
        if part2:
            ret += decompress(s[:int(marker[0])]) * int(marker[1])
        else:
            ret += len(s[:int(marker[0])]) * int(marker[1])
        s = s[int(marker[0]):]
    ret += len(s)
    return ret

with open('input9.txt', 'r') as f:
    for line in f:
        #print(line)
        # s = 'ABCDEF'
        # print(s)
        # s = part_2_loop(list(s))
        # print(s)
        #
        # s = '(3x3)XYZ'
        # print(s)
        # s = part_2_loop(list(s))
        # print(s)
        #
        # s = 'A(2x2)BCD(2x2)EFG'
        # print(s)
        # s = part_2_loop(list(s))
        # print(s)

        # s = '(27x12)(20x12)(13x14)(7x10)(1x12)A'
        # print(s)
        # s = get_len_of_string(s)
        # print(s)

        # s = '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'
        # print(s)
        # s = part_2_loop(list(s))
        # print(s)

        # s = decompress_string_iteration(line.strip())
        # print('Part 1: {}'.format(len(s)))

        s = line.strip()
        # print(s)
        # print(list(s))
        # num = part_2_recursive(list(s))
        # num = part_2_loop(list(s))
        num = get_len_of_string_no_regex(s)
        print('Part 2: {}'.format(num))
