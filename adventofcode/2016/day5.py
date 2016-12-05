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

password = [' ' for _ in range(8)]
found = 0

while found < 8:
    test_string = puzzle_input + str(i)
    hash_str = hashlib.md5(test_string.encode('utf-8')).hexdigest()
    if hash_str.startswith('00000') and ord(hash_str[5]) >= ord('0') and ord(
        hash_str[5]) <= ord('7'):
        position = int(hash_str[5])
        if password[position] == ' ':
            password[position] = hash_str[6]
            print(position)
            print(hash_str)
            print(password)
            found += 1

    i += 1

print('Part 2: {}'.format(''.join(password)))


idCode = "ffykfhsq"
idx = 0
counter = 0
#results
part2Pass=['*' for _ in range(8)]
part1Pass=""

while True:
    key = idCode + str(idx)
    md5 = hashlib.md5(key.encode("UTF-8")).hexdigest()
    if md5.startswith("00000"):
        if ord(md5[5]) >= ord('0') and ord(md5[5]) <= ord('7'):
            print(md5[5])
            if part2Pass[int(md5[5])] == '*':
                part2Pass[int(md5[5])] = md5[6]
            if not '*' in part2Pass:
                break

        if counter < 8:
            part1Pass += md5[5]
            counter += 1
    idx += 1
    # results
print("Part1 password: " + part1Pass)
print("Part2 password: " + "".join(part2Pass))