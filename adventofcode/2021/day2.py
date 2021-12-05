with open('input2.txt', 'r') as f:
    lines = [line.rstrip() for line in f]

values = {
    'height': 0,
    'horizontal': 0
}

for line in lines:
    direction, value = line.split(' ')
    if direction == 'forward':
        values['horizontal'] += int(value)
    if direction == 'up':
        values['height'] -= int(value)
    if direction == 'down':
        values['height'] += int(value)

print(f"Part 1: {values['height'] * values['horizontal']}")

values = {
    'height': 0,
    'horizontal': 0,
    'aim': 0
}

for line in lines:
    direction, value = line.split(' ')
    if direction == 'forward':
        values['horizontal'] += int(value)
        values['height'] += int(value)*values['aim']
    if direction == 'up':
        values['aim'] -= int(value)
    if direction == 'down':
        values['aim'] += int(value)

print(f"Part 2: {values['height'] * values['horizontal']}")