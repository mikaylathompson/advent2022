import collections
import functools
import itertools
import math
import re
import parse as parselib
from pprint import pprint

import utils


def find_shared_item(compA, compB):
    return set(compA).intersection(set(compB)).pop()

def letter_value(x):
    if x.isupper():
        return ord(x) - 38
    return ord(x) - 96


def find_badge(la, lb, lc):
    return set(la).intersection(set(lb)).intersection(set(lc)).pop()


def do_part_1(inpt):
    value = 0
    for line in inpt:
        n = len(line)
        shared = find_shared_item(line[:n//2], line[n//2:])
        # print(shared + " " + str(letter_value(shared)))
        value += letter_value(shared)
    print(value)

def do_part_2(inpt):
    value = 0
    trio = []
    for line in inpt:
        trio.append(line)
        if len(trio) == 3:
            value += letter_value(find_badge(*trio))
            trio = []
    print(value)

def go(input_file, part):
    inpt = utils.load_input_file(input_file)
    if part == 1:
        return do_part_1(inpt)
    else:
        return do_part_2(inpt)

# Part 1: 2935
# Part 2: 1927