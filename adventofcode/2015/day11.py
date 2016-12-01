def char_position(letter):
    return ord(letter) - 97


def pos_to_char(pos):
    return chr(pos + 97)


def increase_string(s):

    l = list(s)

    if char_position(l[-1]) < 25:
        l[-1] = pos_to_char(char_position(l[-1])+1)
        return "".join(l)
    else:
        # Find all the ones that should be flipped, set them to 'a', and increase the one right before them
        in_row = True
        for i in range(len(l)):
            if in_row:
                if char_position(l[len(l)-i-1]) >= 25:
                    # We have a 'z'
                    l[len(l)-i-1] = 'a'
                else:
                    in_row = False
            else:
                # First time only, break
                l[len(l)-i] = pos_to_char(char_position(l[len(l)-i])+1)
                return "".join(l)

        return "".join(l)


def valid(pwd):

    for i in pwd:
        if i in ['i', 'o', 'l']:
            return False

    pwd = list(pwd)
    found_range = False
    for i in range(len(pwd)-2):
        if char_position(pwd[i]) - char_position(pwd[i+1]) == -1 and char_position(pwd[i+1]) - char_position(pwd[i+2]) == -1:
            found_range = True

    if not found_range:
        return False

    pairs = 0
    pair_vals = []
    for i in range(len(pwd)-1):
        if pwd[i] == pwd[i+1]:
            # TODO check that they are different
            pairs += 1
            pair_vals.append(pwd[i])

    if pairs < 2:
        return False

    for i in range(len(pair_vals)-1):
        if pair_vals[i] != pair_vals[i+1]:
            return True

    return False

original_pwd = 'hxbxwxba'

print(original_pwd)

pwd = original_pwd
while True:
    pwd = increase_string(pwd)
    if valid(pwd):
        print(pwd)