import collections
import functools
import itertools
import math
import re
import parse as parselib
from pprint import pprint

import utils

def get_each_chunk(line, n):
    i = n
    while i < len(line):
        yield(line[i-n:i], i)
        i += 1

def do_part_1(inpt):
    for seq, i in get_each_chunk(inpt[0], 4):
        if len(set(seq)) == 4:
            return i
    return None

def do_part_2(inpt):
    for seq, i in get_each_chunk(inpt[0], 14):
        if len(set(seq)) == 14:
            return i
    return None

def go(input_file, part):
    inpt = utils.load_input_file(input_file)
    if part == 1:
        return do_part_1(inpt)
    else:
        return do_part_2(inpt)

# Part 1: 1521
# Part 2: 1673