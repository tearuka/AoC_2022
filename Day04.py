#!/usr/bin/env python
# coding: utf-8

import re

# read input
inp = open("inp/input_04.txt").read().splitlines()

def overlap(data, part):

    counter = 0
    for line in data:
        start1, finish1, start2, finish2 = [int(num) for num in re.split('-|,|-', line)]
        range1 = range(start1, finish1 + 1)
        range2 = range(start2, finish2 + 1)
        
        if part == 1:
            if start1 in range2 and finish1 in range2:
                counter += 1
            elif start2 in range1 and finish2 in range1:
                counter += 1
                
        if part == 2:
            if start1 in range2 or finish1 in range2:
                counter += 1
            elif start2 in range1 or finish2 in range1:
                counter += 1        
        
    return counter

print("Result for part 1: ", overlap(inp, 1))  # 534

print("Result for part 2: ", overlap(inp, 2))  # 841