import os
from time import sleep

data = [list(line.strip()) for line in open('in').readlines()]

start = (0, data[0].index('S'))

print(start)

def is_valid(l,c):
    if l < 0 or c < 0 or l >= len(data) or c >= len(data[0]):
        return False
    return True
tot = 0
to_do = [start]
while len(to_do) > 0:
    l,c = to_do.pop(0)
    if not is_valid(l,c):
        continue
    if is_valid(l+1, c):
        next_cell = data[l+1][c]
        
        if next_cell == '.':
            data[l+1][c] = '|'
            to_do.append((l+1, c))
        elif next_cell == '^':
            tot += 1
            if is_valid(l+1, c-1):
                data[l+1][c-1] = '|'
                to_do.append((l+1, c-1))
            if is_valid(l+1, c+1):
                data[l+1][c+1] = '|'
                to_do.append((l+1, c+1))
print(tot)