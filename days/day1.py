import collections
import functools
import itertools
import math
import re
import parse as parselib
from pprint import pprint

import utils


def do_part_1(inpt):
    max_cals = 0
    current_cals = 0
    for line in inpt:
        if line == '':
            if current_cals > max_cals:
                max_cals = current_cals
            current_cals = 0
        else:
            current_cals += int(line)
    return max_cals

def do_part_2(inpt):
    cals = []
    current_cals = 0
    for line in inpt:
        if line == '':
            cals.append(current_cals)
            current_cals = 0
        else:
            current_cals += int(line)
    cals.append(current_cals)
    return sum(sorted(cals, reverse=True)[:3])


def go(input_file, part):
    inpt = utils.load_input_file(input_file)
    if part == 1:
        return do_part_1(inpt)
    else:
        return do_part_2(inpt)

# Part 1: 108099
# Part 2: 102897
# I forgot that these start on the eve of December, so didn't think of it until the next day.