locations = set()

HEAD = [0 , 0]
TAIL = [0 , 0]
last = [0 , 0]

def needToMove():
    global HEAD, TAIL
    difX = abs(max(TAIL[0], HEAD[0]) - min(TAIL[0], HEAD[0]))
    difY = abs(max(TAIL[1], HEAD[1]) - min(TAIL[1], HEAD[1]))
    return difX, difY

for line in open('test'):
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
        newloc = (TAIL[0], TAIL[1])
        locations.add(newloc)
        last[0] = HEAD[0]
        last[1] = HEAD[1]
        HEAD[where] += dir
        difX, difY = needToMove()
        if difX > 1 or difY > 1:
            TAIL[0] = last[0] 
            TAIL[1] = last[1]
    newloc = (TAIL[0], TAIL[1])
    locations.add(newloc)

print(len(locations))