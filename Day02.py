
#!/usr/bin/env python
# coding: utf-8

# read input
inp = open("inp/input_02.txt").read().splitlines()
inp = [line.split(' ') for line in inp]

# A = rock, B = paper, C = scissors
# part 1 : X = rock (1), Y = paper (2), Z = scissors (3)
# part 2 : X = lose (0), Y = draw (3), Z = win (6)

def game_outcome(line, part):
    
    if line[1] == 'X':
        if line[0] == 'A':
            res = 3 + 1 if part == 1 else 3 + 0
        elif line[0] == 'B':
            res = 0 + 1 if part == 1 else 1 + 0
        elif line[0] == 'C':
            res = 6 + 1 if part == 1 else 2 + 0
            
    elif line[1] == 'Y':
        if line[0] == 'A':
            res = 6 + 2 if part == 1 else 1 + 3
        elif line[0] == 'B':
            res = 3 + 2 if part == 1 else 2 + 3
        elif line[0] == 'C':
            res = 0 + 2 if part == 1 else 3 + 3
            
    elif line[1] == 'Z':
        if line[0] == 'A':
            res = 0 + 3 if part == 1 else 2 + 6
        elif line[0] == 'B':
            res = 6 + 3 if part == 1 else 3 + 6
        elif line[0] == 'C':
            res = 3 + 3 if part == 1 else 1 + 6
            
    return res


def compute_score(inp, part):
    total_sum = 0
    for line in inp:
        total_sum += game_outcome(line, part)
    return total_sum


# part 1
print("Result for part 1: ", compute_score(inp, 1))  # 13565

# part 2
print("Result for part 2: ", compute_score(inp, 2))  # 12424