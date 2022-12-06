#!/usr/bin/env python
# coding: utf-8

# read input
inp = open("inp/input_06.txt").read()

def find_signal(string, part):
    seq = 4 if part == 1 else 14
    for i in range(len(string)- seq - 1):
        if len(string[i:i+seq]) == len(set(string[i:i+seq])):
            return i+seq

# part 1
print("Result for part 1: ", find_signal(inp, 1))  # 1892

# part 2
print("Result for part 2: ", find_signal(inp, 2))  # 2313