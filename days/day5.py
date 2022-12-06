import collections
import functools
import itertools
import math
import re
import parse as parselib
from pprint import pprint

import utils

from collections import deque

operation_parse = parselib.compile("move {:d} from {:d} to {:d}")

def modified_chunk(s, n):
    for i in range(0, len(s), n):
        yield s[i:i+n-1]

def print_code(queues):
    for queue in queues:
        print(queue.pop(), end="")
    print()

def read_input(inpt):
    line0 = inpt[0]
    n_queues = (len(line0) + 1) // 4
    queues = [deque() for _ in range(n_queues)]
    for il, line in enumerate(inpt):
        if line == '\n':
            return queues, il
        for i, chunk in enumerate(modified_chunk(line, 4)):
            if '[' in chunk:
                queues[i].appendleft(chunk[1])
    return queues

def do_manipulation(queues, line):
    n, origin, dest = operation_parse.parse(line)
    for _ in range(n):
        queues[dest-1].append(queues[origin-1].pop())
    return queues

def do_manipulation_part2(queues, line):
    n, origin, dest = operation_parse.parse(line)
    temp_queue = deque()
    for _ in range(n):
        temp_queue.append(queues[origin-1].pop())
    for _ in range(n):
        queues[dest-1].append(temp_queue.pop())
    return queues


def do_part_1(inpt):
    queues, first_line = read_input(inpt)
    inpt = [l.strip() for l in inpt[first_line+1:]]
    for line in inpt:
        queues = do_manipulation(queues, line)
    print_code(queues)

def do_part_2(inpt):
    queues, first_line = read_input(inpt)
    inpt = [l.strip() for l in inpt[first_line+1:]]
    for line in inpt:
        queues = do_manipulation_part2(queues, line)
    print_code(queues)

def go(input_file, part):
    with open('inputs/' + input_file, 'r') as f:
        inpt = [l for l in f.readlines()]
    if part == 1:
        return do_part_1(inpt)
    else:
        return do_part_2(inpt)


# Part 1: 4313
# Part 2: 3511