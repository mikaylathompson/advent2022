import collections
import functools
import itertools
import math
import re
import parse as parselib
from pprint import pprint

import utils


def parse_path(line):
    corners = line.split(' -> ')
    return [tuple(utils.split_as_ints(',', corner)) for corner in corners]


def get_rock_coords(paths):
    rocks = set()
    for path in paths:
        c0 = path[0]
        rocks.add(c0)
        for corner in path[1:]:
            rocks.add(corner)
            if c0[1] == corner[1]:
                if c0[0] > corner[0]:
                    xs = range(corner[0]+1, c0[0])
                else:
                    xs = range(c0[0]+1, corner[0])
                for x in xs:
                    rocks.add((x, c0[1]))
            else:
                if c0[1] > corner[1]:
                    ys = range(corner[1]+1, c0[1])
                else:
                    ys = range(c0[1]+1, corner[1])
                for y in ys:
                    rocks.add((c0[0], y))
            c0 = corner
    return rocks


def next_sand_point(grain, blockers, floor=None):
    if floor:
        if grain[1] + 1 == floor:
            return grain
    if (grain[0], grain[1]+1) not in blockers:
        return (grain[0], grain[1]+1)
    if (grain[0]-1, grain[1]+1) not in blockers:
        return (grain[0]-1, grain[1]+1)
    if (grain[0]+1, grain[1]+1) not in blockers:
        return (grain[0]+1, grain[1]+1)
    return grain


def simulate_sandgrain(sand, rocks, sand_entry, lowest_rock):
    blockers = sand.union(rocks)
    grain = sand_entry
    while grain[1] <= lowest_rock:
        next_grain = next_sand_point(grain, blockers)
        if grain == next_grain:
            sand.add(grain)
            return False
        grain = next_grain

    return True


def simulate_sandgrain_w_floor(sand, rocks, sand_entry, floor):
    blockers = sand.union(rocks)
    grain = sand_entry
    while sand_entry not in sand:
        next_grain = next_sand_point(grain, blockers, floor=floor)
        if grain == next_grain:
            sand.add(grain)
            return False
        grain = next_grain

    return True


def do_part_1(inpt):
    paths = [parse_path(line) for line in inpt]
    rocks = get_rock_coords(paths)
    lowest_rock = max([r[1] for r in rocks])
    sand_entry = (500, 0)

    sand = set()

    while True:
        end = simulate_sandgrain(sand, rocks, sand_entry, lowest_rock)
        # print(end, sand)
        if end:
            return len(sand)


def do_part_2(inpt):
    paths = [parse_path(line) for line in inpt]
    rocks = get_rock_coords(paths)
    floor = max([r[1] for r in rocks]) + 2
    sand_entry = (500, 0)

    sand = set()

    while True:
        end = simulate_sandgrain_w_floor(sand, rocks, sand_entry, floor)
        # print(end, sand)
        if end:
            return len(sand)


def go(input_file, part):
    inpt = utils.load_input_file(input_file)
    if part == 1:
        return do_part_1(inpt)
    else:
        return do_part_2(inpt)

# Part 1: 1416
# Part 2: 1124