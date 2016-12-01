'''import re

last = False
replacements = list()
all = list()
used = dict()

# start = 'e'
# start_len = 1
goal = 'e'
goal_len = 1

with open('input19.txt', 'r') as f:
    for line in f:
        if line != '\n':
            if not last:
                temp = line.split('\n')[0].split(' => ')
                replacements.append(temp)
            else:
                start = line
                start_len = len(start)
                # goal = line
                # goal_len = len(goal)
        else:
            last = True


def do_iter(current, count=0):
    count +=1
    for rep in replacements:
        places = [m.start() for m in re.finditer(rep[1], current)]
        l = len(rep[1])
        for place in places:
            # number_of_end_characters = (start_len-place)-l
            # all.append(start[:place] + rep[1] + start[place+l:])
            new_str = current[:place] + rep[0] + current[place+l:]
            #if len(new_str) <= len(goal):
            print(new_str)

            if new_str == goal:
                print('yay')
                print(count)
            else:
                dead = False
                if new_str in used:
                    if used[new_str] <= count:
                        # We already have been here with a lower or similar count, drop dead
                        dead = True
                    else:
                        used[new_str] = count
                else:
                    used[new_str] = count

                if not dead:
                    # print((used))
                    # TODO keep iterating
                    # print(new_str)
                    do_iter(new_str, count)
                # else:
                    # Do nothing
                    # print(new_str)
                    # pass

    # print(len(all))
    # print(len(set(all)))

do_iter(start)
'''


def neighbours(base, replacements):
    molecules = set()
    for before, after in replacements:
        for i in range(len(base)):
            if base[i : i + len(before)] == before:
                base_chars = list(base)
                base_chars[i : i + len(before)] = list(after)
                molecules.add(''.join(base_chars))
    return sorted(molecules)  # Sorting makes the running time more consistent.

with open('input19.txt', 'r') as f:
    rows = f.read().strip().split('\n')

target = rows[-1]
replacements = []
for row in rows[:-2]:
    before, after = row.split(' => ')
    replacements.append((before, after))

molecules = neighbours(target, replacements)
print('There are %d possible molecules.' % len(molecules))

start, target = target, 'e'
for i in range(len(replacements)):
    before, after = replacements[i]
    replacements[i] = after, before

frontier = [(start, 0)]
steps = 0
while frontier and not steps:  # Terminate as soon as we find a path.
    curr, dist = frontier.pop()
    for neighbour in neighbours(curr, replacements):
        frontier.append((neighbour, dist + 1))
        if neighbour == target:
            steps = dist + 1

print('The target can be reached in %d replacements.' % steps)