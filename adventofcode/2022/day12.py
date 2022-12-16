lines = [[ord(c)-83 for c in list(line.strip())] for line in open("input12.txt", "r").readlines()]

start = None

for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == ord("S") - 83:
            start = (x, y)
            lines[y][x] = ord("a")-83
        if c == ord("E") - 83:
            end = (x, y)
            lines[y][x] = ord("z")-83


class Graph:
    def __init__(self, l):
        self.l = l

    def get_neighbors(self, v):
        x, y = v
        neighbours = []
        if x-1 >= 0:
            if self.l[y][x-1] -1 <= self.l[y][x]:
                neighbours.append(((x-1, y), 1))
        if x+1 < len(self.l[0]):
            if self.l[y][x + 1] - 1 <= self.l[y][x]:
                neighbours.append(((x+1, y), 1))
        if y-1 >= 0:
            if self.l[y - 1][x] - 1 <= self.l[y][x]:
                neighbours.append(((x, y-1), 1))
        if y+1 < len(self.l):
            if self.l[y + 1][x] - 1 <= self.l[y][x]:
                neighbours.append(((x, y+1), 1))
        return neighbours

    def a_star(self, start, stop):
        open_lst = {start}
        closed_lst = set([])
        distances_from_start = {start: 0}
        adjacent = {start: start}

        while len(open_lst) > 0:
            n = None

            for v in open_lst:
                if n is None or distances_from_start[v] < distances_from_start[n]:
                    n = v

            if n is None:
                return None

            if n == stop:
                reconst_path = []

                while adjacent[n] != n:
                    reconst_path.append(n)
                    n = adjacent[n]

                reconst_path.reverse()
                return reconst_path

            for (m, weight) in self.get_neighbors(n):
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    adjacent[m] = n
                    distances_from_start[m] = distances_from_start[n] + weight
                else:
                    if distances_from_start[m] > distances_from_start[n] + weight:
                        distances_from_start[m] = distances_from_start[n] + weight
                        adjacent[m] = n

                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)

            open_lst.remove(n)
            closed_lst.add(n)
        return None


graph = Graph(lines)

path = graph.a_star(start, end)
print(f"Part 1: {len(path)}")

starting_positions = []
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == ord("a") - 83:
            starting_positions.append((x, y))
distances = []
for s in starting_positions:
    g = graph.a_star(s, end)
    if g:
        distances.append(len(g))
print(f"Part 2: {min(distances)}")
