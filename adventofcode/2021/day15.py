import copy

lines = [[int(x) for x in line.strip()] for line in open('input15.txt', 'r').readlines()]


class Graph:
    def __init__(self, l):
        self.l = l

    def get_neighbors(self, v):
        x, y = v
        neighbours = []
        if x-1 >= 0:
            neighbours.append(((x-1, y), int(self.l[y][x-1])))
        if x+1 < len(self.l[0]):
            neighbours.append(((x+1, y), int(self.l[y][x+1])))
        if y-1 >= 0:
            neighbours.append(((x, y-1), int(self.l[y-1][x])))
        if y+1 < len(self.l):
            neighbours.append(((x, y+1), int(self.l[y+1][x])))
        return neighbours

    # This is heuristic function which is having equal values for all nodes
    def h(self, n):
        return 1

    def a_star(self, start, stop):
        open_lst = {start}
        closed_lst = set([])

        # distances_from_start has present distances from start to all other nodes
        # the default value is +infinity
        distances_from_start = {start: 0}

        # adjacent mapping of all nodes
        adjacent = {start: start}

        while len(open_lst) > 0:
            n = None

            # it will find a node with the lowest value of h() -
            for v in open_lst:
                if n == None or distances_from_start[v] + self.h(v) < distances_from_start[n] + self.h(n):
                    n = v

            if n is None:
                return None

            # if the current node is the stop
            # then we start again from start
            if n == stop:
                reconst_path = []

                while adjacent[n] != n:
                    reconst_path.append(n)
                    n = adjacent[n]

                reconst_path.reverse()
                return reconst_path

            # for all the neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                # if the current node is not presentin both open_lst and closed_lst
                # add it to open_lst and note n as it's adjacent
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    adjacent[m] = n
                    distances_from_start[m] = distances_from_start[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update adjacent data and distances_from_start data
                # and if the node was in the closed_lst, move it to open_lst
                else:
                    if distances_from_start[m] > distances_from_start[n] + weight:
                        distances_from_start[m] = distances_from_start[n] + weight
                        adjacent[m] = n

                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)

            # remove n from the open_lst, and add it to closed_lst
            # because all of his neighbors were inspected
            open_lst.remove(n)
            closed_lst.add(n)

        return None


graph_1 = Graph(lines)
path = graph_1.a_star((0, 0), (len(lines) - 1, len(lines[0]) - 1))
print(f"Part 1: {sum([int(lines[p[1]][p[0]]) for p in path])}")


def increment_and_carry(x, y):
    z = x + y - 1
    return z % 9 + 1


lines_2 = []
for l in lines:
    new_line = []
    for i in range(5):
        new_line.extend([increment_and_carry(int(x), i) for x in l])
    lines_2.append(new_line)

tmp = copy.copy(lines_2)
for i in range(1, 5):
    new_line = []
    for l in tmp:
        lines_2.append([increment_and_carry(int(x), i) for x in l])

graph_2 = Graph(lines_2)
path_2 = graph_2.a_star((0, 0), (len(lines_2) - 1, len(lines_2[0]) - 1))
print(f"Part 2: {sum([int(lines_2[p[1]][p[0]]) for p in path_2])}")