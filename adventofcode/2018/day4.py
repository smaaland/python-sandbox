import re
import datetime

lines = []
with open('input4.txt', 'r') as f:
    for line in f:
        lines.append(line.strip())

    lines.sort()

    p = re.compile(r'#\d+')
    d = re.compile(r'\[.*?\]')
    to_print = ''
    awake = '.'
    minute = 0
    guards = 0
    on_guard = False

    current_guard = ''
    data = {}
    current_object = {}
    current_line = ''
    current_date = ''

    for line in lines:
        guard = p.findall(line)

        date_time_str = d.findall(line)[0].replace('[', '').replace(']', '')
        date_str, time = date_time_str.split(' ')
        date = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')

        if len(guard):
            if on_guard:
                while minute < 60:
                    to_print += awake
                    current_line += awake
                    minute += 1
                print(to_print)
                data[current_guard]['metrics'][current_date] = current_line
                data[current_guard]['sleep_minutes'] += current_line.count('#')
                minute = 0
            guards += 1
            if minute != 0:
                while minute < 60:
                    to_print += awake
                    current_line += awake
                    minute += 1
                print(to_print)
                data[current_guard]['metrics'][current_date] = current_line
                data[current_guard]['sleep_minutes'] += current_line.count('#')
            current_guard = guard[0]
            if current_guard not in data.keys():
                data[current_guard] = {
                    'metrics': {},
                    'sleep_minutes': 0
                }
            awake = '.'

            secure_date = date + datetime.timedelta(hours=1)
            to_print = f'{current_guard.ljust(5)} {secure_date.month:02d}-{secure_date.day:02d}  '
            current_line = ''
            current_date = f'{secure_date.month:02d}-{secure_date.day:02d}'
            minute = 0

            on_guard = True
            continue

        on_guard = False

        while minute < date.minute:
            to_print += awake
            current_line += awake
            minute += 1
        if 'wakes up' in line:
            awake = '.'
            to_print += awake
            current_line += awake
            minute += 1
        else:
            awake = '#'
            to_print += awake
            current_line += awake
            minute += 1

    while minute < 60:
        to_print += awake
        current_line += awake
        minute += 1
    print(to_print)
    data[current_guard]['metrics'][current_date] = current_line
    data[current_guard]['sleep_minutes'] += current_line.count('#')

    max_sleep = 0
    sleepiest_guard = ''
    for guard in data:
        if data[guard]['sleep_minutes'] > max_sleep:
            max_sleep = data[guard]['sleep_minutes']
            sleepiest_guard = guard

    max_minutes = 0
    sleepiest_minute = 0
    for m in range(0, 60):
        current_minutes = 0
        for series in data[sleepiest_guard]['metrics']:
            if data[sleepiest_guard]['metrics'][series][m] == '#':
                current_minutes += 1
        if current_minutes > max_minutes:
            max_minutes = current_minutes
            sleepiest_minute = m

    print(f'Part 1: {sleepiest_minute*int(sleepiest_guard.strip("#"))}')

    max_minutes = 0
    sleepiest_minute = 0
    sleepiest_guard = ''
    for guard in data:
        for m in range(0, 60):
            current_minutes = 0
            for series in data[guard]['metrics']:
                if data[guard]['metrics'][series][m] == '#':
                    current_minutes += 1
            if current_minutes > max_minutes:
                max_minutes = current_minutes
                sleepiest_minute = m
                sleepiest_guard = guard

    print(f'Part 2: {sleepiest_minute*int(sleepiest_guard.strip("#"))}')
