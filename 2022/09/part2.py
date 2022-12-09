locations = set()

POSITIONS = {
    0: [0,0],
    1: [0,0],
    2: [0,0],
    3: [0,0],
    4: [0,0],
    5: [0,0],
    6: [0,0],
    7: [0,0],
    8: [0,0],
    9: [0,0],
}

def needToMove(key):
    global POSITIONS, locations
    head = POSITIONS[key-1]
    tail = POSITIONS[key]
    difX = head[0] - tail[0]
    difY = head[1] - tail[1]
    total = abs(difX) + abs(difY)
    if total > 2:
        POSITIONS[key][1] += 1 if difY > 0 else -1
        POSITIONS[key][0] += 1 if difX > 0 else -1
    elif total == 2:
        POSITIONS[key][1] += 1 if difY == 2 else 0
        POSITIONS[key][0] += 1 if difX == 2 else 0
        POSITIONS[key][1] -= 1 if difY == -2 else 0
        POSITIONS[key][0] -= 1 if difX == -2 else 0

    newLoc = (POSITIONS[key][0], POSITIONS[key][1])
    if key == 9:
        locations.add(newLoc) 

def handleMovement():
    global POSITIONS, locations
    for key in POSITIONS:
        if key == 0: continue
        needToMove(key)

moviment = 0
for line in open('in'):
    direction, qnt = line.strip().split()
    where = 0
    dir = 0
    if   direction == 'R':
        where = 1
        dir = 1
    elif direction == 'L':
        where = 1
        dir = -1
    elif direction == 'U':
        where = 0
        dir = 1
    elif direction == 'D':
        where = 0
        dir = -1
    for i in range(int(qnt)):
        POSITIONS[0][where] += dir
        handleMovement()

print(len(locations))