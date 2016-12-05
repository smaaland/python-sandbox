with open('input4.txt', 'r') as f:
    total = 0
    for line in f:
        parts = line.strip().split('-')
        temp = parts.pop().split('[')
        number = int(temp[0])
        checksum = temp[1].split(']')[0]
        encrypted_name = ''.join(parts)

        occurrences = {}
        for c in encrypted_name:
            if c in occurrences:
                occurrences[c] += 1
            else:
                occurrences[c] = 1

        word = ''.join([x[0] for x in sorted(occurrences.items(),
                                             key=lambda t: (-t[1], t[0]))][:5])
        if word == checksum:
            total += number
            word = line.strip().rsplit('-', 1)[0]
            sector_id = int(line.strip().rsplit('-', 1)[1].split('[')[0])
            decrypted = ''
            char_range = ord('z') - ord('a') + 1
            positions_to_shift = sector_id % char_range

            for c in word:
                if c == '-':
                    decrypted += ' '
                elif ord('a') <= ord(c) <= ord('z'):
                    if not ord(c) + positions_to_shift > ord('z'):
                        decrypted += chr(ord(c) + positions_to_shift)
                    else:
                        decrypted += chr(
                            ord(c) + positions_to_shift - char_range)

            if decrypted == 'northpole object storage':
                north_pole_sector = sector_id

    print('Part 1: {}'.format(total))
    print('Part 2: {}'.format(north_pole_sector))
