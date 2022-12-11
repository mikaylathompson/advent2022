import collections
import functools
import itertools
import math
import re
import parse as parselib
from pprint import pprint

import utils

from collections import deque

import sys
sys.set_int_max_str_digits(1000000)

class Operation:
    def __init__(self, line):
        self.string = line

    def apply(self, old):
        return eval(self.string.replace('old', str(old)))


class Monkey:
    def __init__(self, part=1):
        self.part = part
        self.objects = []
        self.operation = None
        self.test_value = None
        self.true_destination = None
        self.false_destination = None
        self.inspection_count = 0
        self.divisor = 0
        return

    def take_turn(self):
        throws = []
        while len(self.objects) > 0:
            throws.append(self.inspect_next())
        return throws

    def inspect_next(self):
        self.inspection_count += 1
        object_worry = self.objects.pop(0)
        new = self.operation.apply(object_worry)
        if self.part == 1:
            new = new // 3
        else:
            new = new % self.divisor
        # print(f"{self.objects=} {self.test_value=} {self.operation.string}")
        if new % self.test_value == 0:
            return (new, self.true_destination)
        return (new, self.false_destination)

def create_monkeys(inpt, part=1):
    monkeys = []
    current_monkey = None
    all_test_values = []
    for line in inpt:
        if 'Monkey' in line:
            current_monkey = Monkey(part=part)
            monkeys.append(current_monkey)
        if 'Starting' in line:
            current_monkey.objects = list(map(int, line.split(':')[1].split(', ')))
        if 'Operation' in line:
            current_monkey.operation = Operation(line.split('=')[1])
        if 'Test' in line:
            current_monkey.test_value = int(line.split()[-1])
            all_test_values.append(int(line.split()[-1]))
        if 'true' in line:18170818354
            current_monkey.true_destination = int(line.split()[-1])
        if 'false' in line:
            current_monkey.false_destination = int(line.split()[-1])
    if part == 2:
        gcd = math.prod(all_test_values)
        print(gcd)
        for monkey in monkeys:
            monkey.divisor = gcd
    return monkeys

def do_part_1(inpt):
    monkeys = create_monkeys(inpt)
    for round_ in range(20):
        for monkey in monkeys:
            throws = monkey.take_turn()
            for value, dest in throws:
                monkeys[dest].objects.append(value)
    inspects = sorted([m.inspection_count for m in monkeys])
    return inspects[-1] * inspects[-2]


    return

def do_part_2(inpt):
    monkeys = create_monkeys(inpt, part=2)
    for round_ in range(10000):
        if round_ % 100 == 0:
            print(round_)
        for monkey in monkeys:
            throws = monkey.take_turn()
            for value, dest in throws:
                monkeys[dest].objects.append(value)
    inspects = sorted([m.inspection_count for m in monkeys])
    return inspects[-1] * inspects[-2]

def go(input_file, part):
    inpt = utils.load_input_file(input_file)
    if part == 1:
        return do_part_1(inpt)
    else:
        return do_part_2(inpt)

# Part 1: 866
# Part 2: 638 -- both are new bests for the year!