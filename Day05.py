#!/usr/bin/env python
# coding: utf-8

import re
import copy

# read input
inp = open("inp/input_05.txt").read().splitlines()
stacks_raw, instructions = inp[:8], inp[10:]

# parse stacks_raw
stacks = [[] for i in range(9)]
for i in range(len(stacks_raw )- 1, -1, -1):
    for stack_number in range(9):
        position = list(range(1, len(stacks_raw[0]), 4))[stack_number]
        if stacks_raw[i][position] != ' ':
            stacks[stack_number].append(stacks_raw[i][position])


def move_crates(stacks, instructions, part):
    for line in instructions:
        nb_crates, start_pos, finish_pos = [int(num) for num in re.split('e | from | to ',line[5:])]
        
        if part == 1:
            for _ in range(nb_crates):
                el = stacks[start_pos - 1].pop()
                stacks[finish_pos - 1].append(el)
        
        if part == 2:
            el = stacks[start_pos - 1][-nb_crates:]
            stacks[start_pos - 1] = stacks[start_pos - 1][:-nb_crates]
            stacks[finish_pos - 1] = stacks[finish_pos - 1] + el
    
    # collect the crates on top
    return ''.join([stack.pop() for stack in stacks])


print("Result for part 1: ", move_crates(copy.deepcopy(stacks), instructions, 1)) # 'DHBJQJCCW'

print("Result for part 2: ", move_crates(copy.deepcopy(stacks), instructions, 2)) # 'WJVRLSJJT'