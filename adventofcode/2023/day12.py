from functools import cache

lines = [line.strip() for line in open("input12.txt", "r").readlines()]


@cache
def get_combinations(condition, set_lengths, cursor, int_set_cursor, num_sets_seen):
    if cursor == len(condition):
        return 1 if len(set_lengths) == num_sets_seen else 0
    elif condition[cursor] == "#":
        return get_combinations(
            condition=condition,
            set_lengths=set_lengths,
            cursor=cursor + 1,
            int_set_cursor=int_set_cursor + 1,
            num_sets_seen=num_sets_seen,
        )
    elif condition[cursor] == "." or num_sets_seen == len(set_lengths):
        if (
            num_sets_seen < len(set_lengths)
            and int_set_cursor == set_lengths[num_sets_seen]
        ):
            cursor += 1
            int_set_cursor = 0
            num_sets_seen += 1
        elif int_set_cursor == 0:
            cursor += 1
        else:
            return 0

        return get_combinations(
            condition=condition,
            set_lengths=set_lengths,
            cursor=cursor,
            int_set_cursor=int_set_cursor,
            num_sets_seen=num_sets_seen,
        )
    else:
        broken_count = get_combinations(
            condition=condition,
            set_lengths=set_lengths,
            cursor=cursor + 1,
            int_set_cursor=int_set_cursor + 1,
            num_sets_seen=num_sets_seen,
        )
        working_count = 0
        if int_set_cursor == set_lengths[num_sets_seen]:
            working_count = get_combinations(
                condition=condition,
                set_lengths=set_lengths,
                cursor=cursor + 1,
                int_set_cursor=0,
                num_sets_seen=num_sets_seen + 1,
            )
        elif int_set_cursor == 0:
            working_count = get_combinations(
                condition=condition,
                set_lengths=set_lengths,
                cursor=cursor + 1,
                int_set_cursor=0,
                num_sets_seen=num_sets_seen,
            )
        return broken_count + working_count


combinations_1 = []
combinations_2 = []
for line in lines:
    condition = line.split(" ")[0]
    set_lengths = tuple([int(x) for x in line.split(" ")[1].split(",")])

    combinations_1.append(get_combinations(condition + ".", set_lengths, 0, 0, 0))
    combinations_2.append(
        get_combinations("?".join([condition] * 5) + ".", set_lengths * 5, 0, 0, 0)
    )
print(f"Part1: {sum(combinations_1)}")
print(f"Part2: {sum(combinations_2)}")
