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

