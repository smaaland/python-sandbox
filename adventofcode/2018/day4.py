import json
import re
import datetime

lines = []
with open('input4.txt', 'r') as f:
    for line in f:
        lines.append(line.strip())

    lines.sort()
    # print(json.dumps(lines, indent=4))
    p = re.compile(r'#\d+')
    d = re.compile(r'\[.*?\]')
    to_print = ''
    awake = '.'
    minute = 0
    guards = 0
    on_guard = False
    for line in lines:
        guard = p.findall(line)

        date_time_str = d.findall(line)[0].replace('[', '').replace(']', '')
        date_str, time = date_time_str.split(' ')
        date = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')

        if len(guard):
            if on_guard:
                while minute < 60:
                    to_print += awake
                    minute += 1
                print(to_print)
                minute = 0
            guards += 1
            if minute != 0:
                while minute < 60:
                    to_print += awake
                    minute += 1
                print(to_print)
            current_guard = guard[0]
            awake = '.'

            secure_date = date + datetime.timedelta(hours=1)
            to_print = f'{current_guard.ljust(5)} {secure_date.month:02d}-{secure_date.day:02d}  '
            minute = 0

            on_guard = True
            continue

        on_guard = False

        while minute < date.minute:
            to_print += awake
            minute += 1
        if 'wakes up' in line:
            awake = '.'
            to_print += awake
            minute += 1
        else:
            awake = '#'
            to_print += awake
            minute += 1

    while minute < 60:
        to_print += awake
        minute += 1
    print(to_print)