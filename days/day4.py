import collections
import functools
import itertools
import math
import re
import parse as parselib
from pprint import pprint

import utils

pattern = parselib.compile("{:d}-{:d},{:d}-{:d}")

def do_part_1(inpt):
    count = 0
    for line in inpt:
        a1,b1,a2,b2 = pattern.parse(line)
        if a1 <= a2 and b1 >= b2:
            count += 1
        elif a2 <= a1 and b2 >= b1:
            count += 1
    print(count)

def do_part_2(inpt):
    count = 0
    for line in inpt:
        a1,b1,a2,b2 = pattern.parse(line)
        if a1 <= a2 <= b1:
            count += 1
        elif a2 <= a1 <= b2:
            count += 1
    print(count)


def go(input_file, part):
    inpt = utils.load_input_file(input_file)
    if part == 1:
        return do_part_1(inpt)
    else:
        return do_part_2(inpt)

# Part 1: 6097
# Part 2: 5207