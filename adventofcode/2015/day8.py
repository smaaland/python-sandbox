import re
d2 = 0
cumul_raw = 0
cumul_view = 0

with open('input8.txt', 'r') as f:

    for line in f:
        line=line.rstrip()
        d2+=4

        cumul_raw+=len(line)
        # print(line)

        for i in range(1,len(line)):
            # print(d2)
            if line[i] == "\\" and not (i == len(line)-2):
                if line[i+1] == "\"":
                    d2+=2
                elif line[i+1] == '\\' and (not line[i-1] == '\\'):
                    d2+=2
                elif line[i+1] == "x":
                    if re.findall(r'[a-f0-9]{2}',line[i+2:i+4]):
                        d2+=1
print(d2)
print(cumul_raw)
print(cumul_raw - d2)
print(cumul_raw + d2)


with open("input8.txt") as f:
    strings = f.readlines()

count = 0
for x in strings:
    temp = x.strip()
    count += 2 + temp.count('"') + temp.count('\\')
print(count)