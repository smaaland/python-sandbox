sizes = []
correct_combinations = 0
min_no = None
ways = {}

with open('input17.txt', 'r') as f:
    for line in f:
        sizes.append(int(line))

def sumup(left, total):
    if total == 150:
        global correct_combinations
        correct_combinations += 1
        return
    elif total > 150:
        return
    if len(left):
        i = left[0]
        sumup(left[1:], total + i)
        sumup(left[1:], total)


def sumup_s(left, total, used):
    if total == 150:
        global correct_combinations, min_no
        correct_combinations += 1

        if used in ways:
            ways[used] +=1
        else:
            ways[used] = 1

        if min_no is None:
            min_no = used
        else:
            min_no = used if used < min_no else min_no
        return
    elif total > 150:
        return
    if len(left):
        i = left[0]
        sumup_s(left[1:], total + i, used + 1)
        sumup_s(left[1:], total, used)


sumup(sizes, 0)
print(correct_combinations)

correct_combinations = 0
sumup_s(sizes, 0, 0)
print(min_no)
print(ways[min_no])