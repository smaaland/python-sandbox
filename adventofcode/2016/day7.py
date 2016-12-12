with open('input7.txt', 'r') as f:
    found = 0

    for line in f:

        bracket_level = 0
        chars_parsed = 0

        for c in line:
            if c == '[':
                bracket_level += 1
            elif c == ']':
                bracket_level -= 1
            else:
                if bracket_level < 1:
                    if chars_parsed > 3:
                        if line[chars_parsed] == line[chars_parsed - 3] and \
                                line[chars_parsed - 1] == line[
                                    chars_parsed - 2] and line[
                                chars_parsed - 1] != line[chars_parsed]:
                            found += 1

            chars_parsed += 1

    print('Part 1: {}'.format(found))


def has_matching_set(outside, inside):
    for s1 in outside:
        for s2 in inside:
            if s1[0] == s2[1] and s2[0] == s1[1]:
                return True
    return False

with open('input7.txt', 'r') as f:
    found = 0

    for line in f:
        bracket_level = 0
        chars_in_sequence = 0
        chars_parsed = 0
        outside = []
        inside = []

        for c in line:
            if c == '[':
                bracket_level += 1
                chars_in_sequence = 0
            elif c == ']':
                bracket_level -= 1
                chars_in_sequence = 0
            else:
                chars_in_sequence += 1
                if chars_in_sequence > 2:
                    if line[chars_parsed] == line[chars_parsed - 2] and line[
                        chars_parsed] != line[chars_parsed - 1]:
                        if bracket_level < 1:
                            # outside
                            outside.append(line[chars_parsed-2:chars_parsed+1])
                        else:
                            # inside
                            inside.append(line[chars_parsed - 2:chars_parsed+1])

            chars_parsed += 1

        if has_matching_set(outside, inside):
            found += 1

    print('Part 2: {}'.format(found))

