import collections
import functools
import itertools
import math
import re
import parse as parselib
from pprint import pprint

import json
from random import randint

import utils


LEFT = 'left'
RIGHT = 'right'

def compare(left, right, debug=False, indent=0):
    if debug:
        print("\t"*indent, left, right)
    if type(left) == int and type(right) == int:
        if debug: print("\t"*indent, "int compare")
        if left < right:
            return LEFT
        if right < left:
            return RIGHT
        return None
    if type(left) == list and type(right) == list:
        if debug: print("\t"*indent, "list compare")
        if len(left) == 0 and len(right) == 0:
            return None
        if len(left) == 0:
            return LEFT
        elif len(right) == 0:
            return RIGHT

        for i in range(len(left)):
            try:
                compare_i = compare(left[i], right[i], debug=debug, indent=indent+1)
            except IndexError:
                if debug: print("\t"*indent, 'IndexError')
                return RIGHT
            if debug: print("\t"*indent, f"result at {i=}: {compare_i}")
            if compare_i is None:
                continue
            return compare_i
        if len(left) < len(right):
            return LEFT
        return None

    if type(left) == int and type(right) != int:
        if debug: print("\t"*indent,"mixed compare (left int)")
        left = [left]
        return compare(left, right, debug=debug, indent=indent+1)
    elif type(right) == int and type(left) != int:
        if debug: print("\t"*indent,"mixed compare (right int)")
        right = [right]
        return compare(left, right, debug=debug, indent=indent+1)
    return None

def do_part_1(inpt):
    score = 0
    for i, pair in enumerate(list(itertools.pairwise(inpt))[::3]):
        # print(i + 1, *pair)
        left = json.loads(pair[0])
        right = json.loads(pair[1])
        result = compare(left, right, debug=(i in [0, 1, 2, 3, 4]))
        if result != RIGHT:
            # print(result)
            # print("OK")
            score += i + 1
        # print()
    return score


def quicksort(arr):
  if len(arr) <= 1:
    return arr
  pivot = arr[len(arr) // 2]
  comparisons = [(x, compare(x, pivot)) for x in arr]
  left = [x for x, c in comparisons if c == LEFT]
  middle = [x for x, c in comparisons if c == None]
  right = [x for x, c in comparisons if c == RIGHT]
  return quicksort(left) + middle + quicksort(right)


def do_part_2(inpt):
    key1 = [[2]]
    key2 = [[6]]
    messages = [json.loads(line) for line in inpt if line != ''] + [key1, key2]
    sorted_messages = quicksort(messages)
    # print(sorted_messages)
    i1 = sorted_messages.index(key1)+1
    i2 = sorted_messages.index(key2)+1
    # print(i1, i2)
    return i1 * i2

def go(input_file, part):
    inpt = utils.load_input_file(input_file)
    if part == 1:
        return do_part_1(inpt)
    else:
        return do_part_2(inpt)

# Part 1: 4091
# Part 2: 3669
# Misunderstood lots of little details and very bogged down in bugs in part 1, frusturating day.