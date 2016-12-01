input = '1321131112'

def it(st):
    last_val = ''
    count = 1
    new = ''
    for c in input:
        if last_val == '':
            # First iteration
            last_val = c
        elif c == last_val:
            count+=1
        else:
            new += str(count)
            new += str(last_val)
            # new += ' '
            count = 1
            last_val = c
    new += str(count)
    new += str(last_val)
    return new

print(input)

print(it(input))

for x in range(50):
    print(x)
    input = it(input)

print(len(input))