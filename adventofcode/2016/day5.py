import hashlib

puzzle_input = 'ffykfhsq'
password = ''

i = 0

while len(password) < 8:
    test_string = puzzle_input + str(i)
    hash_str = hashlib.md5(test_string.encode('utf-8')).hexdigest()
    if hash_str.startswith('00000'):
        password += hash_str[5]
    i += 1

print('Part 1: {}'.format(password))
