
#!/usr/bin/env python
# coding: utf-8

# read input
inp = open("inp/input_02.txt").read().splitlines()
inp = [line.split(' ') for line in inp]

# A = rock, B = paper, C = scissors
# part 1 : X = rock (1), Y = paper (2), Z = scissors (3)
# part 2 : X = lose (0), Y = draw (3), Z = win (6)

def game_outcome(elf, player, part):
    
    if player == 'X':
        if elf == 'A':
            res = 3 + 1 if part == 1 else 3 + 0
        elif elf == 'B':
            res = 0 + 1 if part == 1 else 1 + 0
        elif elf == 'C':
            res = 6 + 1 if part == 1 else 2 + 0
            
    elif player == 'Y':
        if elf == 'A':
            res = 6 + 2 if part == 1 else 1 + 3
        elif elf == 'B':
            res = 3 + 2 if part == 1 else 2 + 3
        elif elf == 'C':
            res = 0 + 2 if part == 1 else 3 + 3
            
    elif player == 'Z':
        if elf == 'A':
            res = 0 + 3 if part == 1 else 2 + 6
        elif elf == 'B':
            res = 6 + 3 if part == 1 else 3 + 6
        elif elf == 'C':
            res = 3 + 3 if part == 1 else 1 + 6
            
    return res

def compute_score(inp, part):
    return sum(game_outcome(elf, player,  part) for elf, player in inp)


# part 1
print("Result for part 1: ", compute_score(inp, 1))  # 13565

# part 2
print("Result for part 2: ", compute_score(inp, 2))  # 12424