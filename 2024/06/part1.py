from colorama import Fore

mapa = [list(line.strip()) for line in open('in')]
# for line in open('ex'):
#     print(line)
start = None
for l, arr in enumerate(mapa):
    for c, v in enumerate(arr):
        if v == '^': start = (l,c)
        
# print(start)
direction = (-1,0)





directions = {
    (-1,0): (0,1),
    (0,1): (1,0),
    (1,0): (0,-1) ,
    (0,-1): (-1,0)
}

# for y,x in directions:
#     print(x,y)
#     mapa[start[0]+y][start[1]+x] = "!"
    
def print_map():
    sl, sc = start
    for l, arr in enumerate(mapa):
        for c, v in enumerate(arr):
            if sl == l and sc == c:
                print(Fore.YELLOW, end='')
                print('X', end = ' ')
            else: print(v, end=' ')
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
    if mapa[l][c] != 'O': tot+=1
    mapa[l][c] = 'O'
    nl, nc = l+y, c+x
    if not is_valid(nl, nc): break
    # print(nl,nc, (len(mapa), len(mapa[0])))
    if mapa[nl][nc] == '#':
        direction = directions[direction]
        continue
    start = (nl, nc)
    # os.system('cls')
    # print_map()
    # sleep(.2)
    
print(tot)