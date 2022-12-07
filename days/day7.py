import collections
import functools
import itertools
import math
import re
import parse as parselib
from pprint import pprint

import utils

CD = "cd"
LS = "ls"
DIR = "dir"
FILE = "file"

def parse_line(line):
    if line[0] == "$":
        # command
        if line[2:4] == "cd":
            return (CD, line[5:])
        return (LS, )
    # file
    if line[0:3] == "dir":
        return (DIR, line[4:])
    size, name = line.split()
    return (FILE, name, int(size))


def tree_for_path(tree, path):
    components = path.split('/')[1:]
    for component in components:
        tree = tree[component]
    return tree


def build_tree(lines):
    tree = {}
    current_path = ''
    for line in lines[1:]:
        current_tree = tree_for_path(tree, current_path)
        if line[0] == CD:
            if line[1] == '..':
                current_path = current_path.rsplit('/', maxsplit=1)[0]
                continue
            else:
                current_path += '/' + line[1]
                continue
        elif line[0] == LS:
            continue
        elif line[0] == DIR:
            current_tree[line[1]] = {}
        else:
            # FILE
            current_tree[line[1]] = line[2]
    return tree


def get_size(tree):
    if type(tree) == int:
        return tree
    else:
        return sum(get_size(leaf) for _, leaf in tree.items())


def get_dir_sizes(tree):
    sizes = [get_size(tree)]
    for x in [x for x in tree.values() if type(x) == dict]:
        sizes += get_dir_sizes(x)
    return sizes


def do_part_1(inpt):
    lines = [parse_line(line) for line in inpt]
    tree = build_tree(lines)
    # pprint(tree)
    max_size = 100000
    sizes = get_dir_sizes(tree)
    print(sum(size for size in sizes if size < max_size))


def do_part_2(inpt):
    total_disk      = 70000000
    necessary_space = 30000000
    lines = [parse_line(line) for line in inpt]
    tree = build_tree(lines)
    used_space = get_size(tree)
    all_sizes = get_dir_sizes(tree)

    current_free_space = total_disk - used_space
    needs_to_be_freed = necessary_space - current_free_space

    to_delete = min([size for size in all_sizes if size >= needs_to_be_freed])
    print(to_delete)


def go(input_file, part):
    inpt = utils.load_input_file(input_file)
    if part == 1:
        return do_part_1(inpt)
    else:
        return do_part_2(inpt)


# Part 1: 2425
# Part 2: 1938