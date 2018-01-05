def recursive_search(key):
    if type(instructions[key]) == int:
        return instructions[key]
    if instructions[key].isdecimal():
        return int(instructions[key])
    else:
        if instructions[key].islower():
            # just another circuit
            instructions[key] = recursive_search(instructions[key])
            return instructions[key]
        elif 'NOT ' in instructions[key]:
            instructions[key] = ~recursive_search(
                instructions[key].split('NOT ')[1]) & 0xffff
            return instructions[key]
        elif ' OR ' in instructions[key]:
            left, right = instructions[key].split(' OR ')
            instructions[key] = (recursive_search(
                left) if not left.isdecimal() else int(left)) | (
                                    recursive_search(
                                        right) if not right.isdecimal() else int(
                                        right))
            return instructions[key]
        elif ' AND ' in instructions[key]:
            left, right = instructions[key].split(' AND ')
            instructions[key] = (recursive_search(
                left) if not left.isdecimal() else int(left)) & (
                                    recursive_search(
                                        right) if not right.isdecimal() else int(
                                        right))
            return instructions[key]
        elif ' LSHIFT ' in instructions[key]:
            left, right = instructions[key].split(' LSHIFT ')
            return recursive_search(left) << int(right)
        elif ' RSHIFT ' in instructions[key]:
            left, right = instructions[key].split(' RSHIFT ')
            return recursive_search(left) >> int(right)


with open('input7.txt', 'r') as f:

    instructions = {}

    for line in f:
        parts = line.strip().split(' -> ')
        instructions[parts[1]] = parts[0]

    first = recursive_search('a')
    print(first)

with open('input7.txt', 'r') as f:
    instructions = {}

    for line in f:
        parts = line.strip().split(' -> ')
        instructions[parts[1]] = parts[0]

    instructions['b'] = first

    second = recursive_search('a')
    print(second)
