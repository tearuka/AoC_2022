#!/usr/bin/env python
# coding: utf-8

# read input
inp = open("inp/input_01.txt").read().split('\n\n')
inp = [line.splitlines() for line in inp]

calories = []
for elf in inp:
    elf = [int(num) for num in elf]
    calories.append(sum(elf))
calories.sort(reverse=True)

# part 1
print("Result for part 1: ", calories[0])  # 68442

# part 2
print("Result for part 2: ", sum(calories[:3]))  # 204837