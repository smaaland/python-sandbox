with open('input5.txt', 'r') as f:
    lines = [line.rstrip() for line in f]

data = [_.split(" -> ") for _ in lines]
max_x = 0
max_y = 0

lines = []
for d in data:
    lines.append({
        "x1": int(d[0].split(",")[0]),
        "y1": int(d[0].split(",")[1]),
        "x2": int(d[1].split(",")[0]),
        "y2": int(d[1].split(",")[1]),
    })
    print(lines)
    print(type(max_x))
    print(type(lines["x1"]))
    if lines["x1"] > max_x:
        max_x = lines["x1"]
    if lines["x2"] > max_x:
        max_x = lines["x2"]
    if lines["y1"] > max_y:
        max_y = lines["y1"]
    if lines["y2"] > max_y:
        max_y = lines["y2"]

print(max_x, max_y)

for l in lines:
    matrix = [max_x * [max_x * 0]]

lines_to_use = []
for l in lines:
    if l["x1"] == l["x2"]:
        lines_to_use.append(l)
    if l["y1"] == l["y2"]:
        lines_to_use.append(l)

for l in lines_to_use:
    if not l["x1"] == l["x2"]:
        for x in range(l["x1"], l["x2"]+1):
            print(type(l["y1"]))
            print(l["y1"])
            print(type(x))
            print(x)
            matrix[l["y1"][x]] = "X"
    if not l["y2"] == l["y2"]:
        for y in range(l["y1"], l["y2"]+1):
            print(y)
