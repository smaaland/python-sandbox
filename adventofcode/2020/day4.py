import itertools
import re

with open('input4.txt', 'r') as f:
    lines = [line.rstrip() for line in f]

key = lambda sep: sep == ''
_passports = [" ".join(list(group)).split(" ") for is_key, group in itertools.groupby(lines, key) if not is_key]

passports = []
for passport in _passports:
    passports.append({k: v for (k, v) in [line.split(":") for line in passport]})

required_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
height_regex_1 = re.compile('(\d*)cm')
height_regex_2 = re.compile('(\d*)in')
color_regex = re.compile(r'^#(?:[0-9a-fA-F]{3}){1,2}$')

total_valid_part_1 = 0
total_valid_part_2 = 0

for passport in passports:
    if all(k in passport for k in required_keys):
        total_valid_part_1 += 1

        valid = True
        for k, v in passport.items():
            if k == "byr":
                if not (v.isnumeric() and int(v) >= 1920 and int(v) <= 2002):
                    valid = False
            if k == "iyr":
                if not (v.isnumeric() and int(v) >= 2010 and int(v) <= 2020):
                    valid = False
            if k == "eyr":
                if not (v.isnumeric() and int(v) >= 2020 and int(v) <= 2030):
                    valid = False
            if k == "hgt":
                h1 = height_regex_1.match(v)
                h2 = height_regex_2.match(v)
                if not (h1 or h2):
                    valid = False
                else:
                    if h1:
                        if not 150 <= int(h1.groups()[0]) <= 193:
                            valid = False
                    elif h2:
                        if not 59 <= int(h2.groups()[0]) <= 76:
                            valid = False
            if k == "hcl":
                if not color_regex.match(v):
                    valid = False
            if k == "ecl":
                if not v in ["amb", "blu", "brn", "gry", "grn", "hzl",  "oth"]:
                    valid = False
            if k == "pid":
                if not(v.isnumeric() and len(v) == 9):
                    valid = False
        if valid:
            total_valid_part_2 += 1

print(f"Part 1: {total_valid_part_1}")
print(f"Part 2: {total_valid_part_2}")