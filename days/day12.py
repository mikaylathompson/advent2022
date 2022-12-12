import collections
import functools
import itertools
import math
import re
import parse as parselib
from pprint import pprint

import utils

def parse(inpt):
    grid = []
    start = (0,0)
    end = (0,0)
    for r, line in enumerate(inpt):
        row = []
        for c, char in enumerate(line):
            if char == 'S':
                start = (r, c)
                row.append(1)
                continue
            elif char == 'E':
                end = (r, c)
                row.append(26)
                continue
            row.append(ord(char) - 96)
        grid.append(row)
    return grid, start, end


def shortest_path(grid, start, end):
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    to_visit = collections.deque()
    to_visit.append((start, 0))

    while len(to_visit) > 0:
        current, steps = to_visit.popleft()
        if current == end:
            return steps

        if current in visited:
            continue
        visited.add(current)

        neighbors = utils.get_neighbor_coordinates(current, (rows, cols))
        for n in neighbors:
            if grid[n[0]][n[1]] <= (grid[current[0]][current[1]] + 1):
                to_visit.append((n, steps + 1))
    return math.inf


def do_part_1(inpt):
    grid, start, end = parse(inpt)
    return shortest_path(grid, start, end)


def parse_part2(inpt):
    grid = []
    starts = []
    end = (0,0)
    for r, line in enumerate(inpt):
        row = []
        for c, char in enumerate(line):
            if char == 'S':
                starts.append((r, c))
                row.append(1)
                continue
            elif char == 'E':
                end = (r, c)
                row.append(26)
                continue
            if char == 'a':
                starts.append((r, c))
            row.append(ord(char) - 96)
        grid.append(row)
    return grid, starts, end


def do_part_2(inpt):
    grid, starts, end = parse_part2(inpt)
    return min([shortest_path(grid, start, end) for start in starts])



def go(input_file, part):
    inpt = utils.load_input_file(input_file)
    if part == 1:
        return do_part_1(inpt)
    else:
        return do_part_2(inpt)

# Part 1: 2280
# Part 2: 1968