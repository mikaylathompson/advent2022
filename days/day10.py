import collections
import functools
import itertools
import math
import re
import parse as parselib
from pprint import pprint

import utils

def operation(op, x):
    if 'noop' in op:
        return x, 1
    else:
        return x + int(op.split()[1]), 2

cycles_of_interest = itertools.count(20, 40)

def do_part_1(inpt):
    x = 1
    cycle = 1
    coi = next(cycles_of_interest)
    signal_strength = 0
    for line in inpt:
        new_x, cycle_change = operation(line, x)
        cycle += cycle_change
        if cycle >= coi:
            if cycle > coi:
                signal_strength += coi * x
            else:
                signal_strength += coi * new_x
            coi = next(cycles_of_interest)
        x = new_x
    return signal_strength

def do_part_2(inpt):
    xs = [1]
    for line in inpt:
        if 'addx' in line:
            xs.append(xs[-1])
            xs.append(xs[-1] + int(line.split()[1]))
        else:
            xs.append(xs[-1])

    logs = []
    for cycle in range(1, 40*6+1):
        x = xs[cycle-1]
        pos = cycle % 40 - 1
        # logs.append(f"Cycle {cycle}: x={x}, pos={pos}")
        if abs(pos-x) <= 1:
            print("#", end="")
        else:
            print(" ", end="")
        if cycle % 40 == 0:
            print()
    # print("\n".join(logs[0:10]))
    return

def go(input_file, part):
    inpt = utils.load_input_file(input_file)
    if part == 1:
        return do_part_1(inpt)
    else:
        return do_part_2(inpt)

# Part 1: 2215
# Part 2: 2777