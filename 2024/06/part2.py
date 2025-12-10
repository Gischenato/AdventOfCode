from colorama import Fore

original_map = [list(line.strip()) for line in open('in')]

start = None
for l, arr in enumerate(original_map):
    for c, v in enumerate(arr):
        if v == '^': start = (l,c)

START_DIRECTION = (-1,0)
real_start = start

path_directions = [[None for _ in line] for line in original_map]

directions = {
    (-1,0): (0,1),
    (0,1): (1,0),
    (1,0): (0,-1) ,
    (0,-1): (-1,0)
}
curr = None
    
def print_map(mapa):
    sl, sc = start
    for l, arr in enumerate(mapa):
        for c, v in enumerate(arr):
            if curr and l == curr[0] and c == curr[1]:
                print(Fore.MAGENTA, end='')
                print('#', end = ' ')
            elif sl == l and sc == c:
                print(Fore.YELLOW, end='')
                print('X', end = ' ')
            else: print(v, end=' ')
            print(Fore.RESET, end='')
        print()

from time import sleep
import os

def is_valid(l, c):
    return 0 <= l < len(original_map) and 0 <= c < len(original_map[0])

tot = 0

for i, line in enumerate(original_map):
    print(i, len(original_map))
    for j, val in enumerate(line):
        mapa = [line.copy() for line in original_map]
        curr = (i,j)
        SEEN = set()
        start = real_start

        direction = START_DIRECTION
        while True:
            l,c = start
            if (l,c,direction) in SEEN:
                tot+=1
                break
            y,x = direction
            SEEN.add((l,c,direction))
            nl, nc = l+y, c+x
            if not is_valid(nl, nc): break
            mapa[l][c] = 'O'
            if mapa[nl][nc] == '#' or (nl == i and nc == j):
                direction = directions[direction]
                continue
            start = (nl, nc)
    
print(tot)