import functools
from collections import Counter

lines = [line.strip() for line in open("input7.txt", "r").readlines()]


def compare_hands(x, y):
    card_order = "AKQJT98765432"
    cx = Counter(x[0])
    cy = Counter(y[0])
    if max(cx.values()) > max(cy.values()):
        return 1
    elif max(cx.values()) < max(cy.values()):
        return -1
    else:
        if len(cx) < len(cy):
            return 1
        elif len(cx) > len(cy):
            return -1
        else:
            for _x, _y in zip(x[0], y[0]):
                if card_order.find(_x) < card_order.find(_y):
                    return 1
                elif card_order.find(_x) > card_order.find(_y):
                    return -1
    return 0


hands = [(x.split(" ")[0], int(x.split(" ")[1])) for x in lines]
sorted_hands = sorted(hands, key=functools.cmp_to_key(compare_hands))
scores = [(i + 1) * hand[1] for i, hand in enumerate(sorted_hands)]
print(f"Part 1: {sum(scores)}")
