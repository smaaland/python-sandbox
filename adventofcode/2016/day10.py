bots = {}
outputs = {}
instructions = []
stop = False


def execute(instruction):
    global stop, outputs
    if instruction[2] == 'goes':
        if not int(instruction[5]) in bots.keys():
            bots[int(instruction[5])] = []
        bots[int(instruction[5])].append(int(instruction[1]))
        # print('EXECUTED {}'.format(instruction))
        # print(bots)
        # print([len(bots[i]) for i in bots])
        return True

    if instruction[2] == 'gives':
        # check if it has two, and then do it
        if int(instruction[1]) in bots.keys():  # the giving bot exists
            if len(bots[int(instruction[1])]) == 2:  # we should execute
                # print(instruction)

                min_num = int(min(bots[int(instruction[1])]))
                max_num = int(max(bots[int(instruction[1])]))

                if instruction[5] == 'bot':
                    if int(instruction[6]) in bots.keys():
                        bots[int(instruction[6])].append(min_num)
                    else:
                        bots[int(instruction[6])] = [min_num]
                elif instruction[5] == 'output':
                    outputs[int(instruction[6])] = min_num

                if instruction[10] == 'bot':
                    if int(instruction[11]) in bots.keys():
                        bots[int(instruction[11])].append(max_num)
                    else:
                        bots[int(instruction[11])] = [max_num]
                elif instruction[10] == 'output':
                    outputs[int(instruction[11])] = max_num

                bots[int(instruction[1])] = []

                if [min_num, max_num] == [17, 61]:
                    print('Part 1: {}'.format(instruction[1]))
                # print('EXECUTED {}'.format(instruction))
                return True

    return False


with open('input10.txt', 'r') as f:
    for line in f:
        instructions.append(line.split())

    while len(instructions):
        instructions = [i for i in instructions if not execute(i)]

    print('Part 2: {}'.format(outputs[0]*outputs[1]*outputs[2]))
