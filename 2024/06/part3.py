# THIS SOLUTION FOR PART 2 DOESNT WORK

from colorama import Fore

mapa = [list(line.strip()) for line in open('in')]

start = None
for l, arr in enumerate(mapa):
    for c, v in enumerate(arr):
        if v == '^': start = (l,c)
        

direction = (-1,0)

path_directions = [[None for _ in line] for line in mapa]


directions = {
    (-1,0): (0,1),
    (0,1): (1,0),
    (1,0): (0,-1) ,
    (0,-1): (-1,0)
}

directions_print = {
    (-1,0): '^',
    (0,1): '>',
    (1,0): 'v' ,
    (0,-1): '<'
}
    
def print_map():
    sl, sc = start
    for l, arr in enumerate(mapa):
        for c, v in enumerate(arr):
            if sl == l and sc == c:
                print(Fore.YELLOW, end='')
                print('X', end = ' ')
            else:
                if not path_directions[l][c] == None:
                    print(Fore.MAGENTA+directions_print[path_directions[l][c][-1]], end=' ')
                else:    
                    print(v, end=' ')
            print(Fore.RESET, end='')
        print()

print_map()


from time import sleep
import os

def is_valid(l, c):
    return 0 <= l < len(mapa) and 0 <= c < len(mapa[0])

tot = 0

while True:
    y,x = direction
    l,c = start
    
    if path_directions[l][c] == None:
        path_directions[l][c] = [direction]
    else:
        if direction not in path_directions[l][c]: path_directions[l][c].append(direction)
    
    mapa[l][c] = 'O'
    
    next_direction = directions[direction]
    if next_direction in path_directions[l][c]:
        sleep(2)
        tot += 1
    
    nl, nc = l+y, c+x
    if not is_valid(nl, nc): break
    if mapa[nl][nc] == '#':
        y,x = direction
        reverse = (y*-1, x*-1)
        start_fill = start
        while True:
            y,x = reverse
            l,c = start_fill
            if path_directions[l][c] == None:
                path_directions[l][c] = [direction]
            else:
                if direction not in path_directions[l][c]: path_directions[l][c].append(direction)
            nl, nc = l+y, c+x
            if not is_valid(nl,nc) or mapa[nl][nc] == '#':
                break
            start_fill = (nl,nc)
            
        direction = next_direction
        continue
    start = (nl, nc)
    os.system('cls')
    print_map()
    sleep(.05)
    # input()
    
    
print(tot)
