import hashlib

puzzle_input = 'ffykfhsq'
password = ''

i = 0

while len(password) < 8:
    test_string = puzzle_input + str(i)
    hash_str = hashlib.md5(test_string.encode('UTF-8')).hexdigest()
    if hash_str.startswith('00000'):
        password += hash_str[5]
    i += 1

print('Part 1: {}'.format(password))

password = [' ' for _ in range(8)]
found = 0
i = 0

while found < 8:
    test_string = puzzle_input + str(i)
    hash_str = hashlib.md5(test_string.encode('UTF-8')).hexdigest()
    if hash_str.startswith('00000') and ord(hash_str[5]) >= ord('0') and ord(
        hash_str[5]) <= ord('7'):
        position = int(hash_str[5])
        if password[position] == ' ':
            password[position] = hash_str[6]
            found += 1
    i += 1

print('Part 2: {}'.format(''.join(password)))