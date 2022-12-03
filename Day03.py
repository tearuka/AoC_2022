#!/usr/bin/env python
# coding: utf-8

# read input
inp = open("inp/input_03.txt").read().splitlines()

# list of letters
import string
alphabet_lower = list(string.ascii_lowercase)
alphabet_upper = list(string.ascii_uppercase)
letters = alphabet_lower + alphabet_upper
# list of numbers
numbers = list(range(1,53))
# create dictionary
priority_values = dict(zip(letters, numbers))

# part 1
sum_one = 0
for rucksack in inp:
    first_compartment, second_compartment = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
    common_item = list(set(first_compartment) & set(second_compartment))
    sum_one += priority_values[common_item[0]]

print("Result for part 1: ", sum_one)  # 8202

# part 2
# divide input into chunks of three rucksacks
chunks = [inp[i:i + 3] for i in range(0, len(inp), 3)]
sum_two = 0
for group in chunks:
    first_elf, second_elf, third_elf = group
    badge = list(set(first_elf) & set(second_elf) & set(third_elf))
    sum_two += priority_values[badge[0]]

print("Result for part 2: ", sum_two)  # 2864