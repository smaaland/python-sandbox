sequence = open("input15.txt", "r").read().strip().split(",")


def _hash(expr):
    h = 0
    for c in expr:
        h += ord(c)
        h *= 17
        h %= 256
    return h


print(f"Part 1: {sum([_hash(expr) for expr in sequence])}")
