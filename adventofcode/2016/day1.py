from PIL import Image


def rainbow():
    while True:
        r, g, b = 255, 0, 0
        for g in range(256):
            yield r, g, b
        for r in range(255, -1, -1):
            yield r, g, b
        for b in range(256):
            yield r, g, b
        for g in range(255, -1, -1):
            yield r, g, b
        for r in range(256):
            yield r, g, b
        for b in range(255, -1, -1):
            yield r, g, b


def draw(stays, fname='test.png'):
    minx = 1000
    miny = 1000
    maxx = -1000
    maxy = -1000

    for s in stays:
        minx = min(s[0], minx)
        miny = min(s[1], miny)
        maxx = max(s[0], maxx)
        maxy = max(s[1], maxy)
    x = 2*(maxx - minx + 1)
    y = 2*(maxy - miny + 1)
    r = rainbow()
    img = Image.new('RGB', (x, y))
    pixels = img.load()
    for s in stays:
        pixels[2*s[0] - 2*minx, 2*s[1] - 2*miny] = next(r)
    img.save(fname)


def check_if_val_visited(x_val, y_val, places_visited):
    if (x_val, y_val) in places_visited:
        return True
    return False


def get_first_intersection(steps):
    compass_quarters = 0
    x_val = 0
    y_val = 0

    places_visited = [(x_val, y_val)]
    for x in steps:
        direction = x[:1]
        amount = int(x[1:])

        # Turn
        if direction == 'R':
            compass_quarters = (compass_quarters + 1) % 4
        else:
            compass_quarters = (compass_quarters - 1) % 4

        # Move
        if compass_quarters == 0:
            for _ in range(amount):
                y_val -= 1
                if not check_if_val_visited(x_val, y_val, places_visited):
                    places_visited.append((x_val, y_val))
                else:
                    return (x_val, y_val)
        elif compass_quarters == 1:
            for _ in range(amount):
                x_val += 1
                if not check_if_val_visited(x_val, y_val, places_visited):
                    places_visited.append((x_val, y_val))
                else:
                    return (x_val, y_val)
        elif compass_quarters == 2:
            for _ in range(amount):
                y_val += 1
                if not check_if_val_visited(x_val, y_val, places_visited):
                    places_visited.append((x_val, y_val))
                else:
                    return (x_val, y_val)
        else:
            for _ in range(amount):
                x_val -= 1
                if not check_if_val_visited(x_val, y_val, places_visited):
                    places_visited.append((x_val, y_val))
                else:
                    return (x_val, y_val)


with open('input1.txt', 'r') as f:
    for line in f:
        line = line.replace(" ", "")
        steps = line.split(',')

        compass_quarters = 0
        x_val = 0
        y_val = 0

        for x in steps:
            direction = x[:1]
            amount = int(x[1:])

            # Turn
            if direction == 'R':
                compass_quarters = (compass_quarters + 1) % 4
            else:
                compass_quarters = (compass_quarters - 1) % 4

            # Move
            if compass_quarters == 0:
                y_val += amount
            elif compass_quarters == 1:
                x_val += amount
            elif compass_quarters == 2:
                y_val -= amount
            else:
                x_val -= amount

        print('Part 1: {}'.format(abs(x_val) + abs(y_val)))

        intersection = get_first_intersection(steps)

        print('Part 2: {}'.format(abs(intersection[0]) + abs(intersection[1])))
