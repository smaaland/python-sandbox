import copy
import sys
from itertools import groupby


def run(_maps, _seeds):
    for _map in _maps:
        moved = [False for _ in _seeds]
        for line in _map[1:]:
            destination_range_start, source_range_start, range_length = [
                int(x) for x in line.split(" ")
            ]
            for i, seed in enumerate(_seeds):
                if not moved[i]:
                    if source_range_start <= seed < source_range_start + range_length:
                        _seeds[i] = destination_range_start + seed - source_range_start
                        moved[i] = True
    return _seeds


def find_boundaries(_maps):
    _boundaries = [0, sys.maxsize]
    for map_ in reversed(_maps):
        new_boundaries = []
        for x in _boundaries:
            already_moved = False
            for condition in map_[1:]:
                dst_start, src_start, range_len = [int(c) for c in condition.split()]
                diff = dst_start - src_start
                if src_start + diff <= x < src_start + range_len + diff:
                    affected_input_value = x - (dst_start - src_start)
                    if (
                        affected_input_value >= 0
                        and affected_input_value not in new_boundaries
                    ):
                        new_boundaries.append(affected_input_value)
                    already_moved = True
            if not already_moved:
                new_boundaries.append(x)
        for condition in map_[1:]:
            dst_start, src_start, range_len = [int(c) for c in condition.split()]
            to_add = [
                src_start - 1,
                src_start,
                src_start + range_len,
                src_start + range_len - 1,
            ]
            for a in to_add:
                if a not in new_boundaries and a >= 0:
                    new_boundaries.append(a)
        _boundaries = new_boundaries
    return _boundaries


lines = [line.strip() for line in open("input5.txt", "r").readlines()]
input_ = [list(g) for k, g in groupby(lines, key=bool) if k]
seeds = [int(x) for x in input_[0][0].split(":")[1].split()]
seeds_2 = copy.copy(seeds)
maps = input_[1:]

boundaries = find_boundaries(maps)
it = iter(seeds_2)
seed_2_boundaries = []
for x, y in zip(it, it):
    seed_2_boundaries.append(x)
    seed_2_boundaries.append(x + y - 1)
for x in seed_2_boundaries:
    if x not in boundaries:
        boundaries.append(x)


def between_boundaries(val, sb):
    _it = iter(sb)
    for x, y in zip(_it, _it):
        if x <= val <= y:
            return True
    return False


print(f"Part 1: {min(run(maps, seeds))}")
print(
    f"Part 2: {min(run(maps, [x for x in boundaries if between_boundaries(x, seed_2_boundaries)]))}"
)
