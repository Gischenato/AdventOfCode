moviment_list = list(open('in').read())
rocks = [
    ((0,0), (1,0), (2,0), (3,0)),
    ((1,0), (0,1), (1,1), (1,2), (2,1)),
    ((0,0), (1,0), (2,0), (2,1), (2,2)),
    ((0,0), (0,1), (0,2), (0,3)),
    ((0,0), (0,1), (1,1), (1,0)),
]

fallen_rocks = set()

highest = 0

curr_rock = 0
curr_mov  = 0

def fall(rock):
    global highest, curr_mov, moviment_list
    Y = highest + 4
    X = 2
    while True:
        moviment = moviment_list[curr_mov%len(moviment_list)]
        curr_mov+=1

        change = True
        dX = 1 if moviment == '>' else -1
        for x,y in rock:
            if (x+X+dX) > 6 or (x+X+dX) < 0 or (x+X+dX, y+Y) in fallen_rocks: 
                change=False
                break 
        
        if change: X+=dX
        end = False
        for x,y in rock:
            if Y-1 <= 0 or (x+X, y+Y-1) in fallen_rocks:    
                end = True
                break
        if end:
            for x,y in rock:
                fallen_rocks.add((x+X, y+Y))
                highest = max(highest, y+Y)
            break
        Y-=1

for i in range(2022):
    fall(rocks[curr_rock%len(rocks)])
    curr_rock+=1
print(highest)