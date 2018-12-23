import string


def react(s):
    removed_something = True
    start = 0
    while removed_something:
        removed_something = False
        index = start
        for i, j in zip(s[start::1], s[start + 1::1]):
            if i.lower() == j.lower() and ((i.isupper() and j.islower()) or (i.islower() and j.isupper())):
                removed_something = True
                s = s[0:index] + s[index + 2:]
                start = index - 1
                if start < 0:
                    start = 0
                break
            index += 1
            removed_something = False
    return s


data = ''
with open('input5.txt', 'r') as f:
    for line in f:
        data += line.strip()

    print(f'Part 1: {len(react(data))}')

    lengths = []
    for char in string.ascii_lowercase:
        s = data.replace(char, '').replace(char.upper(), '')
        c = react(s)
        lengths.append(len(c))
    print(f'Part 2: {min(lengths)}')
