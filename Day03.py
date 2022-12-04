#!/usr/bin/env python
# coding: utf-8

import string

# read input
inp = open("inp/input_03.txt").read().splitlines()

# dictionary of letters and numbers
alphabet = list(string.ascii_letters)
numbers = list(range(1,53))
priority_values = dict(zip(alphabet, numbers))

# part 1
sum_one = 0
for rucksack in inp:
    first_compartment, second_compartment = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
    common_item = (set(first_compartment) & set(second_compartment)).pop()
    sum_one += priority_values[common_item]

print("Result for part 1: ", sum_one)  # 8202

# part 2
# divide input into chunks of three rucksacks
chunks = [inp[i:i + 3] for i in range(0, len(inp), 3)]
sum_two = 0
for first_elf, second_elf, third_elf in chunks:
    badge = (set(first_elf) & set(second_elf) & set(third_elf)).pop()
    sum_two += priority_values[badge]

print("Result for part 2: ", sum_two)  # 2864