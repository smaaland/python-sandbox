def decompress_string(s):
    multiplier = 1
    bracket_level = 0
    new_str = ''

    for c in s:
        if c == '(':
            bracket_level += 1
        elif c == ')':
            bracket_level -= 1
        else:
            if

    return new_str

with open('input9.txt', 'r') as f:
    for line in f:
        s = decompress_string(line.strip())