import collections
import functools
import itertools
import math
import re
import parse as parselib
from pprint import pprint

import utils

rock = ['A', 'X', 0]
paper = ['B', 'Y', 1]
scissors = ['C', 'Z', 2]

def get_value(play):
    if play in rock:
        return 1
    if play in paper:
        return 2
    return 3

def match_score(opp, you):
    opp = get_value(opp)
    you = get_value(you)
    # tie
    if opp == you:
        return 3 + you
    # opp wins
    if opp - 1 == you or opp + 2 == you:
        return 0 + you
    return 6 + you


def do_part_1(inpt):
    score = 0
    for line in inpt:
        score += match_score(line[0], line[2])
    print(score)

def get_your_play(opp, result):
    if (opp, result) in [('A', 'Y'), ('B', 'X'), ('C', 'Z')]:
        return 'X'
    if (opp, result) in [('A', 'Z'), ('B', 'Y'), ('C', 'X')]:
        return 'Y'
    return 'Z'


def do_part_2(inpt):
    score = 0
    for line in inpt:
        play = get_your_play(line[0], line[2])
        score += match_score(line[0], play)
    print(score)

def go(input_file, part):
    inpt = utils.load_input_file(input_file)
    if part == 1:
        return do_part_1(inpt)
    else:
        return do_part_2(inpt)

# Part 1: 13537
# Part 2: 12414
# Stuck hosting a dinner party past 10pm, so another late start
# also I hated this one.