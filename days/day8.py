import collections
import functools
import itertools
import math
import re
import parse as parselib
from pprint import pprint

import utils

def visible_from_left(grid, visible):
    for r, row in enumerate(grid):
        max_seen = -1
        for c, col in enumerate(row):
            if col > max_seen:
                visible[r][c] = 1
                max_seen = col
    return visible

def visible_from_right(grid, visible):
    for r, row in enumerate(grid):
        max_seen = -1
        for c, col in enumerate(row[::-1]):
            actual_c = len(row) - c - 1
            if col > max_seen:
                visible[r][actual_c] = 1
                max_seen = col
    return visible


def do_part_1(inpt):
    rows = len(inpt)
    cols = len(inpt[0])
    visible = utils.grid(cols, rows, default=0)
    visible_from_right(inpt, visible)
    visible_from_left(inpt, visible)
    visible = visible_from_left(utils.transpose(inpt), utils.transpose(visible))
    visible_from_right(utils.transpose(inpt), visible)

    print(sum([sum(row) for row in visible]))
    return

def calc_scenic_score(trees, r, c):
    height = trees[r][c]
    print(f"tree ({r}, {c})")
    # print("ss: ", r, c, height)
    # visibility to north
    north = 1
    for ri in range(r-1, 0, -1):
        # print("checking north: ", ri, trees[ri][c])
        if trees[ri][c] >= height:
            break
        north += 1
    south = 1
    for ri in range(r+1, len(trees) - 1):
        print(f"checking sourth: ({ri}, {c}): {trees[ri][c]}")
        if trees[ri][c] >= height:
            break
        south += 1
    east = 1
    for ci in range(c-1, 0, -1):
        # print("checking east: ", ri, trees[r][ci])
        if trees[r][ci] >= height:
            break
        east += 1
    west = 1
    for ci in range(c+1, len(trees[0]) - 1):
        print(f"checking west: ({r}, {ci}): {trees[r][ci]}")
        if trees[r][ci] >= height:
            break
        west += 1
    print(north, south, east, west)
    print()
    return north * south * east * west

def do_part_2(inpt):
    pprint(inpt)
    rows = len(inpt)
    cols = len(inpt[0])
    scenic_scores = utils.grid(cols, rows, default=0)
    for r in range(rows):
        for c in range(cols):
            if r == 0 or c == 0 or r == rows-1 or c == cols-1:
                # all edge trees have a score of 0
                continue
            scenic_scores[r][c] = calc_scenic_score(inpt, r, c)

    pprint(scenic_scores)
    print(max([max(row) for row in scenic_scores]))
    return

def go(input_file, part):
    # inpt = utils.load_input_file(input_file)
    inpt = utils.load_as_grid(input_file, sep=None)
    if part == 1:
        return do_part_1(inpt)
    else:
        return do_part_2(inpt)

# Part 1: 1007
# Part 2: 2989