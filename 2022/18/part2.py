faces = dict()

maxX = maxY = maxZ = int(-1e6)
minX = minY = minZ = int( 1e6)

droplet = set()
air = set()

looking_to = [
    (0, 0, .5),
    (0, .5, 0),
    (.5, 0, 0),
    (0, 0, -.5),
    (0, -.5, 0),
    (-.5, 0, 0)
]

for line in open('in'):
    x,y,z = map(int, line.split(','))
    
    for dX, dY, dZ in looking_to:
        face = (x+dX, y+dY, z+dZ)
        if face not in faces: faces[face] = 1
        else: faces[face] = 0
    
    droplet.add((x,y,z))
    maxX = max(maxX, x)
    maxY = max(maxY, y)
    maxZ = max(maxZ, z)
    
    minX = min(minX, x)
    minY = min(minY, y)
    minZ = min(minZ, z)

minX -= 1
minY -= 1
minZ -= 1

maxX += 1
maxY += 1
maxZ += 1

queue = [(minX, minY, minZ)]
air.add(queue[0])

next_block = [
    (0, 0, 1),
    (0, 1, 0),
    (1, 0, 0),
    (0, 0, -1),
    (0, -1, 0),
    (-1, 0, 0)
]

while queue:
    x,y,z = queue.pop(0)

    for dX, dY, dZ in next_block:
        nX, nY, nZ = (x+dX, y+dY, z+dZ)
        block = (nX, nY, nZ)    
        if not( minX <= nX <= maxX and
                minY <= nY <= maxY and
                minZ <= nZ <= maxZ): continue 
        
        if block in droplet or block in air: continue

        air.add(block)
        queue.append((nX,nY,nZ))

free_blocks = set()

for x,y,z in air:
    for dX, dY, dZ in looking_to:
        free_blocks.add((x+dX, y+dY, z+dZ))

total = 0

for face in faces:
    if face in free_blocks: total+=1

print(total)
