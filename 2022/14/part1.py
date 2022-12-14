wall = set()
sand = set()
wall2 = list()

for line in open('in'):
    line = line.strip().split(' -> ')
    current = []
    for val in line:
        pos = tuple(map(int, val.split(',')))
        current.append(pos)
        wall.add(pos)
        if pos not in wall2: wall2.append(pos)
    for i in range(len(current)):
        if i+1 == len(current): break
        initial = current[i]
        final = current[i+1]
        difX = final[0] - initial[0]
        difY = final[1] - initial[1]
        if difX > 0: 
            for i in range(1, difX+1): wall.add((initial[0]+i, initial[1]))
        elif difX < 0: 
            for i in range(difX, 0):   wall.add((initial[0]+i, initial[1]))
        
        if difY > 0: 
            for i in range(1, difY+1): wall.add((initial[0], initial[1]+i))
        elif difY < 0: 
            for i in range(difY, 0):   wall.add((initial[0], initial[1]+i))

pouring = (500, 0)

abys = max(wall, key=lambda x: x[1])[1]
print(abys)
def pourSand():
    global wall, sand, pouring, abys
    moved = True
    X,Y = pouring
    while moved:
        if Y == abys: return False
        for i,j in [(0,1), (-1,1), (1,1)]: 
            newPos = (X+i, Y+j)
            if newPos not in wall and newPos not in sand:
                X,Y = newPos
                moved = True
                break
            else:
                moved = False
    # print(f'Pouring at {X},{Y}')
    sand.add((X,Y))
    return True

# matriz = [['.' for i in range(40)] for j in range(20)]

while pourSand():
    pass


# print(sand)
# matriz[pouring[1]][pouring[0]-480] = '+'
# for pos in sand:
#     matriz[pos[1]][pos[0]-480] = '0'
# for pos in wall:
#     matriz[pos[1]][pos[0]-480] = '#'
# for v in matriz:
#     print(''.join(v))

print(len(sand))