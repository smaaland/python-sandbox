import functools
from collections import Counter

lines = [line.strip() for line in open("input7.txt", "r").readlines()]


def compare_hands(cx, cy, x, y, card_order):
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


def compare_hands_1(x, y):
    card_order = "AKQJT98765432"
    cx = Counter(x[0])
    cy = Counter(y[0])
    return compare_hands(cx, cy, x, y, card_order)


def compare_hands_2(x, y):
    card_order = "AKQT98765432J"
    cx = Counter(x[0])
    cy = Counter(y[0])

    for c in cx, cy:
        if "J" in c:
            jokers = c["J"]
            del c["J"]
            most_common = c.most_common(1)
            if most_common:
                c[most_common[0][0]] += jokers
            else:
                c["J"] = jokers

    return compare_hands(cx, cy, x, y, card_order)


hands = [(x.split(" ")[0], int(x.split(" ")[1])) for x in lines]

sorted_hands_1 = sorted(hands, key=functools.cmp_to_key(compare_hands_1))
scores_1 = [(i + 1) * hand[1] for i, hand in enumerate(sorted_hands_1)]
print(f"Part 1: {sum(scores_1)}")

sorted_hands_2 = sorted(hands, key=functools.cmp_to_key(compare_hands_2))
scores_2 = [(i + 1) * hand[1] for i, hand in enumerate(sorted_hands_2)]
print(f"Part 2: {sum(scores_2)}")
