import collections
import functools
import itertools
import math
import re
import parse as parselib
from pprint import pprint

# from sympy import symbols, Eq, solve
import sympy


import utils

def parse(inpt):
    values = {}
    unsolved = {}
    for line in inpt:
        monkey, value = line.split(': ')
        try:
            values[monkey] = int(value)
        except ValueError:
            if monkey == 'root':
                m1, op, m2 = value.split()
                unsolved[monkey] = f"{m1} == {m2}"
            else:
                unsolved[monkey] = value
    return values, unsolved

def solve(values, unsolved, key="root"):
    while key not in values:
        current_unsolved = unsolved.items()
        for monkey, equation in list(current_unsolved):
            m1, op, m2 = equation.split()
            if m1 in values and m2 in values:
                value = eval(f"{values[m1]} {op} {values[m2]}")
                values[monkey] = value
                unsolved.pop(monkey)
            else:
                continue
    return values[key]

def do_part_1(inpt):
    values, unsolved = parse(inpt)
    return solve(values, unsolved)


def parse_part2(inpt):
    values = {}
    for line in inpt:
        monkey, value = line.split(': ')
        try:
            values[monkey] = int(value)
        except ValueError:
            values[monkey] = value
    return values

def sub_val(values, val):
    if type(val) is int or val == 'x':
        return val
    m1, op, m2 = val.split()
    return f"({sub_val(values, values[m1])} {op} {sub_val(values, values[m2])})"

def substitution_solve(values, key="root"):
    root_a, root_b = values[key].split(' + ')
    root_a = sub_val(values, values[root_a])
    root_b = sub_val(values, values[root_b])

    goal = None
    equation = None
    try:
        goal = eval(root_a)
    except:
        equation = root_a

    try:
        goal = eval(root_b)
    except TypeError:
        equation = root_b

    x = sympy.symbols('x')
    expr = eval(equation) - goal
    print(equation)
    print(expr)

    sol = sympy.solve(expr) 
    print(sol)
    return(sol[0])


def do_part_2(inpt):
    values = parse_part2(inpt)
    values['humn'] = 'x'
    x = substitution_solve(values)
    print(x)

    # double check it
    values, unsolved = parse(inpt)
    m1, op, m2 = unsolved["root"].split()
    unsolved["root"] = f"{m1} == {m2}"
    values['humn'] = x
    print(solve(values, unsolved))


def go(input_file, part):
    inpt = utils.load_input_file(input_file)
    if part == 1:
        return do_part_1(inpt)
    else:
        return do_part_2(inpt)

# Part 1: 959
# Part 2: 1214