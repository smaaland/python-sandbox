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

    print('Part 1: {}'.format(total))
