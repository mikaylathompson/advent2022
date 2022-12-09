import collections
import functools
import itertools
import math
import re
import parse as parselib
from pprint import pprint

import utils

dirs = {
    'U': utils.FOUR_DIRECTIONS[0],
    'D': utils.FOUR_DIRECTIONS[2],
    'R': utils.FOUR_DIRECTIONS[1],
    'L': utils.FOUR_DIRECTIONS[3]
}

def move(pos, dir):
    return (pos[0] + dirs[dir][0], pos[1] + dirs[dir][1])


def tail_needs_to_move(head, tail):
    return max([abs(tail[0] - head[0]), abs(tail[1] - head[1])]) >= 2


def new_tail_position(head, tail):
    x, y = 0, 0
    if head[0] > tail[0]:
        x = 1
    elif head[0] < tail[0]:
        x = -1
    if head[1] > tail[1]:
        y = 1
    elif head[1] < tail[1]:
        y = -1
    return (tail[0] + x, tail[1] + y)


def simulate_move(dir, head_position, tail_position):
    head_position = move(head_position, dir)
    if not tail_needs_to_move(head_position, tail_position):
        return head_position,tail_position
    tail_position = new_tail_position(head_position, tail_position)
    return head_position, tail_position


def simulate_multi_moves(dir, head_position, knot_positions):
    head_position = move(head_position, dir)
    for i, knot in enumerate(knot_positions):
        if i == 0:
            head = head_position
        else:
            head = knot_positions[i-1]

        if tail_needs_to_move(head, knot):
            knot = new_tail_position(head, knot)
            knot_positions[i] = knot
    return head_position, knot_positions


def do_part_1(inpt):
    tail_visited = set()
    head_position = (0,0)
    tail_position = head_position
    tail_visited.add(tail_position)
    for line in inpt:
        for _ in range(int(line[2:])):
            head_position, tail_position = simulate_move(line[0], head_position, tail_position)
            tail_visited.add(tail_position)
    return len(tail_visited)


def do_part_2(inpt):
    tail_visited = set()
    head_position = (0,0)
    knot_positions = [(0,0)] * 9
    tail_visited.add(knot_positions[-1])
    for line in inpt:
        for _ in range(int(line[2:])):
            head_position, knot_positions = simulate_multi_moves(line[0], head_position, knot_positions)
            tail_visited.add(knot_positions[-1])
    return len(tail_visited)


def go(input_file, part):
    inpt = utils.load_input_file(input_file)
    if part == 1:
        return do_part_1(inpt)
    else:
        return do_part_2(inpt)

# Part 1: 2069
# Part 2: 939 (best yet!)