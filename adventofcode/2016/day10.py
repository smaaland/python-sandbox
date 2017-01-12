bots = {}
output = {}
instructions = []
stop = False


def execute(instruction):

    if instruction[2] == 'goes':
        if not instruction[5] in bots:
            bots[instruction[5]] = []
        bots[instruction[5]].append(instruction[1])
        return True

    if instruction[2] == 'gives':
        # check if it has two, and then do it
        if instruction[1] in bots:  # the giving bot exists
            if len(bots[instruction[1]]) == 2:  # we should execute
                print(bots.get(instruction[11]))
                min_num = min(bots[instruction[1]])
                max_num = max(bots[instruction[1]])
                if instruction[5] == 'bot':
                    if instruction[6] in bots:
                        bots[instruction[6]].append(min_num)
                    else:
                        bots[instruction[6]] = [min_num]
                elif instruction[5] == 'output':
                    if instruction[6] in output:
                        output[instruction[6]].append(min_num)
                    else:
                        output[instruction[6]] = [min_num]

                if instruction[5] == 'bot':
                    if instruction[11] in bots:
                        bots[instruction[11]].append(max_num)
                    else:
                        bots[instruction[11]] = [max_num]
                elif instruction[5] == 'output':
                    if instruction[11] in output:
                        output[instruction[11]].append(max_num)
                    else:
                        output[instruction[11]] = [max_num]

                if min_num == 17 or min_num == 61 or max_num == 17 or max_num == 61:
                    print(min_num, max_num)
                if [min_num, max_num] == [17, 61]:
                    print('Part 1: {}'.format(instruction[1]))
                    stop = True
                # print('Executed: {}'.format(instruction))
                # print(bots)
                return True

    return False


with open('input10.txt', 'r') as f:

    for line in f:
        instructions.append(line.split())

    # print(instructions)

    while not stop:
        # for i in instructions:
        #     execute(i)
        instructions = [i for i in instructions if not execute(i)]
        # print(len(instructions))
        # eval? maybe no

    # print(bots.get(5))